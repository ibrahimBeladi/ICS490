import pandas;
import json;
import pprint;

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
        
