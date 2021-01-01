from flask import Flask

from ..config import Config
from flask import render_template



app = Flask(__name__)
app.config.from_object(Config)

#db = MongoEngine()
#db.init_app(app)



@app.route("/") # Root directory
@app.route("/index")
def index():
    return render_template("index.html")

#@app.route("/login")
#def login():
#    return render_template("login.html")