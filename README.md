### Python Network Scanning Tool

This is a simple Python tool for scanning all the open ports of a specific IP address. It is useful for network administrators and security professionals to identify open ports on their networks.

# Usage:

To use the tool, simply run it with the IP address of the device you want to scan. For example, to scan the IP address 192.168.1.1, you would run the following command:
- ```bash
  python scanner.py 192.168.1.1

You can also specify the hostname of the device instead of the IP address. For example, to scan the hostname example.com, you would run the following command:

- ```bash
  python scanner.py example.com

The tool will scan all the ports from 1 to 6000 and print the open ports to the console.

Example output:

port 22: OPEN
port 80: OPEN
port 443: OPEN
processes finished


# Installation:

To install the tool, simply clone the GitHub repository and run the following command:
- ```bash
  git clone https://github.com/huho-0/port-scan
  cd port-scan
  python3 setup.py install

This will install the tool in your Python environment.

Contributing:

If you have any suggestions or bug reports, please feel free to create an issue on the GitHub repository.
