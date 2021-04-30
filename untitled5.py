import json, requests
foodName = 'watermelon'
apiKey = '9f8yGs19GGo5ExPpBj7fqjKOFlXXxkJdMyJKXwG3'
response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key={}&query={}'.format(apiKey, foodName))
data = json.loads(response.text)
    
x = data['totalHits']
y = data['foodSearchCriteria']['requireAllWords']
arr = ["Sugars","Energy","Vitamin A","Vitamin D","Protein","Fiber","Iron","Magnesium","Phosphorus","Cholestrol",
       "Vitamin C","Carbohydrate","Total lipid (fat)"]

"""
if x != 0:
    foodArr = data['foods'][0]['foodNutrients']
    print(foodName)
    for x in foodArr:
        if x['nutrientName'].split(',')[0] in arr:
            if(x['nutrientName'].split(',')[0]=="Total lipid (fat)"):
                print("Fat", ":", x['value'],x['unitName']) 
            else:    
                print(x['nutrientName'].split(',')[0], ":", x['value'],x['unitName'])
"""
foodArr = data['foods'][0]['foodNutrients']

print(json.dumps(foodArr, indent=2))
