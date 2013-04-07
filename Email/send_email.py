#Sending an email through gmail using Python - Raghuram Reddy
import smtplib
fromaddr = 'robertf224@gmail.com'
toaddrs = 'robertf224@gmail.com'
msg = 'Hello Robert!'

#provide gmail user name and password
username = ''
password = ''

# functions to send an email
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()