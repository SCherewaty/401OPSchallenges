#!/usr/bin/env python3

#Author: Steve Cherewaty
#Date: 06/26/2024
#Purpose: Attack Tools Pt 3
#Sources: Demo Code + https://pypi.org/project/python-nmap/
# Conferred with ChatGPT for this assignment

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5
sockmod.settimeout(timeout)

hostip = input("Enter the host IP address here: ")
portno = int(input("Enter the port number:"))

def portScanner(portno):
    if sockmod.FUNCTION((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port closed")
    else:
        print("Port open")

portScanner(port)

