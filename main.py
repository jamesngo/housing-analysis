"""Main Driver."""

import argparse
import pandas as pd
import numpy as np
import sys

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

train = pd.read_csv("train.csv")

print(train.isna().sum())

#imputing electrical column with mode
print(train['Electrical'].isna().sum())
print(train['Electrical'].mode()[0])
train['Electrical'].fillna(train['Electrical'].mode()[0], inplace=True)
print(train['Electrical'].isna().sum())

#imputing vnr type with mode and mean
print(train['MasVnrType'].isna().sum())
print(train['MasVnrType'].mode()[0])
train['MasVnrType'].fillna(train['MasVnrType'].mode()[0], inplace=True)
train['MasVnrArea'].fillna(0, inplace=True)
print(train['MasVnrType'].isna().sum())

#imputing lot frontage with mean
print(train['LotFrontage'].isna().sum())
print(train['LotFrontage'].mean())
train['LotFrontage'].fillna(train['LotFrontage'].mean(), inplace=True)
print(train['LotFrontage'].isna().sum())

#has basement square footage, but has nan value
print(train['BsmtFinType2'].unique())
"""
no_basement = {}
for index in range(len(train['BsmtFinType2'])):
    if np.isnan(train['BsmtFinType2'][index]):
        no_basement.append(index)
missing = {}
for index in no_basement:
    if np.isnan(train['TotalBsmtSF'][index]) != 0:
        missing.append(index)
print(len(missing))"""
