#encoding: utf-8
# Logistic Regression Classification

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

filename = 'corpusCinemaMedian.csv'

dataframe = read_csv(filename, engine='python')
array = dataframe.values
X = array[:, 1:] # Features
Y = array[:, 0]# Binary output (Positive and negative classes)
clf = RandomForestClassifier(random_state=0)
clf.fit(X,Y)
print(clf.score(X,Y))

'''
Project:
Default = 0.807995495495
'''
