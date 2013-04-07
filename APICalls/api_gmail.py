#Sending an email through gmail using Python
import smtplib
# fromaddr should be your gmail account, toaddrs can be anything
fromaddr = ''
toaddrs = ''
msg = 'Hello Robert!'

#provide gmail user name and password
username = ''
password = ''

# functions to send an email
server = None

def setup_gmail():
	global server
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(username, password)

def send_email(message):
	global server
	server.sendmail(fromaddr, toaddrs, message)

def end_gmail():
	global server
	server.quit()