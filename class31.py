#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/10/2024
#Purpose: Signature based malware PART 1
#Sources: 
# Worked with Brad Baack on this Ops Challenge

import time  # Import time module for delays
import getpass  # Import getpass module to securely get user passwords
import os  # Import os module for file system operations
import paramiko  # Import paramiko for SSH connections
import zipfile  # Import zipfile for handling zip files
import logging  # Import logging module
from logging.handlers import RotatingFileHandler  # Import RotatingFileHandler for log rotation

# [MOD] Configure logging with rotation, file, and stream handlers
def setup_logger(log_file):
    logger = logging.getLogger("BruteForceLog")
    logger.setLevel(logging.DEBUG)
    
    # [MOD] Add a rotating handler
    rotating_handler = RotatingFileHandler(log_file, maxBytes=2000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rotating_handler.setFormatter(formatter)
    
    # [MOD] Add a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    # [MOD] Add a stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    


