import json;
import sys;
import csv;
import pandas;
from pprint import pprint

def count_neg_rev(products):
    print 'Counting Negative Reviews...'
    count = 0
    for (index,row) in products.iterrows():
        if row.loc['sentiment'] == -1:
            count = count + 1
    print 'Negative Reviews Count: {}'.format(count)

def count_pos_rev(products):
    print 'Counting Positive Reviews...'
    count = 0
    for (index,row) in products.iterrows():
        if row.loc['sentiment'] == 1:
            count = count + 1
    print 'Positive Reviews Count: {}'.format(count)

def remove_punctuation(text):
    import string
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
    print 'First 10 Products:'
    for index in range(10):
        print 'Product #{}: {}'.format((index + 1),products.loc[index]['name'])

def count_important_words(imp_words,products):
    print 'Counting important words...'
    for word in imp_words:
        for (index,row) in products.iterrows():
            row.loc[word] = products['review_clean'].split().count(word)
    return products
if __name__ == '__main__':
    dataset_file = 'amazon_baby_subset.csv'
    
    #read dataset
    data_frame = pandas.read_csv(dataset_file)
    
    print_first_10(data_frame)
    count_pos_rev(data_frame)
    count_neg_rev(data_frame)
    
    data_frame = apply_transformations(data_frame)
    
    #load important words
    important_words = 'important_words.json'
    imp_w = json.load(open(important_words))
    
    data_frame = count_important_words(imp_w,data_frame)









    
