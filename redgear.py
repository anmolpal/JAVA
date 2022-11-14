#! /usr/bin/python
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import simplejson as json
import smtplib

# JSON file
f = open ('/usr/local/info.json', "r")

# Reading from file
data = json.loads(f.read())

# Iterating through the json
# list
hostname = data['hostname']
username = data['user']
password = data['password']
MasterIP = data['masterIP']
SlaveIP  = data['slaveIP']
#print("Username:", username)
#print("HostName:", hostname)
#print("Password:", password)
#print("MasterIP:", MasterIP)
# Closing file
f.close()

# me == my email address
# you == recipient's email address
me = "anmol.pal@kockpit.in"
you = "anmol.pal@kockpit.in"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Server Details&Logs"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
html = """\
<html>
  <head></head>
  <body>
    <p>Here are Details <br>
    <p>Hostname:
       """ +str(hostname)+ """ <br>
    <p>Username:
       """ +str(username)+ """ <br>
    <p>MasterIP:
       """ +str(MasterIP)+ """ <br>
    <p>Password:
       """ +str(password)+ """ <br>
    <p>SlaveIP:
       """ +str(SlaveIP)+ """ <br>   
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
# Record the MIME types of both parts - text/plain and text/html.

part1 = MIMEText(html, 'html')
message = MIMEMultipart()
#attach_file_name = 'log_file.txt'
#pdf = MIMEApplication(open("log_file.txt", 'rb').read())
#pdf.add_header('Content-Disposition', 'attachment', filename= "log_file.txt")
#msg.attach(pdf)
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()
mail.login('alert@kockpit.in', 'alert@123')
mail.sendmail(me, you, msg.as_string())
mail.quit()
print(' ')
