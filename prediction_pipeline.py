# -*- coding: utf-8 -*-
"""Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TqA-wfnRXa7R2TjlzzYz0QBTPHVLi1p7

First i want to find path of saved model, call all custom estimators and text file containing all required packages list and install them if do not exist.
As i am using my drive as my cloud storage so i will mount my google drive
"""

from google.colab import drive
import sys
drive.mount('/content/drive')
sys.path.append('/content/drive/MyDrive/Loanmodel_custom_modules')
import confi as confi
import preprocessing as lp
#No extracting path having all saved artifacts and my test data for prediction that i will use in my custom estimators to make pipeline
p=confi.artifact_path


import numpy as np
import pandas as pd
import pickle
import sys
from pathlib import Path
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', 1500)
# set seed for reproducibility
np.random.seed(123)


import warnings
warnings.filterwarnings('ignore')

#Extend cell width
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:80% !important; }</style>"))
from category_encoders import TargetEncoder
from sklearn.pipeline import Pipeline

class prediction:
  def __init__(self):
    pass
  def predict_function(self,f):
    f['bank_customer_state']=np.where(f['BankState']==f['State'],1,0)
    pipeline=Pipeline([('money_data',lp.money_data(variables=confi.money_columns_in_string_format)),
                   ('Numerical_test_impute',lp.Numerical_test_imputer(path=p,variables=confi.Numerical_columns)),
                   ('categorical_test_imputer',lp.categorical_test_imputer(path=p,variables=confi.categorical_columns)),
                   ('drop_colunms',lp.drop_colunms(variables=confi.columns_to_drop)),
                   ('onehot_test_encoder',lp.onehot_test_encoder(path=p,variables=confi.one_hot_col)),
                   ('target_test_encoder',lp.target_test_encoder(path=p,variables=confi.target_hot_col)),
                   ('scalar_test_encoder',lp.scalar_test_encoder(path=p,variables=confi.scaling_columns))])
    f=pipeline.fit_transform(f)
    model=pickle.load(open(p+'StackingClassifier_model.pkl','rb'))
    result=model.predict(f)
    return result