#!/bin/bash

ids=$(eval 'ls ids | wc -l')
tweets=$(eval 'ls rawdata | wc -l')
empty=$(eval 'find rawdata -type f -size 0 | wc -l')
usable=$(eval 'grep -L "RT @" rawdata/* | wc -l')

echo $ids ids
echo $tweets downloaded tweets
echo $empty empty tweets
echo $(($usable-$empty)) usable tweets
