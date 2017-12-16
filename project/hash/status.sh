#!/bin/bash

tweets=$(eval 'ls rawdata | wc -l')
empty=$(eval 'find rawdata -type f -size 0 | wc -l')
retweets=$(eval 'cat rawdata/* | grep "RT @" | wc -l')
truncated=$(eval 'cat rawdata/* | grep "…"  | wc -l')
trunRet=$(eval 'cat rawdata/* | grep "…"  | grep "RT @" | wc -l')
echo $tweets downloaded tweets
echo $empty empty tweets
echo -------------------
echo $(($tweets-$empty)) all non-empty tweets
echo $(($tweets-$empty-$retweets)) tweets
echo $retweets retweets
echo $truncated truncated
echo $trunRet truncated retweets
echo $(($truncated-$trunRet)) truncated tweets
