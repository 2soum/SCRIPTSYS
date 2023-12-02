# README for IP Network Utilities Script

## Overview
This script provides a range of utilities for handling IP addresses and network calculations. It includes functions for CIDR (Classless Inter-Domain Routing) manipulation, IP address classification, subnet calculations, and more. It's a valuable tool for network administrators, students learning about networking, or anyone needing to perform IP-related computations.

## Features
- **Convert CIDR notation to subnet mask and vice versa.**
- **Calculate network and broadcast addresses** from an IP address and subnet mask.
- **Determine the number of usable hosts** in a subnet.
- **Convert IP addresses** between binary and decimal formats.
- **Classify IP addresses** into classes (A, B, C, D, E).
- **Identify if an IP address is private or public.**
- **Calculate the next subnet** based on the given IP address and subnet mask.

## Requirements
- Python 3.x

## Installation
1. **Clone the repository** or download the script.
2. Ensure **Python 3.x** is installed on your system.

## Usage
Run the script in a Python environment:
```bash
python main.py
```
Follow the on-screen menu to choose the desired operation. Input the required data as prompted, and the script will display the results.

## Functions
- `XtoMASK(X)`: Converts CIDR notation (e.g., /24) to a subnet mask (e.g., 255.255.255.0).
- `MasktoX(mask)`: Converts a subnet mask to CIDR notation.
- `calculate_network_and_broadcast(ip_address, subnet_mask)`: Calculates network and broadcast addresses from an IP address and a subnet mask.
- `hosts_usable(subnet_mask)`: Calculates the number of usable hosts in a subnet.
- `ip_to_binary(ip), binary_to_ip(binary)`: Converts between binary and decimal IP formats.
- `calculate_ip_class(ip)`: Determines the class of an IP address.
- `is_private_ip(ip)`: Checks if an IP address is private.
- `find_next_subnet(ip_address, subnet_mask)`: Calculates the next subnet address.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Contact
Dayssam BAKAAR - dayssam.bakaar@gmail.com
