#!/usr/bin/env python3

import os
import sys

# Check for root/sudo privileges
if os.geteuid() != 0:
    print("\n" + "="*60)
    print("ERROR: This script must be run with root privileges")
    print("="*60)
    print("\nUsage:")
    print("  sudo python3 assignment2.py")
    print("  sudo python3 assignment2.py --mode network")
    print("  sudo python3 assignment2.py --mode firewall --rules rules.nft")
    print("\n" + "="*60 + "\n")
    sys.exit(1)
