#encoding: utf-8
import csv, getpass, json, os, time, urllib, errno
from tweepy import Cursor
from twitter_client import get_twitter_client
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
if __name__ == '__main__':

    mkdir_p("rawdata")
    fname = "not_exported"
    client = get_twitter_client()
    with open(fname, 'r') as f:
        for line in f:
            id_1 = json.loads(line)
            outName = "{}".format(id_1)
            try:
                status = client.get_status(id_1,tweet_mode='extended')
                with open("rawdata"+"/"+outName, 'w') as f:
                    f.write(status.full_text.encode('utf-8'))
            except:
                print "Error at "+line

