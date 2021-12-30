#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 16:54:13 2021

@author: knoldus
"""

import joblib
from flask import Flask,request
import json

app = Flask(__name__)

model = joblib.load(r'/home/knoldus/first_pdf')

@app.route('/predict',methods=['POST'])

def predict():
    event = json.loads(request.data)
    print(event)
    
    
if __name__ == '__main__':
    app.run(debug=True)