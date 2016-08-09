import pandas as pd

activity = pd.read_csv("act_train.csv")
people = pd.read_csv("people.csv")

"""omg en bitch"""
# how="left": take value from "left" and check in "right". left = activity.
joined = pd.merge(activity, people, on="people_id", how="left" , suffixes=('_activity', '_people'))
joined.to_csv("combined.csv")

print(people.columns, activity.columns)
print(joined.columns)

print(people.shape, activity.shape)
print(joined.shape)