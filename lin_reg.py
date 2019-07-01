import argparse
import pandas as pd
import numpy as np
import sys
from sklearn.linear_model import LinearRegression

combine= pd.read_csv("combine.csv")
print(pd.read_csv("train.csv")['Id'])
train = combine.loc[combine['Id'] in pd.read_csv("train.csv")['Id'], features]
test = combine.loc[combine['Id'] in pd.read_csv("train.csv")['Id'], features]

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

features = ['LotFrontage','LotArea', 'OverallQual', 'OverallCond', 'YearRemodAdd', 'Foundation', 'YrSold']


target = pd.DataFrame(data=train, columns=['SalePrice'], copy=True)
predictors = pd.DataFrame(data=train, columns=features, copy=True)


reg = LinearRegression().fit(predictors, target)

res = pd.DataFrame()
res['Id'] = test['Id']

res['SalePrice'] = reg.predict(test[features])


res.to_csv("res.csv", index=False)
