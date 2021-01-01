from flask import Flask, request, jsonify, render_template

from ..config import Config
from .user import User
from .database import session


app = Flask(__name__)
app.config.from_object(Config)





@app.route("/") # Root directory
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        input_data = request.get_json(force=True)
        user = User(
            email = input_data['email'],
            city = input_data['city']
        )
        
        session.add(user)
        session.commit()
        return render_template("index.html")