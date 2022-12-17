#!/usr/bin/env python
# coding: utf-8

# MLZC Capstone Project 1 - Q4/2022
# Diabetes Health Indicators Dataset  

#  T R A I N I N G   (xgboost)


print('\n*** BEG : train_patient_diabete_risk.py\n')

import sys
print('sys.version: ' , sys.version)

import pandas as pda
print('pda.__version__ : ' , pda.__version__)

import numpy as npy
print('npy.__version__ : ' , npy.__version__)

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.metrics import mutual_info_score
from sklearn.metrics import roc_auc_score
print('sklearn.__version__ : ' ,sklearn.__version__)

import xgboost as xgb
print('xgb.__version__ : ' , xgb.__version__)

from pydantic import BaseModel

import bentoml
print('bentoml.__version__ : ', bentoml.__version__)

from tqdm.notebook import tqdm 

# Url of csv file 
urlCsv = '.\data\diabetes_binary_health_indicators_BRFSS2015.csv'               # 253680 rows × 22 columns
print('urlCsv : ' , urlCsv)

# load dataframe from csv
dfrDia = pda.read_csv(urlCsv)
print('dfrDia.shape : ' , dfrDia.shape)

# force all columns in Integer
dfrDia = dfrDia.astype(int)

dfrDia.columns = dfrDia.columns.str.lower().str.replace(' ', '_')
print('dfrDia.columns : ' , dfrDia.columns )

# create the list of columns & features
lstCol = dfrDia.columns.to_list()

strTar = 'diabetes_binary'

lstFea = lstCol.copy()
lstFea.remove(strTar)

print('\nTarget:' , strTar   ,'\n')
print('Features:' , lstFea ,'\n' )

print('\n* Building framework (dataset) * ')
# dataframes
dfrTraFul, dfrTst = train_test_split(dfrDia   , test_size=0.20, random_state=1)
dfrTra   , dfrVal = train_test_split(dfrTraFul, test_size=0.25, random_state=1)

# Target variables
y_TraFul = dfrTraFul[strTar].values
y_Tra    = dfrTra   [strTar].values
y_Val    = dfrVal   [strTar].values
y_Tst    = dfrTst   [strTar].values
#print(len(dfrDia) , len(y_TraFul) , len(y_Tra) , len(y_Val) , len(y_Tst))

# Keep the Target in TraFul (for final training) but remove form others !
dfrTraFul.reset_index(drop=True, inplace=True) 

for dfr in [ dfrTra, dfrVal , dfrTst ]:
    dfr.reset_index(drop=True , inplace=True)
    dfr.drop(columns=[strTar] , axis=1 , inplace=True)

print('\n* Dimensions : ' , dfrDia.shape , dfrTraFul.shape , dfrTra.shape, dfrVal.shape , dfrTst.shape)

dfrTraFul.drop(columns=[strTar] , axis=1 , inplace=True)

print('\n* Building dma * ')
dvt = DictVectorizer(sparse=False)
dicTraFul = dfrTraFul.to_dict(orient='records')
X_TraFul = dvt.fit_transform(dicTraFul)
dmaTraFul = xgb.DMatrix(X_TraFul, label=y_TraFul )

dicTst = dfrTst.to_dict(orient='records')
X_Tst = dvt.transform(dicTst)
dmaTst = xgb.DMatrix(X_Tst)

# xgboost final
xgb_params = { 
    'eta': 0.1, 
    'max_depth': 4,
    'min_child_weight': 4,
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 8, 'seed': 1, 'verbosity': 1  }

print('\n* Training * ')

modXgb = xgb.train(xgb_params, dmaTraFul, num_boost_round=200 )

# # bentoml 
# ### Save xgb model + dic vectorizer

print('\n* Saving bentoml model * ')
modBen = bentoml.xgboost.save_model(
    'patient_diabete_risk',
    modXgb,
    custom_objects={
        'dictVectorizer': dvt
    })

print('\n * bentoml Model Info :' , modBen.info.to_dict())

print('\n * modBen.path : ' , modBen.path)

print('\n*** END : train_patient_diabete_risk.py\n')

