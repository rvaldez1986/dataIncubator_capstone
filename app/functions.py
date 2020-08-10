# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:03:54 2020

@author: rober
"""

from scipy.spatial import distance
import numpy as np

def GaussianKernel(v1, v2, sigma):
    l2norm = distance.euclidean(v1, v2)
    return np.exp(-l2norm**2/(2.*sigma**2))

def state_simil(df, x):
    df2 = df.copy()  #de reference
    sim_index = []
    for i in df2.index:
        x2 = np.array(df2.loc[i][3:])
        sim_index.append(GaussianKernel(x, x2, 1))
    df2['sim_index'] = sim_index
    return df2



html_string = """
<!DOCTYPE html>

<html lang=\"en\">

<head>
  <meta charset=\"utf-8\"/>
  <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"/>
  <title>Results</title>
  <meta name=\"HandheldFriendly\" content=\"True\"/>
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, viewport-fit=cover\"/>
  <meta name=\"theme-color\" content=\"#5eb9d7\"/>
  <script src=\"https://cdn.plot.ly/plotly-latest.min.js\"></script>
  <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css\">
  <link rel=\"stylesheet" href=\"/static/css/style.css\" rel=\"stylesheet\" type=\"text/css\">
  <link rel=\"stylesheet" href=\"/static/css/forms.css\" rel=\"stylesheet\" type=\"text/css\">
  <script src=\"https://kit.fontawesome.com/e3deaeba31.js\" crossorigin=\"anonymous\"></script>
  <link href=\"https://fonts.googleapis.com/css?family=Poppins:200,300,500\" rel=\"stylesheet\">
</head>

<body>
<div class="container">
 <div class="formwrapperRes1">
   <h1 class="title">Credit Scoring Model Results</h1>     
      <div class="formwrapperRes2">
          <h2>Credit default probability</h2>            
          <center><img src="{1}" width="320" height="238"/></center>    
      </div>      
      <div class="formwrapperRes3">
          {0} 
      </div>
 </div>
</div> 
</body>
</html>
"""
