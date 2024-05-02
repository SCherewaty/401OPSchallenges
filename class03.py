#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/01/2024
#Purpose: Class 3 send email script

#FULL DISCLOSURE - my original script was cobbled from Ethan's code and I pieced it toether during class

#import the SMTP library
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import os

#Send email function?
def send_email(user_email, to_email, password, host, subject, message):
    
    msg = MIMEMultipart()
    msg[ 'From' ] = user_email
    msg[ 'To' ] = to_email
    msg[ 'Subject' ] = subject
    body = MIMEText(message, 'plain')
    msg.attach(body)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user_email, password)
    text = msg.as_string()
    server.sendmail(user_email, to_email, text)
    server.quit()
    
    print("email sent!")
    
  #Main
def main()
    previous_status = "down"
    current_status = "up"
    
    while True:
        current_status = check_host(host)
        print(current_status)
        if current_status != previous_status
            subject = f"status change alert for {host}"
            message = f"Host{host} status changed from {previous_status} to (current_status) on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
            send_email(user_email, to_email, password, host, subject, message)
        else:
            pass
        previous_status = current_status
        time.sleep(2)
        
if __name__ == "__main__":
    main()
        
        
#end
    
   
    




    




