#Sending an email through gmail using Python
import smtplib
# fromaddr should be your gmail account, toaddrs can be anything
fromaddr = 'jack@example.com'
toaddrs = 'jill@example.com'
msg = 'Hello Jill!'

#provide gmail user name and password
username = 'your-email'
password = 'your-password'

# functions to send an email
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()