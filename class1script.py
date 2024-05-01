#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 04/29/2024
#Purpose: Powershell script for Automatic Updates

REG write-value "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\AutomaticUpdates" -Name "Updates" -DataType DWORD -Data 4
