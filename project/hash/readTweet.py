#encoding: utf-8
import csv, getpass, json, os, time, urllib, errno, os.path, sys
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
def write(path, msg):
    with open(path, 'w') as f:
        f.write(msg.encode('utf-8'))
###########################################################################################
if __name__ == '__main__':

    destination = "rawdata"
    # ls ids | sed 's|[^0-9]||g' > list ; cat list | wc -l
    fname = "list"

    mkdir_p(destination)
    client = get_twitter_client()

    with open(fname, 'r') as f:
        for line in f:
            id_1 = json.loads(line)
            outName = "{}".format(id_1)
            if not os.path.exists(destination+"/"+outName):
                try:
                    status = client.get_status(id_1,tweet_mode='extended')
                    write(destination+"/"+outName, status.full_text)
                except Exception as e: 
                    if e[0][0]['code'] == 144:
                        print outName + " is deleted"
                        write(destination+"/"+outName, "")
                    elif e[0][0]['code'] == 179:
                        print outName + " is private"
                        write(destination+"/"+outName, "")
                    elif e[0][0]['code'] == 63:
                        print outName + " user's is suspended"
                        write(destination+"/"+outName, "")
                    elif e[0][0]['code'] == 34:
                        print outName + " that page does not exist."
                        write(destination+"/"+outName, "")
                    elif e[0][0]['code'] == 88:
                        sys.exit("Rate limit exceeded, before reaching: " + outName)
                    else:
                        print e
                        print "for " + outName
                        sys.exit("New Error")

