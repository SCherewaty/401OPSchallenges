#!/usr/bin/env python3

#Author: Steve Cherewaty
#Date: 06/25/2024
#Purpose: Attack Tools Pt 2
#Sources: 
# 
# https://thepythoncode.com/article/make-a-xss-vulnerability-scanner-in-python
# Conferred with ChatGPT for this assignment

import nmap

scanner = nmap.PortScanner()

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

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    ### TODO: Add missing code block here
    print("Please enter a valid option") ### TODO: Remove this
elif resp == '3':
    ### TODO: Add missing code block here
    print("Please enter a valid option") ### TODO: Remove this
elif resp >= '4':
    print("Please enter a valid option")
``