import argparse
import pandas as pd
import numpy as np
import sys
from sklearn.linear_model import LinearRegression

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

features = ['LotFrontage','LotArea', 'OverallQual', 'OverallCond', 'YearRemodAdd', 'GarageArea']

#imputing with mean
train['LotFrontage'].fillna(train['LotFrontage'].mean(), inplace=True)
test['LotFrontage'].fillna(test['LotFrontage'].mean(), inplace=True)
test['BsmtFinSF1'].fillna(test['BsmtFinSF1'].mean(), inplace=True)


target = pd.DataFrame(data=train, columns=['SalePrice'], copy=True)
predictors = pd.DataFrame(data=train, columns=features, copy=True)


reg = LinearRegression().fit(predictors, target)

res = pd.DataFrame()
res['Id'] = test['Id']

res['SalePrice'] = reg.predict(test[features])


res.to_csv("res.csv", index=False)
