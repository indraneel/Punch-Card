from twitter import *
import os.path
import foursquare
import logging
import webbrowser

# Set up basic logging
logging.basicConfig()

# Set up a user's twitter account
# Return a Twitter object that can be used
# to manipulate the user's Twitter account
def setup_twitter():

	CONSUMER_KEY = 'UFUkG1tnPBu1TP7cTw112g'
	CONSUMER_SECRET = 'qUb7c79m5fGBHgHdXggIBXVXM4dUuDXVgcQKHohO0'

	MY_TWITTER_CREDS = os.path.expanduser('~/.punch_card_credentials')
	if not os.path.exists(MY_TWITTER_CREDS):
		oauth_dance("Punch Card Twitter", CONSUMER_KEY, CONSUMER_SECRET,
					MY_TWITTER_CREDS)

	oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

	return Twitter(auth=OAuth(
		oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

# Post a tweet to a given Twitter object
def post_tweet(message, twobj):
	twitter.statuses.update(status=message)
	
# Set up a user's foursquare account
def setup_foursquare():

	CLIENT_ID = 'THKVRHYGPBPZOG4HWNKT0PX3IO5KOAQ3UP22XJ0JVKLMU43I'
	CLIENT_SECRET = 'KUNKD0YSJU0S2GLHAZOG0EC25W5NJDDVLU45IUSM5LPF3E5P'
	
	# Construct the client object
	client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://www.mattmik.com/')

	# Build the authorization url for your app
	# auth_uri = client.oauth.auth_url()
	# webbrowser.open_new(auth_uri)

	USER_CODE = 'HXULWT2YKSUZI5B1RAZ0P0HXCQ1RYTKM4I0TTWBI1F512M10'
	
	# Interrogate foursquare's servers to get the user's access_token
	access_token = client.oauth.get_token(USER_CODE)

	# Apply the returned access token to the client
	client.set_access_token(access_token)

	# Get the user's data
	print client.users()

# twitter = setup_twitter()
# post_tweet("Hello, again", twitter)
setup_foursquare()
