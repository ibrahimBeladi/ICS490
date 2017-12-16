#!/bin/bash

directory=$1

csv=`basename $directory`".csv"
exportedList=exportedList

echo 'id,status' > $csv

for tweetID in `dir $directory` ; do
    if [ -s $directory/$tweetID ] # if not empty
    then
        if !(grep -q "$tweetID" $exportedList) # if not exported
        then
            if !(cat $directory/$tweetID  | grep -q "RT @") # if not retweeted
            then
                (echo -n $tweetID, && cat $directory/$tweetID | tr '\n' ' '&& echo) >> $csv
            fi
        fi
    fi
done
