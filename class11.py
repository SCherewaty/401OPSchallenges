#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/13/2024
#Purpose: SCAPY practice
#Sources: https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/
#         https://stackoverflow.com/questions/62848017/using-python-cryptography-module-to-encrypt-recursively


#Import scapy

import scapy.all as scapy

packets = scapy.sniff(count=10)

print(packets.summary())
