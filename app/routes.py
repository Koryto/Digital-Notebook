from app import app
from flask import render_template

@app.route("/") # Root directory
@app.route("/index")
def index():
    return render_template("index.html")

#@app.route("/login")
#def login():
#    return render_template("login.html")