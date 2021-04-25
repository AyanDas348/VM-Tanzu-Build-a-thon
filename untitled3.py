from flask import Flask
import requests
import json

apiKey = '9f8yGs19GGo5ExPpBj7fqjKOFlXXxkJdMyJKXwG3'
foodName = "burger"
response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key={}&query={}'.format(apiKey, foodName))

#print(type(response))
data = json.loads(response.text)
concepts = data['foods'][0]['foodNutrients']
arr = ["Sugars","Energy","Vitamin A","Vitamin D","Protein","Fiber","Iron","Magnesium","Phosphorus","Cholestrol",
       "Vitamin C","Carbohydrate","Total lipid (fat)"]
for x in concepts:
    if x['nutrientName'].split(',')[0] in arr:
        if(x['nutrientName'].split(',')[0]=="Total lipid (fat)"):
            print("Fat", ":", x['value'],x['unitName']) 
        else:    
            print(x['nutrientName'].split(',')[0], ":", x['value'],x['unitName'])


"""
@app.route('/')
def hello():
    return  "hello"

if __name__=='__main__':
    app.run(debug=True)
    
"""