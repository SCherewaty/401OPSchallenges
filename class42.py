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
    
range = '1-50'

### TODO: Prompt the user to type in a port range for this tool to scan

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