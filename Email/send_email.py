# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


# Create a text/plain message
msg = MIMEText('Hello Robert!') # this should actually have the content input from cards
me = 'monkey@test.com'
you = 'robertf224@gmail.com'

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Punch-Card Email!'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()