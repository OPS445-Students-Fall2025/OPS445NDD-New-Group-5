#!/usr/bin/env python3

"""
Firewall Module - Bhavya Patel

References:
    - nftables Wiki: https://wiki.nftables.org/
    - nftables Quick Reference: https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes
    - Python subprocess: https://docs.python.org/3/library/subprocess.html
    - Python os module: https://docs.python.org/3/library/os.html
"""

import os import subprocess

def configure_firewall(rules_path_arg=None): """ High-level firewall configuration flow.

Args:
    rules_path_arg (str or None):
        If provided, use this as nftables rules file path without asking.
        If None, ask user interactively.
"""
print("\n==== Firewall (nftables) Configuration ====\n")

# 1) Get rules file path
if rules_path_arg:
    rules_path = rules_path_arg
    print(f"Using nftables rules file path from CLI argument: {rules_path}")
else:
    while True:
        rules_path = input(
            "Enter full path to nftables rules file (e.g. /home/admin/rules.nft): "
        ).strip()
        if rules_path:
            break
        print("Please enter a path.")

# 2) Check file exists
if not os.path.isfile(rules_path):
    print(f"File '{rules_path}' not found. Aborting firewall configuration.")
    return

print(f"\nYou entered rules file: {rules_path}")
confirm = input(
    f"Do you want to apply nftables rules from this file using 'nft -f {rules_path}'? (y/n): "
).strip().lower()
if confirm != "y":
    print("Aborting firewall configuration by user choice.")
    return

# 3) Apply rules
try:
    print(f"\nApplying nftables rules from {rules_path}...\n")
    subprocess.check_call(["nft", "-f", rules_path])
    print("nftables rules applied successfully.\n")
except subprocess.CalledProcessError as e:
    print(f"Error applying nftables rules: {e}")
    return
except Exception as e:
    print(f"Unexpected error while running nft: {e}")
    return

# 4) Optional: show ruleset
show = input("Do you want to display the current nftables ruleset? (y/n): ").strip().lower()
if show == "y":
    try:
        print("\n==== Current nftables ruleset ====\n")
        subprocess.check_call(["nft", "list", "ruleset"])
    except Exception as e:
        print(f"Error listing nftables ruleset: {e}")
