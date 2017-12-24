import pandas;
import json;
import pprint;
from sklearn.model_selection import KFold;
from sklearn.model_selection import cross_val_score;
from sklearn.linear_model import LogisticRegression;

def to_multidim_array(dataframe,features,label):
    print 'Inserting column of one\'s to dataframe...'
    dataframe.insert(0,'constant',1)
    print 'Inserting new feature...'
    features.insert(0,'constant')
    featurse_matrix = extract_featurs_matrix(features, dataframe)
    label_matrix = extract_label_matrix(label,dataframe)
    return (featurse_matrix, label_matrix)

def extract_label_matrix(label,dataframe):
    print 'Extracting Label matrix...'
    try:
        label_frame = dataframe[label]
        print 'Done!'
        return label_frame.as_matrix()
    except Exception:
        print 'Label "{}" does not exist in the dataframe!'.format(label)
    return None

def extract_featurs_matrix(features,dataframe):
    print 'Extracting features matrix...'
    tmp_df = pandas.DataFrame()
    for x in features:
        try:
            tmp_df[x] = dataframe[x]
        except Exception:
            print 'Feature "{}" does not exist in the dataframe!'.format(x)
    f_mtrx = tmp_df.as_matrix()
    print 'Done!'
    return f_mtrx
def get_important_words(file_name='important_words.json'):
    print 'Reading Important Words...'
    try:
        imp_w = json.load(open(file_name))
        print 'Done!'
    except Exception:
        print 'Unable Read "{}". Check that it is exist and well formatted.'.format(file_name)
    return imp_w

def apply_logistic_reg(features,word_count):
    print 'Applaying Logistic Reg...'
    X = features[:, 0:word_count] # Features
    Y = features[:, word_count] # Binary output (Positive and negative classes)
    kfold = KFold(n_splits = 10, random_state = 7)
    model = LogisticRegression()
    results = cross_val_score(model, X, Y, cv = kfold)
    print('Est. Mean: {}'.format(results.mean()))

    

if __name__ == '__main__':
    data_file = 'word-count/all-words-no-review.csv'
    print 'Reding Data form "{}"...'.format(data_file)
    df = None
    try:
        df = pandas.read_csv(data_file)
        print 'Done!'
    except Exception:
        print 'Unable to read the file. Check that it exist.'.format(data_file)
        sys.exit(-1)
    label = 'sentiment'
    features = get_important_words()
    ret_val = to_multidim_array(df,features,label)
    print 'Number of features in the feature_matrix: {}'.format(len(ret_val[0]))
#193 = count of important words
    apply_logistic_reg(ret_val[0],193)
