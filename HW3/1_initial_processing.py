#*****************************File #1********************************#
#                                                                    #
#    This file is used to perform the following:                     #
#        - Read Dataset and load it into Pandas DataFrame.           #
#        - Read the important words.                                 #
#        - Count positive and negative reviews.                      #
#        - Print first 10 products.                                  #
#        - Apply transformations to reviews (Remiving N/A's and      #
#          punctuations).                                            #
#        - Counting the occurance of important words in reviews.     #
#                                                                    #
#    The final output of running this file is a set of .csv files.   #
#    Each file will contain 10 words out of the 193 words. Each word #
#    will have two columns, one column that indecates if the word    #
#    has appeared in the review (1 or 0) and the second column will  #
#    contain the number of times word has appeared in the review.    #
#                                                                    #
#    After this step, the content of each file should be copyed and  #
#    stored in one single .csv file to run next .py file.            #
#                                                                    #
#********************************************************************#
import json;
import gc;
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
    itr_count = 0;
    start_word_num = 0
    end_word_num = 9;
    for word in imp_words:
        #if itr_count == 10, free memory and load data again.
        #simply, every 10 words, free memory.
        if itr_count == 10:
            print 'Clearing Memory...'
            del products
            start_word_num = end_word_num + 1
            end_word_num = end_word_num + itr_count;
            itr_count = 0;
            gc.collect()
            products = get_products_dataframe()
        print 'Counting the word "{}"...'.format(word)
        col = []
        countList = []
        for (index,row) in products.iterrows():
            count = row['review_clean'].split().count(word)
            col.append(count)
            if count >= 1:
                countList.append(1)
            else:
                countList.append(0)
        products[word] = col
        products['contains_'+word] = countList
        itr_count = itr_count + 1
        try:
            products.to_csv('word-count/{}-{}.csv'.format(start_word_num,end_word_num))
        except Exception:
            print 'Unable to save CSV.'
    return products
def get_products_dataframe(file_name='amazon_baby_subset.csv'):
    print 'Reading Dataset...'
    try:
        data_frame = pandas.read_csv(file_name)
        data_frame = apply_transformations(data_frame)
    except Exception:
        print 'Unable Read "{}". Check that it is exist and well formatted.'.format(file_name)
    return data_frame

def get_important_words(file_name='important_words.json'):
    print 'Reading Important Words...'
    try:
        imp_w = json.load(open(file_name))
    except Exception:
        print 'Unable Read "{}". Check that it is exist and well formatted.'.format(file_name)
    return imp_w

if __name__ == '__main__':
    data_frame = get_products_dataframe()
    print_first_10(data_frame)
    count_rev(data_frame)
    important_words = get_important_words()
    data_frame = count_important_words(important_words,data_frame)

  
