# -*- coding: utf-8 -*-
"""confi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15GeEKv_zlLeCoY6YvUgQNeajV6PN3qUL
"""
train_path='/content/drive/MyDrive/Laon_prediction_model/loan_train.csv'
artifact_path='/content/drive/MyDrive/Laon_prediction_model/'
test_path='/content/drive/MyDrive/Laon_prediction_model/loan_test.csv'
text_path='/content/drive/MyDrive/Loanmodel_custom_modules/Loanrequirement.txt'
columns_to_drop=['SBA_Appv', 'DisbursementGross', 'City', 'Zip']
money_columns_in_string_format=['DisbursementGross','GrAppv','SBA_Appv','BalanceGross']
one_hot_col=['LowDoc']
target_hot_col=['State', 'Bank', 'BankState','RevLineCr' ]
Numerical_columns=['Zip', 'NAICS', 'NoEmp', 'NewExist', 'CreateJob', 'RetainedJob', 'FranchiseCode', 'UrbanRural', 'DisbursementGross', 'BalanceGross', 'GrAppv', 'SBA_Appv']
categorical_columns=['City', 'State', 'Bank', 'BankState', 'RevLineCr', 'LowDoc']
scaling_columns=['NAICS'	,'NoEmp',	'NewExist','CreateJob','RetainedJob','FranchiseCode','UrbanRural','BalanceGross','GrAppv']
discrete_col=['State', 'Bank', 'BankState', 'NAICS', 'NoEmp', 'CreateJob', 'RetainedJob', 'FranchiseCode', 'UrbanRural', 'RevLineCr', 'LowDoc']