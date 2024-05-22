#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/22/2024
#Purpose: Brute Force III
#Sources: https://docs.python.org/3/library/zipfile.html


from zipfile import ZipFile

zip_file = ### Your password protected zip file ###
password = ### Password to guess ###

with ZipFile(zip_file) as zf:
  zf.extractall(pwd=bytes(password,'utf-8'))
