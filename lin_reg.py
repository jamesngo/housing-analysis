import argparse
import pandas as pd
import numpy as np
import sys
from sklearn.linear_model import LinearRegression

features = ['LotFrontage','LotArea', 'OverallQual', 'OverallCond', 'YearRemodAdd', 'Foundation', 'YrSold']

#splitting training and test sets
combine= pd.read_csv("combine.csv")
print(pd.read_csv("train.csv")['Id'])
train = combine.loc[combine['Id'].isin(pd.read_csv("train.csv")['Id'].tolist())]
test = combine.loc[combine['Id'].isin(pd.read_csv("test.csv")['Id'].tolist())]


#splitting training set into target and predictors column using pandas dataframe constructor
target = pd.DataFrame(data=train, columns=['SalePrice'], copy=True)
predictors = pd.DataFrame(data=train, columns=features, copy=True)

#fitting the data
reg = LinearRegression().fit(predictors, target)

#creating new dataframe which will have our result in it, we will index it using "Id"
res = pd.DataFrame()
res['Id'] = test['Id']


#prediction
res['SalePrice'] = reg.predict(test[features])


#export to csv
res.to_csv("res.csv", index=False)
