#************************File #2**************************#
#     This file is used to find the number of reviews     #
#     containing a specific word. It reads the file       #
#     "all-words.csv" and count the number of one's in    #
#     The column contains_{word}.                         #
#                                                         #
#*********************************************************#


import pandas

def count_word(word):
    print 'Reading Dataset...'
    file_name = 'word-count/all-words.csv'
    try:
        data_frame = pandas.read_csv(file_name)
        is_contain_col = data_frame['contains_'+word]
        count = 0
        print 'Counting the occurrence of the word "{}"...'.format(word)
        for x in is_contain_col:
            if x == 1:
                count += 1
        print 'The word "{}" has appeared in {} reviews.'.format(word,count)
    except Exception:
        print 'Unable to open CSV file. Check that the file "{}" is exist.'.format(file_name)
if __name__ == '__main__':
    count_word('perfect')
