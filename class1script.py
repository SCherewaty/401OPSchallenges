#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 04/29/2024
#Purpose: Powershell script for Automatic Updates

#Attempted registry modification for automatic updates
REG write-value "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\AutomaticUpdates" -Name "Updates" -DataType DWORD -Data 4
