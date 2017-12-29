#encoding: utf-8
# Multinomial naiive bayes

from pandas import read_csv
import numpy as np
from sklearn.naive_bayes import MultinomialNB

filename = 'all-words-no-review2.csv'

dataframe = read_csv(filename, engine='python')
array = dataframe.values
X = array[:, 1:]
Y = array[:, 0]
clf = MultinomialNB()
clf.fit(X,Y)
print(clf.score(X,Y))

'''
Project:
Default = 0.668168168168

Sandar's (After replacing -1 with 0)

'''
