#encoding: utf-8
# Logistic Regression Classification

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import ElasticNet
from sklearn import svm

filename = 'all-words-no-review2.csv'

dataframe = read_csv(filename, engine='python')
array = dataframe.values
X = array[:, 1:] # Features
Y = array[:, 0]# Binary output (Positive and negative classes)
clf = svm.SVC(C=1.0, cache_size=200, class_weight='balanced', coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
clf.fit(X,Y)
print(clf.score(X,Y))

# Results (700 Splits / scoring : neg_mean_squared_error) = -0.369634291175
# Results (10 Splits / scoring : neg_mean_squared_error) = -0.385998731563

'''
Sandar's:
Class weight = 'balanced' -> 0.808675007537
'''
