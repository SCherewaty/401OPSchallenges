#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/03/2024
#Purpose: Logging
#Sources: 

#Import Libraries
import logging
import os

#Configure the logger
logging.basicConfig(filename="demo.log", format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

#Create a log object
test_log = logging.getLogger("my_logger")




