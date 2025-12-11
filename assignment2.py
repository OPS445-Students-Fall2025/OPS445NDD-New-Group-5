#!/usr/bin/env python3

import argparse
import sys
import os
import subprocess
#import netplan_utils
#import firewall

# Check for Python Version 
if sys.version_info < (3, 6):
    print("ERROR: This script requires Python 3.6 or higher.")
    print(f"You are running Python {sys.version_info.major}.{sys.version_info.minor}")
    print("\nPlease upgrade Python or use a compatible environment.")
    sys.exit(1)

# Check for Root/Sudo Privileges
def check_root_privileges():
    if os.geteuid() != 0:
        print("\n" + "="*60)
        print("ERROR: This script must be run with root privileges")
        print("="*60)
        print("\nUsage:")
        print("  sudo python3 assignment2.py")
        #print("  sudo python3 assignment2.py --mode network")
        #print("  sudo python3 assignment2.py --mode firewall --rules rules.nft")
        print("\n" + "="*60 + "\n")
        #sys.exit(1)

try: 
    import netplan_utils
    import firewall
    import network_core
except ImportError as e:
    print("Error: Failed to import required modules")
    print(f"\nDetails:")
    print("\nPlease ensure all required files are present:")
    print("   - network_core.py")
    print("   - netplan_utils.py")
    print("   - firewall.py")
    print("   - assignment2.py")
    print("\nAll files must be in the same directory.")
    sys.exit(1)

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="OPS445 Group Assignment 2: Network + Firewall Automation Tool"
    )

    parser.add_argument(
        "--mode",
        choices=["network", "firewall", "both"],
        help="What to configure: network, firewall, or both (network then firewall). "
             "If omitted, an interactive menu will be shown."
    )

    parser.add_argument(
        "--rules",
        help="Path to nftables rules file (used when mode=firewall or mode=both). "
             "If omitted, the script will ask interactively."
    )

    # You can add more options later if needed, e.g.:
    # parser.add_argument("--interface", help="Interface name to configure (skips selection menu)")

    return parser.parse_args()

# Interactive menu
def interactive_mode():
    """
    Shows a simple interactive menu for mode selection.
    It also handles user input with validation and error.
    """
    print("\n" + "="*60)
    print("    Admin Helper: Network + Firewall Configuration")
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
        except E0Error:
            print("\n\n[ERROR] Unexpected end of input.")
            sys.exit(1)
    
    # Handle exit option
    if choice == "4":
        print("\n[INFO] Exiting. Goodbye!\n")
        sys.exit(0)

    # Execute bsed on choice
    try:
        if choice == "1":
            print("\n" + "="*60)
            print("     NETWORK CONFIGURATION")
            print("="*60)
            netplan_utils.configure_network()
        elif choice == "2":
            firewall.configure_firewall()
    elif choice == "3":
        netplan_utils.configure_network()
        firewall.configure_firewall()


def main():
    args = parse_args()

    # If mode not provided → interactive selection
    if not args.mode:
        interactive_mode()
        return

    # Non-interactive mode via CLI
    if args.mode == "network":
        netplan_utils.configure_network()
    elif args.mode == "firewall":
        firewall.configure_firewall(rules_path_arg=args.rules)
    elif args.mode == "both":
        netplan_utils.configure_network()
        firewall.configure_firewall(rules_path_arg=args.rules)


if __name__ == "__main__":
    main(
