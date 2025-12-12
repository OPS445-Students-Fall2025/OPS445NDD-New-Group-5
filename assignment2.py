#!/usr/bin/env python3
"""
OPS445 Assignment 2: Network Configuration and Firewall Automation Tool

A tool for automating network configuration (netplan) and firewall management (nftables)
on Linux systems.

Authors:
    - Nilkanthkumar Patel: network_core.py - Network interface discovery and validation
    - Himay Shah: netplan_utils.py - Netplan YAML generation and application
    - Bhavya Patel: firewall.py - Firewall (nftables) configuration
    - Vaidehi Patel: assignment2.py - Main integration and CLI

Usage:
    sudo python3 assignment2.py
    sudo python3 assignment2.py --mode network
    sudo python3 assignment2.py --mode firewall --rules /path/to/rules.nft
    sudo python3 assignment2.py --mode both
"""

import argparse
import sys
import os
import subprocess

# STEP 1: Checks Python Version (before any other imports)
# ============================================================================
if sys.version_info < (3, 6):
    print("\n" + "="*60)
    print("ERROR: This script requires Python 3.6 or higher")
    print("="*60)
    print(f"You are running Python {sys.version_info.major}.{sys.version_info.minor}")
    print("\nPlease upgrade Python or use a compatible environment.")
    print("="*60 + "\n")
    sys.exit(1)


# STEP 2: Checks Root Privileges 
# ============================================================================
def check_root_privileges():
    """
    Checks if the script is running with root/sudo privileges.
    
    Returns:
        bool: True if running as root, False otherwise
    """
    return os.geteuid() == 0


# Performs root check immediately
if not check_root_privileges():
    print("\n" + "="*60)
    print("ERROR: This script must be run with root privileges")
    print("="*60)
    print("\nUsage:")
    print("  sudo python3 assignment2.py")
    print("  sudo python3 assignment2.py --mode network")
    print("  sudo python3 assignment2.py --mode firewall --rules rules.nft")
    print("  sudo python3 assignment2.py --mode both")
    print("\n" + "="*60 + "\n")
    sys.exit(1)



# STEP 3: Import modules (after root check)
# ============================================================================
try:
    import netplan_utils
    import firewall
except ImportError as e:
    print("\n" + "="*60)
    print("ERROR: Failed to import required modules")
    print("="*60)
    print(f"\nDetails: {e}")
    print("\nPlease ensure all required files are in the same directory:")
    print("  - network_core.py     (Person 1)")
    print("  - netplan_utils.py    (Person 2)")
    print("  - firewall.py         (Person 3)")
    print("  - assignment2.py      (Person 4 - this file)")
    print("\n" + "="*60 + "\n")
    sys.exit(1)


# STEP 4: Argument Parsing
# ============================================================================
def parse_args():
    """
    Parses command-line arguments.
    Returns:
        argparse.Namespace: Parsed arguments containing mode, rules, etc.
    """
    parser = argparse.ArgumentParser(
        description="OPS445 Group Assignment 2: Network + Firewall Automation Tool",
        epilog="This tool must be run with root/sudo privileges.",
        #formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    
    parser.add_argument(
        "--mode",
        choices=["network", "firewall", "both"],
        help="What to configure: network, firewall, or both (network then firewall). "
             "If omitted, an interactive menu will be shown."
    )
    
    parser.add_argument(
        "--rules",
        metavar="PATH",
        help="Path to nftables rules file (used when mode=firewall or mode=both). "
             "If omitted, the script will ask interactively."
    )
    
    # parser.add_argument(
    #     "--interface",
    #     help="Interface name to configure (skips selection menu)"
    # )
    
    return parser.parse_args()


# STEP 5: Interactive Menu
# ============================================================================
def interactive_mode():
    """
    Shows an interactive menu for mode selection.
    Handles user input with validation and error handling.
    """
    print("\n" + "="*60)
    print("   Admin Helper: Network + Firewall Configuration")
    print("="*60)
    print("\nWhat do you want to configure?\n")
    print("  1) Network configuration (netplan)")
    print("  2) Firewall (nftables)")
    print("  3) Both (Network then Firewall)")
    print("  4) Exit")
    print()
    
    choice = None
    while choice not in ("1", "2", "3", "4"):
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice not in ("1", "2", "3", "4"):
                print("[ERROR] Invalid choice, please enter 1, 2, 3, or 4.")
        
        except KeyboardInterrupt:
            print("\n\n[INFO] Operation cancelled by user.")
            sys.exit(130)
        
        except EOFError:
            print("\n\n[ERROR] Unexpected end of input.")
            sys.exit(1)
    
    # Handle exit option
    if choice == "4":
        print("\n[INFO] Exiting. Goodbye!\n")
        sys.exit(0)
    
    # Execute based on choice
    try:
        if choice == "1":
            print("\n" + "="*60)
            print("        NETWORK CONFIGURATION")
            print("="*60)
            netplan_utils.configure_network()
        
        elif choice == "2":
            print("\n" + "="*60)
            print("        FIREWALL CONFIGURATION")
            print("="*60)
            firewall.configure_firewall()
        
        elif choice == "3":
            print("\n" + "="*60)
            print("        STEP 1/2: NETWORK CONFIGURATION")
            print("="*60)
            netplan_utils.configure_network()
            
            print("\n" + "="*60)
            print("        STEP 2/2: FIREWALL CONFIGURATION")
            print("="*60)
            firewall.configure_firewall()
        
        print("\n" + "="*60)
        print("        OPERATION COMPLETED SUCCESSFULLY")
        print("="*60 + "\n")
    
    except KeyboardInterrupt:
        print("\n\n[INFO] Operation cancelled by user.")
        sys.exit(130)
    
    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


# STEP 6: Main Function
# ============================================================================
def main():
    """
    Main function - entry point of the program.
    Manages and controls the workflow based on arguments or interactive mode.
    """
    # Parse command-line arguments
    args = parse_args()
    
    try:
        # If mode not provided → interactive selection
        if not args.mode:
            interactive_mode()
            return
        
        # Non-interactive mode via CLI
        print(f"\n[INFO] Running in non-interactive mode: {args.mode}\n")
        
        if args.mode == "network":
            print("="*60)
            print("        NETWORK CONFIGURATION")
            print("="*60)
            netplan_utils.configure_network()
        
        elif args.mode == "firewall":
            print("="*60)
            print("        FIREWALL CONFIGURATION")
            print("="*60)
            firewall.configure_firewall(rules_path_arg=args.rules)
        
        elif args.mode == "both":
            print("="*60)
            print("        STEP 1/2: NETWORK CONFIGURATION")
            print("="*60)
            netplan_utils.configure_network()
            
            print("\n" + "="*60)
            print("        STEP 2/2: FIREWALL CONFIGURATION")
            print("="*60)
            firewall.configure_firewall(rules_path_arg=args.rules)
        
        print("\n" + "="*60)
        print("        OPERATION COMPLETED SUCCESSFULLY")
        print("="*60 + "\n")
    
    except KeyboardInterrupt:
        print("\n\n[INFO] Operation cancelled by user.")
        sys.exit(130)
    
    except Exception as e:
        print(f"\n[ERROR] Operation failed: {e}")
        import traceback
        print("\n--- Error Details ---")
        traceback.print_exc()
        print("-" * 60 + "\n")
        sys.exit(1)


# STEP 7: Entry Point
# ============================================================================
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[FATAL ERROR] Unhandled exception: {e}")
        sys.exit(1)
