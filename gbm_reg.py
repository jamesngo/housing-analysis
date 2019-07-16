import argparse
import pandas as pd
import numpy as np
import sys
from sklearn import ensemble
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#splitting training and test sets
combine = pd.read_csv("combine.csv")
train = combine.loc[combine['Id'].isin(pd.read_csv("train.csv")['Id'].tolist())]
X_train = train.drop(['Id','SalePrice'], axis = 1)
Y_train = train['SalePrice']
test = combine.loc[combine['Id'].isin(pd.read_csv("test.csv")['Id'].tolist())]
Y_test = test.drop(['Id','SalePrice'], axis = 1)

#k-fold validator
kf = KFold(n_splits = 5, random_state=6969, shuffle=True)

params = { 'n_estimators': 2000, 'max_depth':4, 'min_samples_split': 2, 'learning_rate': 0.005, 'loss': 'ls', 'subsample':0.8, 'max_features':'sqrt'}

clf = ensemble.GradientBoostingRegressor(**params)

clf.fit(X_train, Y_train)

res = clf.predict(Y_test)
res = pd.Series(res)

res = pd.concat([test['Id'], res], axis=1)
res.columns = ['Id', 'SalePrice']
importances = pd.DataFrame(clf.feature_importances_).T
importances.columns = X_train.columns
print(importances)

res.to_csv("res.txt", index=False)
