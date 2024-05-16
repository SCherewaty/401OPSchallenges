#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/15/2024
#Purpose: SCAPY practice part 3
#Sources: https://scapy.readthedocs.io/en/latest/usage.html#icmp-ping 
#  https://stackoverflow.com/questions/61180264/find-webserver-listening-on-port-with-scapy-port-scanner
# Also filled in gaps with what Ethan and Ricky covered in review.

#Import scapy
from scapy.all import IP, TCP, sr1, send, ICMP
import logging  
from ipaddress import IPv4Network


def ping_host(ip):
    response = sr1(IP(dst=ip)/ICMP(), timeout=2, verbose=0)
    return response == None 

def scan_ports(ip):
    common_ports = [22, 23, 443]
    open_ports = []
    
    for port in common_ports:
        response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), timeout=1, verbose=0) 
        if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
            open_ports.append(port)
            sr1(IP(dst=ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)
            
    if open_ports:
        print(f"Ports are OPEN on {ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No OPEN port on {ip}.")
        
def main():
    while True:
        ip = input("Enter an IP address: ")
        if ip.lower() =='exit':
            break
        if ping_host(ip):
            print(f"Host {ip} is successful.")
            scan_ports(ip)
        else:
            print(f"Host {ip} was NOT successful")
            
if __name__ == "__main__":
    main()
    



  
   