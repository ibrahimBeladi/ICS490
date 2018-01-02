# twitter_client.py
import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """Setup Twitter authentication.

    Return: tweepy.OAuthHandler object
    
    try:
        consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_secret = os.environ['TWITTER_ACCESS_SECRET']
        print consumer_key
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    """

# IMPORTANT NOTE: Make sure to use your own Twitter App Credentials
    consumer_key = '7RVcavx0VJkB5gIknVQgU8dp2' #os.environ["TWITTER_CONSUMER_KEY"]
    consumer_secret = 'DNBIPPz8eOuFfmhIw99tNbWjQScuJIVwZQoh1CzhozwexdaoWW' # os.environ['TWITTER_CONSUMER_SECRET']
    access_token = '922919621493174273-syUxRdt1Y19qr9w0DOBuU3f5yyJIJrV' # os.environ['TWITTER_ACCESS_TOKEN']
    access_secret = 'fLhehwLyKZr86YE5gxQBQbCCca9AEqXjjkeSGZvtJU0op' # os.environ['TWITTER_ACCESS_SECRET']

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.

    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client
