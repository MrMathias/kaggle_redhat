
"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.
"""

import csv
import pandas
from pandas import Series
import numpy as np
import sys
from datetime import datetime
from sklearn.feature_extraction.text import CountVectorizer

def float_convertable(s):
    try:
        s=float(s)
    except ValueError:
        pass
    return s

def int_convertable(s):
    try:
        s=float(s)
    except ValueError:
        return False
    return True

def date_convertible(s):
    try:                            #2021-06-29
        s=datetime.strptime(s, '%Y-%m-%d')
    except ValueError:
        return False
    return True

def bag_of_words(df):
    word_index = list(Series(df.values.ravel()).unique())
    return word_index

def convert(input, output = "output.vw"):
    df = pandas.read_csv(input)

    #remove columns
    df = df.drop(['date_activity', 'date_people'], 1)

    for column in df:
        df[column] = df[column].astype(str)

    # add column prefrix to values
    for column_idx, column in enumerate(df):
        for row_idx, row in enumerate(df.iterrows()):
            if not str(df.get_value(row_idx, column)) == "nan":
               value = str(column) + str(df.get_value(row_idx, column))
               df.set_value(row_idx, column, value)

    #all distinct "words"
    word_index = bag_of_words(df)
    print(len(word_index))

    #build vw datafile
    o = open(output, 'w')
    for row_idx, row in enumerate(df.iterrows()):
        new_line = ""

        label = None
        if df.get_value(row_idx, "outcome") == "outcome1":
            label = 1
        else:
            label = -1
        new_line += str(label) + " " + "|features "

        features = ""
        for column_idx, column in enumerate(df):
            if not str(df.get_value(row_idx, column)) == "nan":
                value = str(df.get_value(row_idx, column))
                if value in word_index:
                    index = word_index.index(value)
                    features += str(index) + ":1 "
        new_line += features
        new_line += "\n"
        o.write(new_line)