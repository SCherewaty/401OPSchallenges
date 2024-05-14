#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/13/2024
#Purpose: SCAPY practice
#Sources: https://scapy.readthedocs.io/en/latest/usage.html#icmp-ping
#  https://stackoverflow.com/questions/61180264/find-webserver-listening-on-port-with-scapy-port-scanner
#  Also Gilbert Collado and Omar Ardid helped me with this during class.   

from scapy.all import IP, TCP, sr1, send
import logging  

# Disable Scapy's verbose logging output
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

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
    ports_to_scan = range(22, 25)  

    scan_ports_range(target_host, ports_to_scan)  


        
        
 