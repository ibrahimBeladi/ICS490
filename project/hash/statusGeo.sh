#!/bin/bash
echo There are $(find ./geo/* -not -empty -ls | wc -l) geo-located out of $(ls ./geo/* | wc -l)

