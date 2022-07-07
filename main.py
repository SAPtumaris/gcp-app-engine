from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the index page"

@app.route("/hi")
def who():
    return "who are you"