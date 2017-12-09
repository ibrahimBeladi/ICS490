import json;
import sys;
import csv;
import pandas;
from pprint import pprint

def count_neg_rev(products):
    count = 0
    for (index,row) in products.iterrows():
        if row.loc['sentiment'] == -1:
            count = count + 1
    print 'Negative Reviews Count: {}'.format(count)

def count_pos_rev(products):
    count = 0
    for (index,row) in products.iterrows():
        if row.loc['sentiment'] == 1:
            count = count + 1
    print 'Positive Reviews Count: {}'.format(count)

def print_first_10(products):
    print 'First 10 Products:'
    for index in range(10):
        print 'Product #{}: {}'.format((index + 1),products.loc[index]['name'])
    
if __name__ == '__main__':
    dataset_file = 'amazon_baby_subset.csv'
    data_frame = pandas.read_csv(dataset_file)
    data_frame.get
    print_first_10(data_frame)
    count_pos_rev(data_frame)
    count_neg_rev(data_frame)
    important_words = 'important_words.json'
    imp_w = json.load(open(important_words))
