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

# Disable Scapy's verbose logging output
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def scan_ports(host, port):
  
    # Create a SYN packet with the target host and port
    syn_packet = IP(dst=host) / TCP(dport=port, flags='S')
    response = sr1(syn_packet, timeout=2, verbose=0)
    
    if response is None:
        # No response received, port is considered filtered and silently dropped
        print(f"Port {port} is filtered and dropped.")
        return
    
    # Check if the response contains a TCP layer
    if response.haslayer(TCP):
        # Check the TCP flags in the response
        if response[TCP].flags == 0x12:  # SYN-ACK response indicates the port is open
            # Create and send a RST packet to gracefully close the connection
            rst_packet = IP(dst=host) / TCP(dport=port, flags='R')
            send(rst_packet, verbose=0)
            print(f"Port {port} is open.")
        elif response[TCP].flags == 0x14:  # RST-ACK response indicates the port is closed
            print(f"Port {port} is closed.")
        else:
            # Any other response is considered as the port being filtered
            print(f"Port {port} is filtered.")
    else:
        # No TCP layer in the response, port is considered filtered
        print(f"Port {port} is filtered.")

def scan_ports(host, port_range):
 
    for port in port_range:
        scan_ports(host, port)

if __name__ == "__main__":
     # Define the host IP to scan
    target_host = "192.168.40.135" 
    # Define the range of ports to scan (from port 20 to 1024)
    ports_to_scan = range(20, 1025)  

    scan_ports(target_host, ports_to_scan)  
    
    