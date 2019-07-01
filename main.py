"""Main Driver."""

import argparse
import pandas as pd
import numpy as np
import sys

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

### ARGUMENTS ###
parser = argparse.ArgumentParser()
parser.add_argument('--column', type=str)
args = parser.parse_args()


### DATA IMPORT ###
test = pd.read_csv("test.csv") 
train = pd.read_csv("train.csv")
df = test.append(train, verify_integrity=True, sort=False, ignore_index=True)


### IMPUTING ###
#imputing MSZoning with mode
df['MSZoning'].fillna(df['MSZoning'].mode()[0], inplace=True)

#imputing LotFrontage with mean
df['LotFrontage'].fillna(df['LotFrontage'].mean(), inplace=True)

#imputing Utilities with mode
df['Utilities'].fillna(df['Utilities'].mode()[0], inplace=True)

#imputing Exterior1st with mode
df['Exterior1st'].fillna(df['Exterior1st'].mode()[0], inplace=True)

#imputing Exterior2nd with mode
df['Exterior2nd'].fillna(df['Exterior2nd'].mode()[0], inplace=True)

#imputing MasVnrType with mode
df['MasVnrType'].fillna(df['MasVnrType'].mode()[0], inplace=True)

#imputing MasVnrArea with mode
df['MasVnrArea'].fillna(df['MasVnrArea'].mean(), inplace=True)

#imputing MasVnrType with mode
df['Electrical'].fillna(df['Electrical'].mode()[0], inplace=True)

#imputing BsmtFullBath with mode
df['BsmtFullBath'].fillna(df['BsmtFullBath'].mode()[0], inplace=True)

#imputing BsmtHalfBath with mode
df['BsmtHalfBath'].fillna(df['BsmtHalfBath'].mode()[0], inplace=True)

#imputing KitchenQual with mode
df['KitchenQual'].fillna(df['KitchenQual'].mode()[0], inplace=True)

#imputing Functional with mode
df['Functional'].fillna(df['Functional'].mode()[0], inplace=True)

#imputing SaleType with mode
df['SaleType'].fillna(df['SaleType'].mode()[0], inplace=True)

#If the pool area is non-zero, imputing it with the 'Ex' (mode)
for i, quality in df['PoolQC'].iteritems():
    if df['PoolArea'][i] != 0 and str(quality).strip() == "nan":
        df['PoolQC'] = df['PoolQC'].mode()[0]

#If one of the Garage features is not present, fill all missing features
columns = ['GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond']
for i, row in df.loc[:,columns].iterrows():
    nan = []
    for col in columns:
        if str(row[col]).strip() == "nan":
            nan.append(col)
        if col == 'GarageCars' and row['GarageCars'] == 0:
            nan.append(col)
        if col == 'GarageArea' and row['GarageArea'] == 0:
            nan.append(col)

    if len(nan) == 0 or len(nan) == len(columns):
        pass
    else:
        for col in nan:
            if col == 'GarageArea':
               df.loc[i, col] = df[col].mean() 
            else:
                df.loc[i, col] = df[col].mode()[0]
        if df['YearBuilt'][i] > df['GarageYrBlt'][i]:
            df.loc[i, 'GarageYrBlt'] = df['YearBuilt'][i]

### TESTING COLUMNS ###


columns = ['BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath']
for i, row in df.loc[:,columns].iterrows():
    nan = []



print(df.describe())
print(df.isna().sum())
if not (args.column is None):
    print(df[args.column].describe())
    print(df[args.column].isna().sum())
