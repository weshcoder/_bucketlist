"""Importing flask for render temaplte and urlfor later"""
from flask import Flask, render_template
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, static_url_path='/static', instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    @app.route("/home")
    def home():
        """Creating the route for home page"""
        return render_template("index.html")

    @app.route("/createbucket")
    def bucket():
        """Creating the route for createbucket"""
        return render_template("createbucket.html")

    @app.route("/signup")
    def signup():
        """Creating the route for signup"""
        return render_template("signup.html")

    @app.route("/signin")
    def signin():
        """Creating the route for signin"""
        return render_template("signin.html")

    @app.route("/forgot")
    def forgot():
        """Creating the route for forgot"""
        return render_template("forgot.html")

    @app.route("/resetpassword")
    def reset():
        """Creating the route for resetpassword"""
        return render_template("resetpassword.html")

    @app.route("/editbucket")
    def editbucket():
        """Cerating the route for editbucket"""
        return render_template("editbucket.html")

    @app.route("/items")
    def items():
        """Creating the route for items"""
        return render_template("items.html")
    return app

if __name__ == '__main__':
    app.run(debug=True, port=8000)
