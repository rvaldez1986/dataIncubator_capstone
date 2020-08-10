# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:01:16 2020

@author: rober
"""

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn import base
import numpy as np
import pandas as pd

import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

from sklearn import base
class ColumnSelectTransformer(base.BaseEstimator, base.TransformerMixin):    
    def __init__(self, col_names=[]):
        self.col_names = col_names  
    
    def fit(self, X, y=None):      
        return self
    
    def transform(self, X, y=None):
        return X[self.col_names]


class EncoderTransformer(base.BaseEstimator, base.TransformerMixin):    
    def __init__(self):       
        self.encColumns = None
        self.scColumns = None
        self.encoder = None 
        self.feature_Names = None
    
    def fit(self, X, y=None):
        self.scColumns = [x for x,y in zip(X.columns,X.dtypes) if y !=  'object']
        self.encColumns = [x for x in X.columns if x not in self.scColumns]        
        self.encoder = OneHotEncoder(handle_unknown='ignore')
        self.encoder.fit(X[self.encColumns])    
        self.feature_Names = self.scColumns + list(self.encoder.get_feature_names(self.encColumns))
        return self
    
    def transform(self, X, y=None): 
        notenc = X[self.scColumns].to_numpy()
        encoded = self.encoder.transform(X[self.encColumns]).toarray()  
        data = np.concatenate((notenc, encoded), axis=1)      
        return  pd.DataFrame(data=data, columns= self.feature_Names) 