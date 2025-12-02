#!/usr/bin/env python3

import subprocess

def run_cmd(cmd): """Run a shell command and return output as text.""" return subprocess.check_output(cmd, text=True).strip()

def show_current_interfaces(): """ Show current non-loopback interfaces and their IPs.

Returns:
    interfaces (list of (name, ip_str)) e.g. [("enp0s3", "192.168.1.10/24"), ...]
"""
print("Current network interfaces and IP addresses:\n")
output = run_cmd(["ip", "-br", "addr"])
lines = output.splitlines()

interfaces = []
index = 1
for line in lines:
    parts = line.split()
    if not parts:
        continue
    name = parts[0]
    if name == "lo":
        continue  # skip loopback
    ip_addr = "N/A"
    for p in parts[2:]:
        if "." in p:  # very simple IPv4 check
            ip_addr = p
            break
    interfaces.append((name, ip_addr))
    print(f"{index}) {name:10s}  {ip_addr}")
    index += 1

if not interfaces:
    print("No non-loopback interfaces found.")
print()
return interfaces
def choose_interface(interfaces): """ Ask the user to choose an interface by number.

Args:
    interfaces: list of (name, ip_str)

Returns:
    interface_name (str)
"""
if not interfaces:
    raise SystemExit("No interfaces to choose from. Exiting.")

while True:
    choice = input("Enter the number of the adapter you want to configure: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.")
        continue
    choice = int(choice)
    if 1 <= choice <= len(interfaces):
        return interfaces[choice - 1][0]
    else:
        print("Number out of range, try again.")
def get_current_ipv4(interface): """ Return current IPv4 address with CIDR for a given interface, or None.

Example return: '192.168.1.10/24'
"""
try:
    output = run_cmd(["ip", "-4", "addr", "show", "dev", interface])
except subprocess.CalledProcessError:
    return None

for line in output.splitlines():
    line = line.strip()
    if line.startswith("inet "):
        parts = line.split()
        if len(parts) >= 2:
            return parts[1]  # e.g. '192.168.1.10/24'

return None
def ask_dhcp_or_static(): """ Ask user whether to configure DHCP or Static.

Returns:
    mode (str): "dhcp" or "static"
"""
while True:
    ans = input("Use DHCP for this interface? (y/n): ").strip().lower()
    if ans == "y":
        return "dhcp"
    elif ans == "n":
        return "static"
    else:
        print("Please answer with 'y' or 'n'.")
def ask_ip_address(current_ip): """ Ask user if they want to keep the current IP or enter a new one.

Args:
    current_ip (str or None): e.g. '192.168.1.10/24'

Returns:
    address_cidr (str): e.g. '192.168.1.50/24'
"""
if current_ip:
    print(f"Current IPv4 on this interface: {current_ip}")
    keep = input("Do you want to keep this IP? (y/n): ").strip().lower()
    if keep == "y":
        return current_ip

while True:
    new_ip = input("Enter new IPv4 address with CIDR (e.g. 192.168.1.50/24): ").strip()
    # TODO (optional): add better validation for IP and prefix
    if "/" in new_ip and "." in new_ip:
        return new_ip
    else:
        print("Please enter a valid IP with CIDR, for example 192.168.1.50/24.")
def has_multiple_non_loopback_interfaces(): """ Check if there are 2 or more non-loopback interfaces.

Returns:
    bool
"""
interfaces = show_current_interfaces()
return len(interfaces) >= 2
