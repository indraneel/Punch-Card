from twitter import *
import os.path

# The Twitter object
twitter_obj = None

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

	twitter_obj =  Twitter(auth=OAuth(
						oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

# Post a tweet to a given Twitter object
def post_tweet(message):
	twitter_obj.statuses.update(status=message)
