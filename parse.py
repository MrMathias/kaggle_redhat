import pandas as pd

#Train data
activity_train = pd.read_csv("act_train.csv")
people = pd.read_csv("people.csv")

# how="left": take value from "left" and check in "right". left = activity.
joined = pd.merge(activity_train, people, on="people_id", how="left" , suffixes=('_activity', '_people'))
joined.to_csv("small_combined_train.csv", index=False)

# Test data
activity_test = pd.read_csv("act_test.csv")
people = pd.read_csv("people.csv")

# how="left": take value from "left" and check in "right". left = activity.
joined = pd.merge(activity_test, people, on="people_id", how="left" , suffixes=('_activity', '_people'))
joined.to_csv("small_combined_test.csv", index=False)
