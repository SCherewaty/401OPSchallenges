#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 04/30/2024
#Purpose: Pinging Python


#Using the library datetime, print out current date and time
#import datetime

#Transmit a single ICMP (ping) packet to a specific IP every two seconds.
import ping 
import time 

#Target IP address
target_ip = "192.168.40.135"

while True:
    response = ping.ping(target_ip, timeout=1)
    

#Evaluate the response as either success or failure.
if response.alive:
    print(f"Ping to {target_ip} successful. (RTT: {response.rtt}ms)")
else:
    print(f"Ping to {target_ip} failed.")
    
#Assign success or failure to a status variable.


#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.

#from datetime import date 

