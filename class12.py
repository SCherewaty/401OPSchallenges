#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/14/2024
#Purpose: SCAPY practice part 2
#Sources: https://scapy.readthedocs.io/en/latest/usage.html#icmp-ping
#  https://stackoverflow.com/questions/61180264/find-webserver-listening-on-port-with-scapy-port-scanner
#  Also Gilbert Collado helped me with this during class.   

#Import scapy
from scapy.all import *
import logging

logging.getLogger("scapy.runtime").SetLevel(logging.ERROR)

# User input for specified range
target_IP = input("What is the target IP address? ")
start_port = int(input("What's the start of the port range? "))
end_port = int(input("What's the end of the range? "))

# Create ethernet frame that's empty and add an IP layer
my_frame = scapy.Ether() / scapy.ARP()

# Create the function
def scan_port(target_IP, port):
    syn_packet = IP(dst=target_IP) / TCP(dport=port, flags='S')
    response = sr1(syn_packet, timeout=2, verbose=0)
    
    if response is None:
        print(f"Port {port} is filtered already.")
        return
    
    if response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            rst_packet = IP(dst=target_IP) / TCP(dport=port, flags='R')
            send(rst_packet, verbose=0)
            print(f"Port {port} is open.")
        elif response[TCP].flags == 0x14:
            print(f"Port {port} is closed.")
        else:
            print(f"Port {port} is filtered.")
    else:
        print(f"Port {port} is filtered.")
        
def scan_ports(target_IP, port_range):
    
    for port in port_range:
        scan_port(host, port)

if __name__ == "__main__":
    target_host = "192.168.40.135"  
    ports_to_scan = range(20, 1025) 

    scan_ports(target_host, ports_to_scan)