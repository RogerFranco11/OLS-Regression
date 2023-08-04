# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

OLS Ordinary Least Squares
"""
import numpy as np 
import statsmodels.api as sm
import pandas as pd

# reading data from the csv
data = pd.read_csv('toyData.csv')
data.columns

# defining the variables
y = data['y'].tolist()
x1 = data['x1'].tolist()
x2 = data['x2'].tolist()

 
X = np.array([[1,-4,6,3],[4,3,1,5]])
X = X.T
# adding the constant term
X = sm.add_constant(X)
 
# performing the regression
# and fitting the model
result = sm.OLS(y, X).fit()
 
# printing the summary table
print(result.summary()) 