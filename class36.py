#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/12/2024
#Purpose: Signature based malware PART 3
#Sources: https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/
# Conferred with ChatGPT for this assignment

import os
import subprocess

# Function 1
def banner_grab_with_netcat(target, port):
    print(f"\n[+] Banner grabbing using Netcat on {target}:{port}")
    try:
        result = subprocess.check_output(f"nc -vz {target} {port}", shell=True, stderr=subprocess.STDOUT, timeout=10)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
    except subprocess.TimeoutExpired:
        print("Netcat command timed out.")
# Function 2
def banner_grab_with_netcat(target, port):
    print(f"\n[+] Banner grabbing using Netcat on {target}:{port}")
    try:
        result = subprocess.check_output(f"nc -vz {target} {port}", shell=True, stderr=subprocess.STDOUT, timeout=10)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
    except subprocess.TimeoutExpired:
        print("Netcat command timed out.")
        
