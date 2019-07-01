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

#enumerating Alley with numbers
print(train['Alley'].astype("category").cat.codes.unique())
train['Alley'] = train['Alley'].astype("category").cat.codes
print(train['Alley'].isna().sum())

#enumerating MSZoning
print(train['MSZoning'].astype("category").cat.codes.unique())
print(train['MSZoning'].astype("category").unique())
train['MSZoning'] = train['MSZoning'].astype("category").cat.codes
print(train['MSZoning'].isna().sum())

#enumerating MSSubClass
print(train['MSSubClass'].astype("category").cat.codes.unique())
print(train['MSSubClass'].astype("category").unique())
train['MSSubClass'] = train['MSSubClass'].astype("category").cat.codes
print(train['MSSubClass'].isna().sum())

#enumerating LotArea
print(train['LotArea'].astype("category").cat.codes.unique())
print(train['LotArea'].astype("category").unique())
train['LotArea'] = train['LotArea'].astype("category").cat.codes
print(train['LotArea'].isna().sum())

#enumerating Street
print(train['Street'].astype("category").cat.codes.unique())
print(train['Street'].astype("category").unique())
train['Street'] = train['Street'].astype("category").cat.codes
print(train['Street'].isna().sum())

#enumerating LotShape
print(train['LotShape'].astype("category").cat.codes.unique())
print(train['LotShape'].astype("category").unique())
train['LotShape'] = train['LotShape'].astype("category").cat.codes
print(train['LotShape'].isna().sum())

#enumerating LandContour
print(train['LandContour'].astype("category").cat.codes.unique())
print(train['LandContour'].astype("category").unique())
train['LandContour'] = train['LandContour'].astype("category").cat.codes
print(train['LandContour'].isna().sum())

#enumerating Utilities
print(train['Utilities'].astype("category").cat.codes.unique())
print(train['Utilities'].astype("category").unique())
train['Utilities'] = train['Utilities'].astype("category").cat.codes
print(train['Utilities'].isna().sum())

#enumerating LotConfig
print(train['LotConfig'].astype("category").cat.codes.unique())
print(train['LotConfig'].astype("category").unique())
train['LotConfig'] = train['LotConfig'].astype("category").cat.codes
print(train['LotConfig'].isna().sum())

#enumerating LandSlope
print(train['LandSlope'].astype("category").cat.codes.unique())
print(train['LandSlope'].astype("category").unique())
train['LandSlope'] = train['LandSlope'].astype("category").cat.codes
print(train['LandSlope'].isna().sum())

#enumerating Neighborhood
print(train['Neighborhood'].astype("category").cat.codes.unique())
print(train['Neighborhood'].astype("category").unique())
train['Neighborhood'] = train['Neighborhood'].astype("category").cat.codes
print(train['Neighborhood'].isna().sum())

#enumerating Condition1
print(train['Condition1'].astype("category").cat.codes.unique())
print(train['Condition1'].astype("category").unique())
train['Condition1'] = train['Condition1'].astype("category").cat.codes
print(train['Condition1'].isna().sum())

#enumerating Condition2
print(train['Condition2'].astype("category").cat.codes.unique())
print(train['Condition2'].astype("category").unique())
train['Condition2'] = train['Condition2'].astype("category").cat.codes
print(train['Condition2'].isna().sum())

#enumerating BldgType
print(train['BldgType'].astype("category").cat.codes.unique())
print(train['BldgType'].astype("category").unique())
train['BldgType'] = train['BldgType'].astype("category").cat.codes
print(train['BldgType'].isna().sum())

#enumerating HouseStyle
print(train['HouseStyle'].astype("category").cat.codes.unique())
print(train['HouseStyle'].astype("category").unique())
train['HouseStyle'] = train['HouseStyle'].astype("category").cat.codes
print(train['HouseStyle'].isna().sum())

#enumerating RoofStyle
print(train['RoofStyle'].astype("category").cat.codes.unique())
print(train['RoofStyle'].astype("category").unique())
train['RoofStyle'] = train['RoofStyle'].astype("category").cat.codes
print(train['RoofStyle'].isna().sum())

#enumerating RoofMatl
print(train['RoofMatl'].astype("category").cat.codes.unique())
print(train['RoofMatl'].astype("category").unique())
train['RoofMatl'] = train['RoofMatl'].astype("category").cat.codes
print(train['RoofMatl'].isna().sum())

#enumerating Exterior1st
print(train['Exterior1st'].astype("category").cat.codes.unique())
print(train['Exterior1st'].astype("category").unique())
train['Exterior1st'] = train['Exterior1st'].astype("category").cat.codes
print(train['Exterior1st'].isna().sum())

#enumerating Exterior2nd
print(train['Exterior2nd'].astype("category").cat.codes.unique())
print(train['Exterior2nd'].astype("category").unique())
train['Exterior2nd'] = train['Exterior2nd'].astype("category").cat.codes
print(train['Exterior2nd'].isna().sum())

#enumerating MasVnrType
print(train['MasVnrType'].astype("category").cat.codes.unique())
print(train['MasVnrType'].astype("category").unique())
train['MasVnrType'] = train['MasVnrType'].astype("category").cat.codes
print(train['MasVnrType'].isna().sum())

#enumerating ExterQual
print(train['ExterQual'].astype("category").cat.codes.unique())
print(train['ExterQual'].astype("category").unique())
train['ExterQual'] = train['ExterQual'].astype("category").cat.codes
print(train['ExterQual'].isna().sum())

#enumerating ExterCond
print(train['ExterCond'].astype("category").cat.codes.unique())
print(train['ExterCond'].astype("category").unique())
train['ExterCond'] = train['ExterCond'].astype("category").cat.codes
print(train['ExterCond'].isna().sum())

#enumerating Foundation
print(train['Foundation'].astype("category").cat.codes.unique())
print(train['Foundation'].astype("category").unique())
train['Foundation'] = train['Foundation'].astype("category").cat.codes
print(train['Foundation'].isna().sum())

#enumerating BsmtQual
print(train['BsmtQual'].astype("category").cat.codes.unique())
print(train['BsmtQual'].astype("category").unique())
train['BsmtQual'] = train['BsmtQual'].astype("category").cat.codes
print(train['BsmtQual'].isna().sum())

#enumerating BsmtCond
print(train['BsmtCond'].astype("category").cat.codes.unique())
print(train['BsmtCond'].astype("category").unique())
train['BsmtCond'] = train['BsmtCond'].astype("category").cat.codes
print(train['BsmtCond'].isna().sum())

#enumerating BsmtExposure
print(train['BsmtExposure'].astype("category").cat.codes.unique())
print(train['BsmtExposure'].astype("category").unique())
train['BsmtExposure'] = train['BsmtExposure'].astype("category").cat.codes
print(train['BsmtExposure'].isna().sum())

#enumerating BsmtFinType1
print(train['BsmtFinType1'].astype("category").cat.codes.unique())
print(train['BsmtFinType1'].astype("category").unique())
train['BsmtFinType1'] = train['BsmtFinType1'].astype("category").cat.codes
print(train['BsmtFinType1'].isna().sum())

#enumerating BsmtFinType2
print(train['BsmtFinType2'].astype("category").cat.codes.unique())
print(train['BsmtFinType2'].astype("category").unique())
train['BsmtFinType2'] = train['BsmtFinType2'].astype("category").cat.codes
print(train['BsmtFinType2'].isna().sum())

#enumerating Heating
print(train['Heating'].astype("category").cat.codes.unique())
print(train['Heating'].astype("category").unique())
train['Heating'] = train['Heating'].astype("category").cat.codes
print(train['Heating'].isna().sum())

#enumerating HeatingQC
print(train['HeatingQC'].astype("category").cat.codes.unique())
print(train['HeatingQC'].astype("category").unique())
train['HeatingQC'] = train['HeatingQC'].astype("category").cat.codes
print(train['HeatingQC'].isna().sum())

#enumerating Electrical
print(train['Electrical'].astype("category").cat.codes.unique())
print(train['Electrical'].astype("category").unique())
train['Electrical'] = train['Electrical'].astype("category").cat.codes
print(train['Electrical'].isna().sum())

#enumerating KitchenQual
print(train['KitchenQual'].astype("category").cat.codes.unique())
print(train['KitchenQual'].astype("category").unique())
train['KitchenQual'] = train['KitchenQual'].astype("category").cat.codes
print(train['KitchenQual'].isna().sum())

#enumerating Functional
print(train['Functional'].astype("category").cat.codes.unique())
print(train['Functional'].astype("category").unique())
train['Functional'] = train['Functional'].astype("category").cat.codes
print(train['Functional'].isna().sum())
 
#enumerating GarageType
print(train['GarageType'].astype("category").cat.codes.unique())
print(train['GarageType'].astype("category").unique())
train['GarageType'] = train['GarageType'].astype("category").cat.codes
print(train['GarageType'].isna().sum())

#enumerating GarageFinish
print(train['GarageFinish'].astype("category").cat.codes.unique())
print(train['GarageFinish'].astype("category").unique())
train['GarageFinish'] = train['GarageFinish'].astype("category").cat.codes
print(train['GarageFinish'].isna().sum())

#enumerating SaleType
print(train['SaleType'].astype("category").cat.codes.unique())
print(train['SaleType'].astype("category").unique())
train['SaleType'] = train['SaleType'].astype("category").cat.codes
print(train['SaleType'].isna().sum())

#enumerating SaleCondition
print(train['SaleCondition'].astype("category").cat.codes.unique())
print(train['SaleCondition'].astype("category").unique())
train['SaleCondition'] = train['SaleCondition'].astype("category").cat.codes
print(train['SaleCondition'].isna().sum())
