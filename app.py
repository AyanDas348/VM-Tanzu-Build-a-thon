import numpy as np
import pandas as pd
from io import BytesIO
from flask import Flask, request, render_template, send_file
from clarifai.rest import ClarifaiApp
import json
import matplotlib.pyplot as plt
import seaborn as sns


app=Flask(__name__)
app1=ClarifaiApp(api_key='e56af53f775c4f98ac8c4694a6ce093d')

model = app1.public_models.general_model
response = model.predict_by_url(
    url='https://st.depositphotos.com/1102480/1589/i/950/depositphotos_15890699-stock-photo-big-hamburger.jpg')
print(json.dumps(response, indent=2))
    
"""
@app.route('/graph_pie/')
def graph_pie():
    model = app1.public_models.general_model
    response = model.predict_by_url(
        url='https://st.depositphotos.com/1102480/1589/i/950/depositphotos_15890699-stock-photo-big-hamburger.jpg')
    

@app.route('/')
def hello():
    return render_template('index.html')
        

if __name__=='__main__':
    app.run(debug = True)
"""
