#encoding: utf-8
import csv, getpass, json, os, time, urllib
from tweepy import Cursor
#from twitter_client import get_twitter_client
from twitter_client import get_twitter_client


if __name__ == '__main__':

    fname = "ids.jsonl"
    client = get_twitter_client()
    with open(fname, 'r') as f:
        for line in f:
            id_1 = json.loads(line)
            outName = "{}.json".format(id_1)
            status = client.get_status(id_1)
            with open("rawdata"+"/"+outName, 'w') as f:
                f.write(json.dumps(status._json))

