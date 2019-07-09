import argparse
import pandas as pd
import numpy as np
import sys
from sklearn import ensemble

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#splitting training and test sets
combine= pd.read_csv("combine.csv")
train = combine.loc[combine['Id'].isin(pd.read_csv("train.csv")['Id'].tolist())]
test = combine.loc[combine['Id'].isin(pd.read_csv("test.csv")['Id'].tolist())]


params = { 'n_estimators': 500, 'max_depth':4, 'min_samples_split': 2, 'learning_rate': 0.01, 'loss': 'ls'}

clf = ensemble.GradientBoostingRegressor(**params)
clf.fit(train.drop(['Id','SalePrice'], axis=1), train['SalePrice'])

res = clf.predict(test.drop(['Id','SalePrice'], axis=1))
res = pd.Series(res)

res = pd.concat([test['Id'], res], axis=1)
res.columns = ['Id', 'SalePrice']
res.to_csv("res.txt", index=False)
