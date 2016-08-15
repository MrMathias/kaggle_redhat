import csv
from datetime import datetime

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
    try:                     #2021-06-29
        s=datetime.strptime(s, '%Y-%m-%d')
    except ValueError:
        return False
    return True

def convert(input, word_index, train, output = "output.vw"):
    o = open(output, 'w')
    count = 0
    with open(input) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # print(row)
            count += 1
            if count % 10000 == 0:
                print(count, "--",datetime.now())
            new_line = ""
            label = ""
            features = ""
            for (k,v) in row.items():
                if v != "":
                    if train and k == "outcome":
                        if v == "0":
                            label = "-1"
                        if v == "1":
                            label = "1"

                    # make features
                    # -- bag of words
                    # -- skip some columns
                    if ((k != "date_activity") and (k != "date_people") and (k != "activity_id") and (k != "outcome")):
                        if k+v in word_index:
                            pass
                            index = word_index[k+v]
                            features += str(index) + ":1 "

            # line finished
            new_line += label + " " + "|features " + features + "\n"
            # print(new_line)
            o.write(new_line)