#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/14/2024
#Purpose: SCAPY practice part 2
#Sources: https://scapy.readthedocs.io/en/latest/usage.html#icmp-ping 

#Import scapy
from scapy.all import IP, TCP, sr1, send
import logging  

# Disable Scapy's verbose logging output
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Add a menu that gives choices to include ICMP scan
def display_menu():
    menu = {
        '1': "Search via TCP.", 
        '2': "Search via ICMP.",
        'E': "Exit."
    }

    options = sorted(menu.keys())
    for entry in options:
        print(entry, menu[entry])
    
def main():
    while True:
        display_menu()
        selection = input("Please Select (1, 2, or E): ")
        if selection == '1':
            print("TCP")
            # TCP 
        elif selection == '2':
            print("ICMP")
            # ICMP
        elif selection == 'E':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter 1 for TCP, 2 for ICMP, or E to exit.")

if __name__ == "__main__":
    main()

def scan_port(host, port):
  
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
        if response[TCP].flags == 0x12: 
            # Create and send a RST packet to close the connection
            rst_packet = IP(dst=host) / TCP(dport=port, flags='R')
            send(rst_packet, verbose=0)
            print(f"Port {port} is open.")
        elif response[TCP].flags == 0x14: 
            print(f"Port {port} is closed.")
        else:
            # Any other response is considered as the port being filtered
            print(f"Port {port} is filtered.")
    else:
        # No TCP layer in the response, port is considered filtered
        print(f"Port {port} is filtered.")

def scan_ports_range(host, port_range):
 
    for port in port_range:
        scan_port(host, port)

if __name__ == "__main__":
     # Define the host IP to scan
    target_host = "192.168.40.135" 
    # Define the range of ports to scan (from port 20 to 1024)
    ports_to_scan = range(20, 25)  

    scan_ports_range(target_host, ports_to_scan)  
  
    
    