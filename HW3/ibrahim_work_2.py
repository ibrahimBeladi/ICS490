import json;
import sys;
import csv;
import pandas;
from pprint import pprint

def count_rev(products):
    countP = 0
    countN = 0
    for (index,row) in products.iterrows():
        if row.loc['sentiment'] == 1:
            countP += 1
        else:
            countN += 1
    print '\nPositive Reviews Count: {}\nNegative Reviews Count: {}'.format(countP,countN)

def print_first_10(products):
    print '\nFirst 10 Products:'
    for index in range(10):
        print 'Product #{}: {}'.format((index + 1),products.loc[index]['name'])

def print_first_unique_10(products):
    print '\nFirst 10 Products:'
    first_10 = []
    count = 0
    for (index,row) in products.iterrows():
        if count == 10:
            break
        if not row['name'] in first_10:
            first_10.append(row['name'])
            count += 1

    for index in range(10):
        print 'Product #{}: {}'.format((index + 1),first_10[index])
    
if __name__ == '__main__':
    dataset_file = 'amazon_baby_subset.csv'
    data_frame = pandas.read_csv(dataset_file)
    data_frame.get
    #print_first_10(data_frame)
    print_first_unique_10(data_frame)
    count_rev(data_frame)
    important_words_json = 'important_words.json'
    important_words = json.load(open(important_words_json))

