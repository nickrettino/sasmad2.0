"""server side script"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def sign_up():
    """login page"""
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/input")
def input_page():
    return render_template("main_page.html")


if __name__ == "__main__":
    app.run(debug=True)
