#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/01/2024
#Purpose: 

#import the SMTP library
import smtplib

#Define Variables
server_info = smtplib.SMTP_SSL("smtp.gmail.com", 465)
from_address = "steve.opswork29@gmail.com"
to_address = "scherewaty@gmail.com"
from_username = "steve.opwork29"
from_password = os.environ.get("EMAIL_PASSWORD")
message = "Hi, I'm definitely NOT a Telemarketer..."

#Function
def send_email(
    server, 
    from_addr, 
    to_addr, 
    from_user,
    from_pswd,
    msg
):
    
    server.login(from_user, from_pswd)
    server.sendmail(from_addr, to_addr, msg)
    server.quit()



    




