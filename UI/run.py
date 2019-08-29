from flask import Flask
from flask import render_template
app = Flask(__name__, static_url_path='/static')
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/createbucket")
def bucket():
    return render_template("createbucket.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/signin")
def signin():
    return render_template("signin.html")
@app.route("/forgot")
def forgot():
    return render_template("forgot.html")
@app.route("/resetpassword")
def reset():
    return render_template("resetpassword.html")
@app.route("/editbucket")
def editbucket():
    return render_template("editbucket.html")
@app.route("/items")
def items():
    return render_template("items.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
