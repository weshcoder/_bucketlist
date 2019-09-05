"""Importing flask for render temaplte and urlfor later"""
from flask import Flask, render_template

APP = Flask(__name__, static_url_path='/static')
@APP.route("/home")
def home():
    """Creating the route for home page"""
    return render_template("index.html")

@APP.route("/createbucket")
def bucket():
    """Creating the route for createbucket"""
    return render_template("createbucket.html")

@APP.route("/signup")
def signup():
    """Creating the route for signup"""
    return render_template("signup.html")

@APP.route("/signin")
def signin():
    """Creating the route for signin"""
    return render_template("signin.html")

@APP.route("/forgot")
def forgot():
    """Creating the route for forgot"""
    return render_template("forgot.html")

@APP.route("/resetpassword")
def reset():
    """Creating the route for resetpassword"""
    return render_template("resetpassword.html")

@APP.route("/editbucket")
def editbucket():
    """Cerating the route for editbucket"""
    return render_template("editbucket.html")

@APP.route("/items")
def items():
    """Creating the route for items"""
    return render_template("items.html")
    

if __name__ == '__main__':
    APP.run(debug=True, port=8000)
