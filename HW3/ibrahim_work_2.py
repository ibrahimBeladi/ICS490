import json;
import sys;
import csv;
import pandas;
import string;
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

def remove_punctuation(text):
    return text.translate(None, string.punctuation)

def apply_transformations(products):
    #transformation #1. remove n/a's
    print 'Applying Data Transformations...'
    products = products.fillna({'review':''})
    review_clean = []
    for (index,row) in products.iterrows():
        review_clean.append(remove_punctuation(row.loc['review']))
    products['review_clean'] = review_clean
    return products

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

def count_important_words(imp_words,products):
    print 'Counting important words...'
    for word in imp_words:
        for (index,row) in products.iterrows():
            row.loc[word] = row['review_clean'].split().count(word)
    return products

if __name__ == '__main__':
    dataset_file = 'amazon_baby_subset.csv'
    
    #read dataset
    data_frame = pandas.read_csv(dataset_file)
    
    print_first_unique_10(data_frame)
    count_rev(data_frame)
    
    data_frame = apply_transformations(data_frame)
    
    #load important words
    important_words_json = 'important_words.json'
    important_words = json.load(open(important_words_json))
    
    data_frame = count_important_words(important_words,data_frame)

