#encoding: utf-8
# Logistic Regression Classification

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
#from sklearn.linear_model import ElasticNet

filename = 'corpusCinemaMedian.csv'

dataframe = read_csv(filename, engine='python')
array = dataframe.values
X = array[:, 1:] # Features
Y = array[:, 0]# Binary output (Positive and negative classes)
num_folds = 10
kfold = KFold(n_splits = 700, random_state = 7)
model = LogisticRegression(C=0.9)
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv = kfold, scoring=scoring)
print(results.mean())

#Sandar's:
#Default = 0.730988322997
#With C=0.8 -> 0.731007169584
#With class_weight='balanced' -> 0.785009561386'
############################################################
#Cenima:
#With class_weight='balanced' -> 0.623118890096
#Default = 0.645274654742
#With C=1.1 -> 0.64527359675 / c=0.8 -> 0.645650594592 / c=0.9 -> 0.646213446374
#with n_splits = 20 / c = 0.9 -> 0.660425642759
#with n_splits = 20 / c = 0.9 -> 0.666050910938
#with n_splits = 700 -> 0.680025510204
