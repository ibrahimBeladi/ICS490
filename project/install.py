#
# Sanders-Twitter Sentiment Corpus Install Script
# Version 0.1
#
# Pulls tweet data from Twitter because ToS prevents distributing it directly.
#
# Right now we use unauthenticated requests, which are rate-limited to 150/hr.
# We use 125/hr to stay safe.  
#
# We could more than double the download speed by using authentication with
# OAuth logins.  But for now, this is too much of a PITA to implement.  Just let
# the script run over a weekend and you'll have all the data.
#
#   - Niek Sanders
#     njs@sananalytics.com
#     October 20, 2011
#
#
# Excuse the ugly code.  I threw this together as quickly as possible and I
# don't normally code in Python.
#
import csv, getpass, json, os, time, urllib, sys
from tweepy import Cursor
#from twitter_client import get_twitter_client
from tweepy import API
from tweepy import OAuthHandler


def get_user_params():

    user_params = {}

    # get user input params
    user_params['inList']  = raw_input( '\nInput file [./corpus.csv]: ' )
    user_params['outList'] = raw_input( 'Results file [./full-corpus.csv]: ' )
    user_params['rawDir']  = raw_input( 'Raw data dir [./rawdata/]: ' )
    
    # apply defaults
    if user_params['inList']  == '': 
        user_params['inList'] = './corpus.csv'
    if user_params['outList'] == '': 
        user_params['outList'] = './full-corpus.csv'
    if user_params['rawDir']  == '': 
        user_params['rawDir'] = './rawdata/'

    return user_params


def dump_user_params( user_params ):

    # dump user params for confirmation
    print 'Input:    '   + user_params['inList']
    print 'Output:   '   + user_params['outList']
    print 'Raw data: '   + user_params['rawDir']
    return


def read_total_list( in_filename ):

    # read total fetch list csv
    fp = open( in_filename, 'rb' )
    reader = csv.reader( fp, delimiter=',', quotechar='"' )

    total_list = []
    for row in reader:
        total_list.append( row )

    return total_list


def purge_already_fetched( fetch_list, raw_dir ):

    # list of tweet ids that still need downloading
    rem_list = []

    # check each tweet to see if we have it
    for item in fetch_list:

        # check if json file exists
        tweet_file = raw_dir + item[2] + '.json'
        if os.path.exists( tweet_file ):

            # attempt to parse json file
            try:
                parse_tweet_json( tweet_file )
                print '--> already downloaded #' + item[2]
            except RuntimeError:
                rem_list.append( item )
        else:
            rem_list.append( item )

    return rem_list


def get_time_left_str( cur_idx, fetch_list, download_pause ):

    tweets_left = len(fetch_list) - cur_idx
    total_seconds = tweets_left * download_pause

    str_hr = int( total_seconds / 3600 )
    str_min = int((total_seconds - str_hr*3600) / 60)
    str_sec = total_seconds - str_hr*3600 - str_min*60

    return '%dh %dm %ds' % (str_hr, str_min, str_sec)


def download_tweets( fetch_list, raw_dir ):

    # ensure raw data directory exists
    if not os.path.exists( raw_dir ):
        os.mkdir( raw_dir )

    # stay within rate limits
    max_tweets_per_hr  = 125
    download_pause_sec = 3600 / max_tweets_per_hr
    client = get_twitter_client()

    # download tweets
    for idx in range(0,len(fetch_list)):

        # current item
        item = fetch_list[idx]

        # print status
        trem = get_time_left_str( idx, fetch_list, download_pause_sec )
        print '--> downloading tweet #%s (%d of %d) (%s left)' % \
              (item[2], idx+1, len(fetch_list), trem)

        # pull data
        fname = "{}.json".format(item[2])
        #api = tweepy.API(auth)
        try:
            status = client.get_status(item[2])
        
            with open(raw_dir+"/"+fname, 'w') as f:
                f.write(json.dumps(status._json))
            
        #url = 'http://api.twitter.com/1/statuses/show.json?id=' + item[2]
        #urllib.urlretrieve( url, raw_dir + item[2] + '.json' )

        # stay in Twitter API rate limits 
            print '    pausing %d sec to obey Twitter API rate limits' % \
                  (download_pause_sec)
            time.sleep( download_pause_sec)
        except:
            print "Error",sys.exc_info()[0]
    return


def parse_tweet_json( filename ):
    
    # read tweet
    fp = open( filename, 'rb' )

    # parse json
    try:
        tweet_json = json.load( fp )
    except ValueError:
        raise RuntimeError('error parsing json')

    # look for twitter api error msgs
    if 'error' in tweet_json:
        raise RuntimeError('error in downloaded tweet')

    # extract creation date and tweet text
    return [ tweet_json['created_at'], tweet_json['text'] ]


def build_output_corpus( out_filename, raw_dir, total_list ):

    # open csv output file
    fp = open( out_filename, 'wb' )
    writer = csv.writer( fp, delimiter=',', quotechar='"', escapechar='\\',
                         quoting=csv.QUOTE_ALL )

    # write header row
    writer.writerow( ['Topic','Sentiment','TweetId','TweetDate','TweetText'] )

    # parse all downloaded tweets
    missing_count = 0
    for item in total_list:

        # ensure tweet exists
        if os.path.exists( raw_dir + item[2] + '.json' ):

            try: 
                # parse tweet
                parsed_tweet = parse_tweet_json( raw_dir + item[2] + '.json' )
                full_row = item + parsed_tweet
    
                # character encoding for output
                for i in range(0,len(full_row)):
                    full_row[i] = full_row[i].encode("utf-8")
    
                # write csv row
                writer.writerow( full_row )

            except RuntimeError:
                print '--> bad data in tweet #' + item[2]
                missing_count += 1

            except:
                print "Some error about ",sys.exc_info()[0]
        else:
            print '--> missing tweet #' + item[2]
            missing_count += 1

    # indicate success
    if missing_count == 0:
        print '\nSuccessfully downloaded corpus!'
        print 'Output in: ' + out_filename + '\n'
    else: 
        print '\nMissing %d of %d tweets!' % (missing_count, len(total_list))
        print 'Partial output in: ' + out_filename + '\n'

    return

def get_twitter_auth():

    try:
        consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_secret = os.environ['TWITTER_ACCESS_SECRET']
        print "used env vars:",consumer_key
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")

        consumer_key = '7RVcavx0VJkB5gIknVQgU8dp2'
        consumer_secret = 'DNBIPPz8eOuFfmhIw99tNbWjQScuJIVwZQoh1CzhozwexdaoWW'
        access_token = '922919621493174273-syUxRdt1Y19qr9w0DOBuU3f5yyJIJrV'
        access_secret = 'fLhehwLyKZr86YE5gxQBQbCCca9AEqXjjkeSGZvtJU0op'

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

def main():

    #client = get_twitter_client()
    
    # get user parameters
    user_params = get_user_params()
    dump_user_params( user_params )

    # get fetch list
    total_list = read_total_list( user_params['inList'] )
    fetch_list = purge_already_fetched( total_list, user_params['rawDir'] )

    # start fetching data from twitter
    download_tweets( fetch_list, user_params['rawDir'] )

    # second pass for any failed downloads
    print '\nStarting second pass to retry any failed downloads';
    fetch_list = purge_already_fetched( total_list, user_params['rawDir'] )
    download_tweets( fetch_list, user_params['rawDir'] )

    # build output corpus
    build_output_corpus( user_params['outList'], user_params['rawDir'], 
                         total_list )

    return


if __name__ == '__main__':
    main()
