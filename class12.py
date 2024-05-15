#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/14/2024
#Purpose: SCAPY practice part 2
#Sources: https://scapy.readthedocs.io/en/latest/usage.html#icmp-ping 

#Import scapy
from scapy.all import IP, TCP, sr1, send, ICMP
import logging  
from ipaddress import IPv4Network

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


def scan_port(host, port):
  
    # Create a SYN packet with the target host and port
    syn_packet = IP(dst=host) / TCP(dport=port, flags='S')
    response = sr1(syn_packet, timeout=2, verbose=0)
    
    if response is None:
        # No response received, port is considered filtered and silently dropped
        return f"Port {port} is filtered and dropped."
    
    # Check if the response contains a TCP layer
    if response.haslayer(TCP):
        # Check the TCP flags in the response
        if response[TCP].flags == 0x12: 
            # Create and send a RST packet to close the connection
            rst_packet = IP(dst=host) / TCP(dport=port, flags='R')
            send(rst_packet, verbose=0)
            print(f"Port {port} is open.")

        elif response[TCP].flags == 0x14: 
            return f"Port {port} is closed."

        else:
            # Any other response is considered as the port being filtered
            return f"Port {port} is filtered."
    else:
        # No TCP layer in the response, port is considered filtered
        return f"Port {port} is filtered."

def scan_ports_range():
    # Define the host IP to scan
    target_host = input("Please enter a target IP: ") or "10.0.0.145" 
    # Define the range of ports to scan (from port 20 to 1024)
    ports_to_scan = [22, 23, 80, 443, 3389] 

    for port in ports_to_scan:
        scan_port(target_host, port)

# Ping sweep function
# This function gets a CIDR block address from the user then it pings each host and responds based on the challenge requirements
# It then counts how many hosts are online using an incrementing variable to do so.
def ping_sweep():

    # user input for IPv4 CIDR block
    network = input("Please enter the CIDR block for the IPv4 network you want to scan: ")

    # Variables for creating a list of addresses from the chosen network and setting a live host counter
    addresses = IPv4Network(network)
    live_count = 0

    # Send ICMP ping request, wait for reply
    for host in addresses:
        if (host in (addresses.network_address, addresses.broadcast_address)):
            # Skip these two addresses
            continue

        resp = sr1(IP(dst=str(host))/ICMP(),timeout=1,verbose=0)

        if resp is None:
            return f"{host} is down or not responding. "

        elif (
            int(resp.getlayer(ICMP).type) == 3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            return f"{host} is blocking ICMP traffic."
        else:
            return f"{host} is responding."
            live_count += 1

    return f"{live_count}/{addresses.num_addresses} hosts are online. "

def main():

    while True:
        display_menu()
        selection = input("Please Select (1, 2, or E): ")
        if selection == '1':
            results = scan_ports_range()
            print(results)
            # TCP 
        elif selection == '2':
            results = ping_sweep()
            print(results)
            # ICMP
        elif selection.upper() == 'E':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter 1 for TCP, 2 for ICMP, or E to exit.")


if __name__ == "__main__":
    main()
  
    
    