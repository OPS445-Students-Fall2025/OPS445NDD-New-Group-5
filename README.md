# Network Configuration and Firewall Automation Tool

**OPS445 Assignment 2 - Group Project**  
**Seneca College - Fall 2024**

A comprehensive Python-based automation tool for managing network configurations (netplan) and firewall rules (nftables) on Linux systems.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Educational-green)](LICENSE)
[![Course](https://img.shields.io/badge/course-OPS445-orange)](https://www.senecacollege.ca/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Team Members & Contributions](#team-members--contributions)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Quick Start](#quick-start)
  - [Interactive Mode](#interactive-mode)
  - [Command-Line Mode](#command-line-mode)
  - [Command-Line Options](#command-line-options)
  - [Usage Examples](#usage-examples)
- [Project Structure](#project-structure)
- [Module Documentation](#module-documentation)
- [Configuration Examples](#configuration-examples)
- [Troubleshooting](#troubleshooting)
- [Testing](#testing)
- [Safety Features](#safety-features)
- [Known Limitations](#known-limitations)
- [References and Research](#references-and-research)
- [Git Workflow](#git-workflow)
- [Academic Integrity](#academic-integrity)
- [License](#license)

---

## 🎯 Overview

This tool automates the complex and error-prone processes of network interface configuration and firewall rule management on Linux systems. It is specifically designed for Ubuntu systems using **netplan** for network management and **nftables** for firewall configuration.

### Why This Tool?

- **Reduces Human Error**: Validates all inputs before applying changes
- **Saves Time**: Automates multi-step configuration processes
- **Provides Safety**: Backs up configurations before modifications
- **Improves Accessibility**: Offers both interactive and scriptable interfaces
- **Educational Value**: Demonstrates system administration automation with Python

### Core Functionality

The tool provides two operational modes:

1. **Interactive Mode**: Menu-driven interface for manual administration
2. **Command-Line Mode**: Argument-based interface for automation and scripting

---

## ✨ Features

### Network Configuration Features
- ✅ Automatic network interface discovery using `ip` command
- ✅ Display current IP configurations with interface status
- ✅ DHCP or Static IP configuration options
- ✅ Custom DNS server configuration (can override DHCP DNS)
- ✅ Default gateway configuration with subnet validation
- ✅ IP address validation (CIDR notation) with range checking
- ✅ Automatic timestamped backups of existing configurations
- ✅ IPv4 forwarding enablement for routing/gateway scenarios
- ✅ Interactive prompts with comprehensive validation
- ✅ Preview generated configuration before applying

### Firewall Configuration Features
- ✅ nftables rules application from external rule files
- ✅ Rules file validation before application
- ✅ Display current firewall ruleset for review
- ✅ Interactive confirmation prompts for safety
- ✅ Support for custom rules files with any path
- ✅ Automatic nftables installation option (interactive mode)

### General Features
- ✅ Root privilege checking with clear error messages
- ✅ Distribution detection (Ubuntu, Debian, CentOS, RHEL, Fedora)
- ✅ Dependency verification (netplan, nftables, system tools)
- ✅ Comprehensive error handling with helpful messages
- ✅ Verbose mode for debugging (`-v`, `--verbose`)
- ✅ **Both short and long command-line options** (`-m`/`--mode`, `-r`/`--rules`)
- ✅ Keyboard interrupt handling (graceful Ctrl+C handling)
- ✅ Professional CLI interface with styled output using box-drawing characters
- ✅ Detailed logging and progress indicators
- ✅ Informative output at every step

---

## 👥 Team Members & Contributions

| Member | Role | Responsibility | Files | Contribution % |
|--------|------|----------------|-------|----------------|
| **Nilkanthkumar Patel** | Network Core Developer | Interface discovery, IP validation, user input handling | `network_core.py` | 25% |
| **Himay Shah** | Netplan Specialist | YAML generation, netplan application, IP forwarding | `netplan_utils.py` | 25% |
| **Bhavya Patel** | Firewall Engineer | nftables integration, rules application | `firewall.py` | 25% |
| **Vaidehi Patel** | Integration Lead | CLI interface, module coordination, error handling | `assignment2.py` | 25% |

### Division of Work

**Nilkanthkumar Patel (Network Core):**
- Interface discovery using `ip addr show`
- IP address validation (IPv4 with CIDR)
- Gateway and DNS validation
- User input collection and validation
- Current IP detection functions

**Himay Shah (Netplan Utilities):**
- Netplan YAML generation for DHCP and Static configurations
- File backup with timestamps
- Configuration file writing with proper permissions
- Netplan application (`netplan apply`)
- IP forwarding configuration via sysctl

**Bhavya Patel (Firewall):**
- nftables rules file validation
- Rules application using `nft -f`
- Current ruleset display (`nft list ruleset`)
- Interactive confirmation workflows

**Vaidehi Patel (Main Integration):**
- Command-line argument parsing (with short and long options)
- System detection and validation
- Module integration and orchestration
- Error handling framework
- Interactive menu system
- Documentation (README, REFERENCES, RESEARCH)

---

## 💻 System Requirements

### Supported Operating Systems
- **Ubuntu 18.04 LTS** or newer (recommended)
- **Ubuntu 20.04 LTS** (tested)
- **Ubuntu 22.04 LTS** (tested)
- Debian 10+ with netplan installed
- Other Linux distributions (limited support - netplan required)

### Required Software

| Component | Minimum Version | Purpose | Installation |
|-----------|----------------|---------|--------------|
| **Python** | 3.6+ | Script runtime | Pre-installed on Ubuntu 18.04+ |
| **netplan** | 0.98+ | Network configuration | `sudo apt install netplan.io` |
| **nftables** | 0.9.0+ | Firewall management | `sudo apt install nftables` |
| **iproute2** | 4.15+ | Network interface tools (`ip` command) | Usually pre-installed |
| **systemctl** | systemd | Service management | Usually pre-installed |

### System Permissions
- **Root/sudo access**: Required for all network and firewall operations
- **Read access**: `/etc/netplan/`, `/etc/os-release`
- **Write access**: `/etc/netplan/`, `/etc/sysctl.d/`

---

## 📦 Installation

### Method 1: Git Clone (Recommended)
```bash
