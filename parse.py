import pandas as pd

act = pd.read_csv("act_train.csv")

people = pd.read_csv("people.csv")

print(people.columns, act.columns)
print(people.shape, act.shape)

joined = act.join(people,on='people_id',how='left',lsuffix='p',rsuffix='a')

print(joined.shape)