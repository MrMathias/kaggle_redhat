from csv_to_libsvm import convert
import pandas as pd
from pandas import Series

def bag_of_words(train_csv,test_csv):
    # df_train = pd.read_csv(train_csv, dtype={'': object})
    # df_train = df_train.drop(['outcome','date_activity', 'date_people','activity_id'], 1)
    #
    # df_test = pd.read_csv(test_csv, dtype={'': object})
    # df_test = df_test.drop(['date_activity', 'date_people','activity_id'], 1)

    # combine test/train: gather all words
    #df = df_train.append(df_test, ignore_index=True)
    #df.to_csv("small_combined_test_train.csv", index=False)

    df = pd.read_csv("combined_test_train.csv")
    print("frames combined")

    # find uniques
    word_index = {}
    word_set = set()
    count = 1
    for column in df:
        words = list(Series(df[column].values.ravel()).unique()) # unique values in column
        for word in words:
            if word != "nan":
                word_index[str(column)+str(word)] = count
                count += 1
    print("words:",len(word_index))
    return word_index

word_index = bag_of_words("combined_train.csv", "combined_test.csv")

#Convert training data
print("converting training")
convert("combined_train.csv",word_index,train=True,output="combined2_train.vw")

#Convert test data
print("converting test")
convert("combined_test.csv",word_index,train=False,output="combined2_test.vw")