#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 04/30/2024
#Purpose: Pinging Python


#import ping  (struggled with this)
import ping3

import os
import time

def ping_ip(ip):
# Needed help with line 16 and used Ethan's review code
  response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1") 
  if response == 0:
    return "Succeeded"
  else:
    return "Failed"
  
def main():
    ip = "192.168.40.135"
    while True:
      status = ping_ip(ip)
# Also needed help with line 27-29 and used Ethan's review code
      timestamp = time.strftime("%Y-%m-%d %H:%M:%S:%f")
      print(f"{timestamp} Network {status} to {ip}")
      time.sleep(2)
      
if __name__ == "__main__":
    main()
    
      
      
      
      #First pass attempt

# Define target IP address
# target_ip = "192.168.40.135"

# # Send pings to IP every 2 seconds
# for i in range(5):
#   response = ping3.ping(target_ip)
#   if response:
#     print("Ping successful! " + str(response))
#   else:
#     print("Ping failed.")
    
    
#     time.sleep(2)
    




