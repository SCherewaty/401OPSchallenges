#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/13/2024
#Purpose: SCAPY practice
#Sources: 
#      


#Import scapy
import scapy.all as scapy 

# Create ethernet frame that's empty and add an IP layer
my_frame = scapy.Ether() / scapy.ARP()

print(my_frame)
print('-' * 80)
#print(my_frame.show())
#print('-' * 80)

# Use sniff function in scapy to capture 10 packets of data
packets = scapy.sniff(count=10)

# Let's see them
print(packets.summary())

# Create for loop to scan ports
#for my_frame 