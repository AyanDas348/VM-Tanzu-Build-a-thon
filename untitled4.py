# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:28:50 2021

@author: LemonNitz
"""

import requests
import json

apiKey = '9f8yGs19GGo5ExPpBj7fqjKOFlXXxkJdMyJKXwG3'
foodName = "170150"
response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key={}&query={}'.format(apiKey, foodName))

#print(type(response))
data = json.loads(response.text)
print(json.dumps(data, indent=2))