#encoding: utf-8
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream 
import json, sys, os, errno, codecs
###########################################################################################
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
###########################################################################################
def write(path, tweet):
	file = open(path,"w") 
	file.write(tweet.encode('utf-8')) 
	file.close()
###########################################################################################

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1269774780-S0BIdXogvM5ZqSJCAID2xRO9b8bXxIZH9g09io7' 
ACCESS_SECRET = 'sU1NLe5ew0PJ7BiB3dAXrkv4j72eL5vg1UPIHKaF02WFX' 
CONSUMER_KEY = 'IKcOaqTowQAiQM90M74SeyPJW' 
CONSUMER_SECRET = 'XwgpChlY3ol7aBuDLMD7a0V9aHbD78dYSr6n4DLoQ9LyvUrXzt' 
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET) 

# Initiate the connection to Twitter Streaming API 
twitter_stream = TwitterStream(auth=oauth) 
# Get a sample of the public data following through Twitter 
iterator = twitter_stream.statuses.filter(track="#السينما_في_السعودية", language="ar",tweet_mode='extended')

for tweet in iterator: 
    try:
        write("ids/"+tweet[u'id_str'],"")
    except Exception as e: 
        print e
        pass

