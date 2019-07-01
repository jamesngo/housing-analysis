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




print(df.isna().sum())

#imputing electrical column with mode
print(df['Electrical'].isna().sum())
print(df['Electrical'].mode()[0])
df['Electrical'].fillna(df['Electrical'].mode()[0], inplace=True)
print(df['Electrical'].isna().sum())

#imputing vnr type with mode and mean
print(df['MasVnrType'].isna().sum())
print(df['MasVnrType'].mode()[0])
df['MasVnrType'].fillna(df['MasVnrType'].mode()[0], inplace=True)
df['MasVnrArea'].fillna(0, inplace=True)
print(df['MasVnrType'].isna().sum())

#imputing lot frontage with mean
print(df['LotFrontage'].isna().sum())
print(df['LotFrontage'].mean())
df['LotFrontage'].fillna(df['LotFrontage'].mean(), inplace=True)
print(df['LotFrontage'].isna().sum())

#enumerating Alley with numbers
print(df['Alley'].astype("category").cat.codes.unique())
df['Alley'] = df['Alley'].astype("category").cat.codes
print(df['Alley'].isna().sum())

#enumerating MSZoning
print(df['MSZoning'].astype("category").cat.codes.unique())
print(df['MSZoning'].astype("category").unique())
df['MSZoning'] = df['MSZoning'].astype("category").cat.codes
print(df['MSZoning'].isna().sum())

#enumerating MSSubClass
print(df['MSSubClass'].astype("category").cat.codes.unique())
print(df['MSSubClass'].astype("category").unique())
df['MSSubClass'] = df['MSSubClass'].astype("category").cat.codes
print(df['MSSubClass'].isna().sum())

#enumerating LotArea
print(df['LotArea'].astype("category").cat.codes.unique())
print(df['LotArea'].astype("category").unique())
df['LotArea'] = df['LotArea'].astype("category").cat.codes
print(df['LotArea'].isna().sum())

#enumerating Street
print(df['Street'].astype("category").cat.codes.unique())
print(df['Street'].astype("category").unique())
df['Street'] = df['Street'].astype("category").cat.codes
print(df['Street'].isna().sum())

#enumerating LotShape
print(df['LotShape'].astype("category").cat.codes.unique())
print(df['LotShape'].astype("category").unique())
df['LotShape'] = df['LotShape'].astype("category").cat.codes
print(df['LotShape'].isna().sum())

#enumerating LandContour
print(df['LandContour'].astype("category").cat.codes.unique())
print(df['LandContour'].astype("category").unique())
df['LandContour'] = df['LandContour'].astype("category").cat.codes
print(df['LandContour'].isna().sum())

#enumerating Utilities
print(df['Utilities'].astype("category").cat.codes.unique())
print(df['Utilities'].astype("category").unique())
df['Utilities'] = df['Utilities'].astype("category").cat.codes
print(df['Utilities'].isna().sum())

#enumerating LotConfig
print(df['LotConfig'].astype("category").cat.codes.unique())
print(df['LotConfig'].astype("category").unique())
df['LotConfig'] = df['LotConfig'].astype("category").cat.codes
print(df['LotConfig'].isna().sum())

#enumerating LandSlope
print(df['LandSlope'].astype("category").cat.codes.unique())
print(df['LandSlope'].astype("category").unique())
df['LandSlope'] = df['LandSlope'].astype("category").cat.codes
print(df['LandSlope'].isna().sum())

#enumerating Neighborhood
print(df['Neighborhood'].astype("category").cat.codes.unique())
print(df['Neighborhood'].astype("category").unique())
df['Neighborhood'] = df['Neighborhood'].astype("category").cat.codes
print(df['Neighborhood'].isna().sum())

#enumerating Condition1
print(df['Condition1'].astype("category").cat.codes.unique())
print(df['Condition1'].astype("category").unique())
df['Condition1'] = df['Condition1'].astype("category").cat.codes
print(df['Condition1'].isna().sum())

#enumerating Condition2
print(df['Condition2'].astype("category").cat.codes.unique())
print(df['Condition2'].astype("category").unique())
df['Condition2'] = df['Condition2'].astype("category").cat.codes
print(df['Condition2'].isna().sum())

#enumerating BldgType
print(df['BldgType'].astype("category").cat.codes.unique())
print(df['BldgType'].astype("category").unique())
df['BldgType'] = df['BldgType'].astype("category").cat.codes
print(df['BldgType'].isna().sum())

#enumerating HouseStyle
print(df['HouseStyle'].astype("category").cat.codes.unique())
print(df['HouseStyle'].astype("category").unique())
df['HouseStyle'] = df['HouseStyle'].astype("category").cat.codes
print(df['HouseStyle'].isna().sum())

#enumerating RoofStyle
print(df['RoofStyle'].astype("category").cat.codes.unique())
print(df['RoofStyle'].astype("category").unique())
df['RoofStyle'] = df['RoofStyle'].astype("category").cat.codes
print(df['RoofStyle'].isna().sum())

#enumerating RoofMatl
print(df['RoofMatl'].astype("category").cat.codes.unique())
print(df['RoofMatl'].astype("category").unique())
df['RoofMatl'] = df['RoofMatl'].astype("category").cat.codes
print(df['RoofMatl'].isna().sum())

#enumerating Exterior1st
print(df['Exterior1st'].astype("category").cat.codes.unique())
print(df['Exterior1st'].astype("category").unique())
df['Exterior1st'] = df['Exterior1st'].astype("category").cat.codes
print(df['Exterior1st'].isna().sum())

#enumerating Exterior2nd
print(df['Exterior2nd'].astype("category").cat.codes.unique())
print(df['Exterior2nd'].astype("category").unique())
df['Exterior2nd'] = df['Exterior2nd'].astype("category").cat.codes
print(df['Exterior2nd'].isna().sum())

#enumerating MasVnrType
print(df['MasVnrType'].astype("category").cat.codes.unique())
print(df['MasVnrType'].astype("category").unique())
df['MasVnrType'] = df['MasVnrType'].astype("category").cat.codes
print(df['MasVnrType'].isna().sum())

#enumerating ExterQual
print(df['ExterQual'].astype("category").cat.codes.unique())
print(df['ExterQual'].astype("category").unique())
df['ExterQual'] = df['ExterQual'].astype("category").cat.codes
print(df['ExterQual'].isna().sum())

#enumerating ExterCond
print(df['ExterCond'].astype("category").cat.codes.unique())
print(df['ExterCond'].astype("category").unique())
df['ExterCond'] = df['ExterCond'].astype("category").cat.codes
print(df['ExterCond'].isna().sum())

#enumerating Foundation
print(df['Foundation'].astype("category").cat.codes.unique())
print(df['Foundation'].astype("category").unique())
df['Foundation'] = df['Foundation'].astype("category").cat.codes
print(df['Foundation'].isna().sum())

#enumerating BsmtQual
print(df['BsmtQual'].astype("category").cat.codes.unique())
print(df['BsmtQual'].astype("category").unique())
df['BsmtQual'] = df['BsmtQual'].astype("category").cat.codes
print(df['BsmtQual'].isna().sum())

#enumerating BsmtCond
print(df['BsmtCond'].astype("category").cat.codes.unique())
print(df['BsmtCond'].astype("category").unique())
df['BsmtCond'] = df['BsmtCond'].astype("category").cat.codes
print(df['BsmtCond'].isna().sum())

#enumerating BsmtExposure
print(df['BsmtExposure'].astype("category").cat.codes.unique())
print(df['BsmtExposure'].astype("category").unique())
df['BsmtExposure'] = df['BsmtExposure'].astype("category").cat.codes
print(df['BsmtExposure'].isna().sum())

#enumerating BsmtFinType1
print(df['BsmtFinType1'].astype("category").cat.codes.unique())
print(df['BsmtFinType1'].astype("category").unique())
df['BsmtFinType1'] = df['BsmtFinType1'].astype("category").cat.codes
print(df['BsmtFinType1'].isna().sum())

#enumerating BsmtFinType2
print(df['BsmtFinType2'].astype("category").cat.codes.unique())
print(df['BsmtFinType2'].astype("category").unique())
df['BsmtFinType2'] = df['BsmtFinType2'].astype("category").cat.codes
print(df['BsmtFinType2'].isna().sum())

#enumerating Heating
print(df['Heating'].astype("category").cat.codes.unique())
print(df['Heating'].astype("category").unique())
df['Heating'] = df['Heating'].astype("category").cat.codes
print(df['Heating'].isna().sum())

#enumerating HeatingQC
print(df['HeatingQC'].astype("category").cat.codes.unique())
print(df['HeatingQC'].astype("category").unique())
df['HeatingQC'] = df['HeatingQC'].astype("category").cat.codes
print(df['HeatingQC'].isna().sum())

#enumerating Electrical
print(df['Electrical'].astype("category").cat.codes.unique())
print(df['Electrical'].astype("category").unique())
df['Electrical'] = df['Electrical'].astype("category").cat.codes
print(df['Electrical'].isna().sum())

#enumerating KitchenQual
print(df['KitchenQual'].astype("category").cat.codes.unique())
print(df['KitchenQual'].astype("category").unique())
df['KitchenQual'] = df['KitchenQual'].astype("category").cat.codes
print(df['KitchenQual'].isna().sum())

#enumerating Functional
print(df['Functional'].astype("category").cat.codes.unique())
print(df['Functional'].astype("category").unique())
df['Functional'] = df['Functional'].astype("category").cat.codes
print(df['Functional'].isna().sum())
 
#enumerating GarageType
print(df['GarageType'].astype("category").cat.codes.unique())
print(df['GarageType'].astype("category").unique())
df['GarageType'] = df['GarageType'].astype("category").cat.codes
print(df['GarageType'].isna().sum())

#enumerating GarageFinish
print(df['GarageFinish'].astype("category").cat.codes.unique())
print(df['GarageFinish'].astype("category").unique())
df['GarageFinish'] = df['GarageFinish'].astype("category").cat.codes
print(df['GarageFinish'].isna().sum())

#enumerating SaleType
print(df['SaleType'].astype("category").cat.codes.unique())
print(df['SaleType'].astype("category").unique())
df['SaleType'] = df['SaleType'].astype("category").cat.codes
print(df['SaleType'].isna().sum())

#enumerating SaleCondition
print(df['SaleCondition'].astype("category").cat.codes.unique())
print(df['SaleCondition'].astype("category").unique())
df['SaleCondition'] = df['SaleCondition'].astype("category").cat.codes
print(df['SaleCondition'].isna().sum())

df.to_csv("combine.csv")
