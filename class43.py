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
    try:
        sockmod.connect((hostip, portno))
        print("Port open")
    except socket.timeout:
        print("Connection timed out")
    except socket.error:
        print("Port closed")
    finally:
        sockmod.close()

portScanner(portno)

# End
