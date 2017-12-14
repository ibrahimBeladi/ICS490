#!/bin/bash
directory=$1

csv=`basename $directory`".csv"
# Clears the csv file
echo 'id,status'> $csv

for i in `dir $directory` ; do
    # list the tweets in the csv
    (echo -n $i, && cat $directory/$i | tr '\n' ' '&& echo) >> $csv
done
