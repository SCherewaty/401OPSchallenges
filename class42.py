#!/usr/bin/env python3

#Author: Steve Cherewaty
#Date: 06/25/2024
#Purpose: Attack Tools Pt 2
#Sources: Demo Code + https://pypi.org/project/python-nmap/
# Conferred with ChatGPT for this assignment

#!/usr/bin/env python3

import nmap

def print_scan_info(scanner, ip_addr):
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("All Protocols: ", scanner[ip_addr].all_protocols())

def main():
    scanner = nmap.PortScanner()
    print("Nmap Automation Tool")
    print("--------------------")

    ip_addr = input("IP address to scan: ")
    print(f"The IP you entered is: {ip_addr}")

    scan_type = input("Select scan to execute:\n1) SYN ACK Scan\n2) UDP Scan\n3) OS Detection\n")
    ports = input("Enter the port range (e.g., 1-100): ")

    if scan_type == '1':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, ports, '-v -sS')
        print_scan_info(scanner, ip_addr)
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    elif scan_type == '2':
        scanner.scan(ip_addr, ports, '-v -sU')
        print_scan_info(scanner, ip_addr)
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    elif scan_type == '3':
        scanner.scan(ip_addr, ports, '-v -O')
        print_scan_info(scanner, ip_addr)
        if 'osclass' in scanner[ip_addr]:
            for osclass in scanner[ip_addr]['osclass']:
                print(f"The OS of {ip_addr} is {osclass['osfamily']} {osclass['osgen']}")
        else:
            print("No OS information available.")
    else:
        print("Please enter a valid option")

if __name__ == "__main__":
    main()
