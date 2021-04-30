import os
from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

"""
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user=request.files["file"]
        return redirect(url_for("display", img=user))
    else:
        return render_template("login.html")
"""

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
                return redirect(request.url)
            else:
                print("Wrong File Type")
                return redirect(request.url)
    return render_template("login.html")

if __name__=='__main__':
    app.run(debug = True)
    


    