import numpy as np
import pandas as pd
from io import BytesIO
from flask import Flask, request, render_template, send_file, redirect, url_for
from clarifai.rest import ClarifaiApp
import json, requests
import matplotlib.pyplot as plt
import seaborn as sns
import os

app=Flask(__name__)

"""
@app.route('/')
def home():
    return render_template("index.html")


app.config["IMAGE_UPLOADS"] = "C:\\Users\\LemonNitz\\Desktop\\Nutrition Assistant Manager\\static"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG","JPG","PNG","GIF"]

def allowed_images(filename):
    if not "." in filename:
        return False
    
    ext = filename.rsplit("." ,1)[1]
    
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSION"]:
        return True
    else:
        return False


@app.route("/display", methods=["POST","GET"])
def display_img():
    if request.method == "POST":
        if request.files:
            image = request.files["file"]
            if image.filename == "":
                print("NO FILENAME")
                return redirect(request.url)
            if allowed_images(image.filename):
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
                print("image saved")
                # For final model cut and paste [1] here and us response = model.predict_by_url(image.filename)
                return redirect(request.url)
            else:
                print("Wrong File Type")
                return redirect(request.url)
    return render_template("login.html")
app=Flask(__name__)
"""
# [1]
app1=ClarifaiApp(api_key='e56af53f775c4f98ac8c4694a6ce093d')
model = app1.public_models.general_model
response = model.predict_by_url(
    url='https://st.depositphotos.com/1102480/1589/i/950/depositphotos_15890699-stock-photo-big-hamburger.jpg')
concepts = response['outputs'][0]['data']['concepts']
arr = ["Sugars","Energy","Vitamin A","Vitamin D","Protein","Fiber","Iron","Magnesium","Phosphorus","Cholestrol",
       "Vitamin C","Carbohydrate","Total lipid (fat)"]

for concept in concepts:
    apiKey = '9f8yGs19GGo5ExPpBj7fqjKOFlXXxkJdMyJKXwG3'
    foodName = concept['name']
    response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key={}&query={}'.format(apiKey, foodName))
    data = json.loads(response.text)
    
    x = data['totalHits']
    y = data['foodSearchCriteria']['requireAllWords']
    if x != 0 and concept['value']>0.99:
        foodArr = data['foods'][0]['foodNutrients']
        print(foodName)
        for x in foodArr:
            if x['nutrientName'].split(',')[0] in arr:
                if(x['nutrientName'].split(',')[0]=="Total lipid (fat)"):
                    print("Fat", ":", x['value'],x['unitName']) 
                else:    
                    print(x['nutrientName'].split(',')[0], ":", x['value'],x['unitName'])
        print("--------------------")
    else:
        break

# [1]
    
"""
if __name__=='__main__':
    app.run(debug = True)
"""
