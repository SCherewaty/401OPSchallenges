#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/12/2024
#Purpose: Signature based malware PART 3
#Sources: https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/
# Conferred with ChatGPT for this assignment

import os
import subprocess

# Function 1 - grab the banner with NetCat
def banner_grab_with_netcat(target, port):
    print(f"\n[+] Grabbing a banner using Netcat on {target}:{port}")
    try:
        result = subprocess.check_output(f"nc -vz {target} {port}", shell=True, stderr=subprocess.STDOUT, timeout=10)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
    except subprocess.TimeoutExpired:
        print("Netcat command timed out.")

# Function 2 - grab the banner with Telnet
def banner_grab_with_telnet(target, port):
    print(f"\n[+] Banner grabbing using Telnet on {target}:{port}")
    try:
        result = subprocess.check_output(f"echo quit | telnet {target} {port}", shell=True, stderr=subprocess.STDOUT, timeout=10)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
    except subprocess.TimeoutExpired:
        print("Telnet command timed out.")
        
# Function 3 - grab the banner with Nmap
def banner_grab_with_nmap(target):
    print(f"\n[+] Banner grabbing using Nmap on {target}")
    try:
        result = subprocess.check_output(f"nmap -sV {target}", shell=True, stderr=subprocess.STDOUT, timeout=60)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
    except subprocess.TimeoutExpired:
        print("Nmap command timed out.")

# Prompt user for input
def get_user_input():
    target = input("Please enter the URL or IP address: ")
    port = input("Please enter the port number: ")
    return target, port       
          
# Main function
def main():
    target, port = get_user_input()
    banner_grab_with_netcat(target, port)
    banner_grab_with_telnet(target, port)
    banner_grab_with_nmap(target)
        
# Run the main function
if __name__ == "__main__":
    main()