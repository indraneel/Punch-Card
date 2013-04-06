# MAKE SURE TWILIO LIBRARY IS INSTALLED!  pip install twilio


# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "ACd2a61e174d00842835bef8b531481fae"
auth_token = "8b6089970e77555da09217697ba9e606"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(to="+19734876086", from_="+18623978705",
                                     body="Hello Robert!")