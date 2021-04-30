from flask import Flask, render_template, request, redirect, url_for, session
import requests
import json
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'a'
app.config['MYSQL_HOST'] = "remotemysql.com" 
app.config["MYSQL_PORT"] = 3306
app.config['MYSQL_USER'] = "lypD47Dxuh" 
app.config['MYSQL_PASSWORD'] = "EATLsr4rTp"
app.config['MYSQL_DB'] = "lypD47Dxuh" 
mysql = MySQL(app)



@app.route('/')
def index():
    return  render_template('login.html')

@app.route('/login', methods = ["POST", "GET"])
def login():
    """
    Login page with username and password
    """
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        session['name'] = name
        session['password'] = password
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO user_details VALUES(NULL,% s, % s)',(name, password))
        mysql.connection.commit()
        return render_template("submission.html")
    else:
        return redirect(request.url)

@app.route('/submission', methods = ["POST", "GET"])
def submission():
    """
        Submission of data like images or just name of food for now
    """
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM user_details WHERE name=% s', (session['name']))
    mysql.connection.commit()
    account = cursor.fetchone()
    print(account)
    if request.method == "POST":
        return render_template("display.html", account = session['name'])
    else:
        return redirect(request.url)
@app.route('/display', methods = ["POST", "GET"])
def display():
    """
    Display page that displays nutritional value of input image of food name
    """
    if request.method == "POST":
        foodName = request.form['food']
        nutrients = {}
        USDAapiKey = '9f8yGs19GGo5ExPpBj7fqjKOFlXXxkJdMyJKXwG3'
        response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key={}&query={}&requireAllWords={}'.format(USDAapiKey, foodName, True))

        data = json.loads(response.text)
        concepts = data['foods'][0]['foodNutrients']
        arr = ["Sugars","Energy","Vitamin A","Vitamin D","Protein","Fiber","Iron","Magnesium","Phosphorus","Cholestrol",
               "Vitamin C","Carbohydrate","Total lipid (fat)"]
        for x in concepts:
            if x['nutrientName'].split(',')[0] in arr:
                if(x['nutrientName'].split(',')[0]=="Total lipid (fat)"):
                    nutrients['Fat'] = [x['value'], x['unitName']]
                else:    
                    nutrients[x['nutrientName'].split(',')[0]] = [x['value'], x['unitName']]
                    
        return render_template('display.html', x = foodName, data = nutrients)
    else:
        return render_template(request.url)        

if __name__=='__main__':
    app.run(debug=True)
    
