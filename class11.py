#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/13/2024
#Purpose: SCAPY practice
#Sources: 
#      

#Import scapy
#import scapy.all as scapy 

# User input for specified range
target_IP = input("What is the target IP address? ")
start_port = int(input("What's the start of the port range? "))
end_port = int(input("What's the end of the range? "))

# Create ethernet frame that's empty and add an IP layer
my_frame = scapy.Ether() / scapy.ARP()

# Create the function
def scan_port(target_IP, port):
    



# Loop for port scanning
for port in range(start_port, end_port + 1):
    scan_port(target_IP, port)