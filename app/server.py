# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:44:37 2020

@author: rober
"""

from flask import Flask, url_for, render_template, redirect
from forms import ContactForm
import os
import numpy as np
import pandas as pd
import re
from sklearn.externals import joblib  #save trained scaler
from plots import create_plot, plot2
from functions import state_simil, html_string



app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
df_state = pd.read_pickle('data//df_state2.pkl')
scaler = joblib.load( 'data//state_scaler.pkl')


@app.route('/')
def home():
    return render_template('index.jinja2',
                           template='home-template')
    
    


@app.route('/inputs', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit(): 
        l = [form.input1.data, form.input2.data]        
        return redirect(url_for('success', listOfObjects = l))
    return render_template('contact.jinja2',
                           form=form, title = 'Inputs')
    
    
    
    
    
@app.route('/success/<listOfObjects>', methods=('GET', 'POST'))
def success(listOfObjects):  
    l = listOfObjects
    res = l.strip('][').split(', ') 
    res = [re.sub(r'[\']', '', line) for line in res]
    #print(url_for('static', filename='css/style.css'))    
    
    x_cal0 = np.array([79975.5,0.5064,146.785,5.53])
    x_cal = scaler.transform(x_cal0.reshape(1, -1))[0]
    df_state2 = state_simil(df_state, x_cal) 
    df_state2['p_def'] =(np.random.rand(df_state2.shape[0])*0.1)+0.3
    
    fig_div = create_plot(df_state2) 
    p = 0.3238543
    fig_div2 = plot2(p)    
    
    with open("templates/plot1.html", 'w') as f:
        f.write(html_string.format(fig_div,fig_div2))
    
    
    return render_template('plot1.html')


if __name__ == '__main__':
    app.run(debug=True)