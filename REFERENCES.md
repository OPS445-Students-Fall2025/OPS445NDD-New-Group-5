# References and Resources Used

## Official Documentation

### Python Standard Library
1. **subprocess module** - Running external commands
   - URL: https://docs.python.org/3/library/subprocess.html
   - Used for: Executing system commands (ip, netplan, nft)

2. **argparse module** - Command-line argument parsing
   - URL: https://docs.python.org/3/library/argparse.html
   - Used for: Creating CLI interface with --mode and --rules arguments

3. **os module** - Operating system interface
   - URL: https://docs.python.org/3/library/os.html
   - Used for: Root privilege checking (os.geteuid()), file operations

4. **sys module** - System-specific parameters
   - URL: https://docs.python.org/3/library/sys.html
   - Used for: Exit codes, Python version checking

5. **shutil module** - High-level file operations
   - URL: https://docs.python.org/3/library/shutil.html
   - Used for: Backing up netplan configuration files

6. **datetime module** - Date and time handling
   - URL: https://docs.python.org/3/library/datetime.html
   - Used for: Timestamping backup files

7. **re module** - Regular expressions
   - URL: https://docs.python.org/3/library/re.html
   - Used for: IP address validation and parsing

---

## Network Configuration

### Netplan Documentation
1. **Netplan Official Documentation**
   - URL: https://netplan.io/
   - Used for: Understanding netplan configuration format and syntax

2. **Netplan Reference Guide**
   - URL: https://netplan.io/reference/
   - Used for: YAML structure, dhcp4, addresses, routes, nameservers configuration

3. **Netplan Examples**
   - URL: https://netplan.io/examples/
   - Used for: Static IP and DHCP configuration examples

4. **Ubuntu Server Network Configuration**
   - URL: https://ubuntu.com/server/docs/network-configuration
   - Used for: Best practices for Ubuntu network configuration

---

## Firewall Configuration

### nftables Documentation
1. **nftables Wiki**
   - URL: https://wiki.nftables.org/
   - Used for: Understanding nftables syntax and rule structure

2. **nftables Quick Reference**
   - URL: https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes
   - Used for: Command syntax for applying and listing rules

3. **nftables vs iptables**
   - URL: https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables
   - Used for: Understanding differences between iptables and nftables

---

## Linux System Administration

1. **ip command man page**
   - Command: `man ip`
   - URL: https://man7.org/linux/man-pages/man8/ip.8.html
   - Used for: Interface discovery, IP address parsing

2. **sysctl command and configuration**
   - Command: `man sysctl`
   - URL: https://man7.org/linux/man-pages/man8/sysctl.8.html
   - Used for: Enabling IP forwarding (net.ipv4.ip_forward)

3. **systemctl man page**
   - Command: `man systemctl`
   - URL: https://man7.org/linux/man-pages/man1/systemctl.1.html
   - Used for: Service management and status checking

---

## Programming Concepts and Best Practices

1. **PEP 8 - Style Guide for Python Code**
   - URL: https://peps.python.org/pep-0008/
   - Used for: Code formatting, naming conventions, documentation standards

2. **PEP 257 - Docstring Conventions**
   - URL: https://peps.python.org/pep-0257/
   - Used for: Writing proper docstrings for modules and functions

3. **Real Python - Command Line Interfaces in Python**
   - URL: https://realpython.com/command-line-interfaces-python-argparse/
   - Used for: Implementing argparse for CLI arguments

4. **Python Exception Handling Best Practices**
   - URL: https://realpython.com/python-exceptions/
   - Used for: Error handling with try-except blocks

---

## Network Concepts

1. **CIDR Notation Explanation**
   - URL: https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing
   - Used for: Understanding and validating IP addresses with CIDR notation

2. **IP Addressing and Subnetting**
   - URL: https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html
   - Used for: Understanding subnet masks, gateway validation

3. **DNS Configuration Best Practices**
   - URL: https://www.cloudflare.com/learning/dns/what-is-dns/
   - Used for: Understanding DNS server configuration

---

## Security Concepts

1. **Linux File Permissions**
   - URL: https://www.redhat.com/sysadmin/linux-file-permissions-explained
   - Used for: Setting proper permissions on configuration files (chmod 600)

2. **Principle of Least Privilege**
   - URL: https://en.wikipedia.org/wiki/Principle_of_least_privilege
   - Used for: Understanding why root privileges are required

3. **IP Forwarding Security Implications**
   - URL: https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt
   - Used for: Understanding risks of enabling IP forwarding

---

## Course Materials

1. **OPS445 Course Notes**
   - Source: Seneca College OPS445 Course Materials
   - Used for: Understanding network automation requirements

2. **OPS445 Course Notesn**
   - Source: Seneca College OPS445 Course Materials
   - Used for: Understanding system-level Python programming

3. **OPS445 Assignment 2 Requirements**
   - Source: Seneca College OPS445 Assignment Specification
   - Used for: Project requirements and deliverables

---

## Additional Resources

1. **Ubuntu Community Help - Networking**
   - URL: https://help.ubuntu.com/community/NetworkConfigurationCommandLine
   - Used for: Understanding Ubuntu-specific network configuration
---

## Testing and Debugging Tools

1. **journalctl man page**
   - Command: `man journalctl`
   - URL: https://man7.org/linux/man-pages/man1/journalctl.1.html
   - Used for: Debugging network and firewall issues

---

## Git and Version Control

1. **Git Documentation - Commit Messages**
   - URL: https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
   - Used for: Writing meaningful commit messages

2. **Conventional Commits**
   - URL: https://www.conventionalcommits.org/
   - Used for: Standardized commit message format

---

## Notes

All URLs were last accessed in December 2024 during the development of this assignment.

All Python standard library references are from Python 3.6+ documentation to ensure compatibility with the minimum required version.

Course materials are proprietary to Seneca College and used in accordance with academic integrity policies.
