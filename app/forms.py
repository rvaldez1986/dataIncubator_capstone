# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:52:08 2020

@author: rober
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DecimalField, BooleanField
from wtforms.validators import DataRequired, Length, Email




class ContactForm(FlaskForm):
    """Contact form."""

    input1 = DecimalField('Annual Income', [DataRequired()])
    input2 = DecimalField('Employment Length', [DataRequired()])
    input3 = DecimalField('Loan Amount', [DataRequired()])
    input4 = BooleanField('Home Ownership?', [])
    input5 = BooleanField('Debt?', [])
    input6 = DecimalField('GDP per Capita', [DataRequired()])
    input7 = DecimalField('Gini Coeficcient', [DataRequired()])
    input8 = DecimalField('Cost of Living', [DataRequired()])
    input9 = DecimalField('HDI', [DataRequired()])
    submit = SubmitField('Submit')