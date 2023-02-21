"""server side script"""
import json
import os
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import LogForm, LoginForm
from sqlman import Log, User

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

SECRET_KEY = os.urandom(32)
db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sasmad.db"
app.config["SECRET_KEY"] = SECRET_KEY
db.init_app(app)

oauth = OAuth(app)


# TODO make sure the form boolean is_admin is working when people are being added to the database
@app.route("/", methods=["POST", "GET"])
def home():
    # """sign up page for first time users"""
    # form = LoginForm(request.form)
    # if request.method == "POST" and form.validate_on_submit():
    #     email = request.form["email"]
    #     password = request.form["password"]
    #     # ADD INFORMATION TO THE DATABASE
    #     with app.app_context():
    #         user = User(email=email, password=password, is_admin=False)
    #         db.create_all()
    #         db.session.add(user)
    #         db.session.commit()
    #     # REDIRECT TO THE LOGIN PAGE TO VERIFY BEING ADDED TO THE DATABASE
    #     return render_template("login.html")
    return render_template("index.html")


@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """login page for returning users"""
#     # TODO check form input against database to verify if user has been created before allowing them to proceed to the main page
#     form = LoginForm(request.form)
#     # GET LOGIN DATA FROM THE FORM
#     if request.method == "POST" and form.validate_on_submit():
#         email = request.form["email"]
#         password = request.form["password"]
#         # CREATE QUERY TO SEARCH FOR USERS WITH SAME DETAILS
#         search_for_user_query = db.session.execute(
#             db.select(User).where(User.email == email and User.password == password)
#         ).scalars()
#         # CHECK QUERY RESULTS AGAINST LOGIN FORM DATA
#         with app.app_context():
#             # FORMAT RESULT TYPES AS DICTIONARY
#             query_results = [
#                 {"email": row.email, "password": row.password}
#                 for row in search_for_user_query
#             ]
#             if (
#                 query_results[0]["email"] == email
#                 and query_results[0]["password"] == password
#             ):
#                 return redirect(url_for("main_page"))
#             else:
#                 return render_template("login.html", form=form)

#     return render_template("login.html", form=form)


@app.route("/main")
def main_page():
    """page where you can input and login to view data"""
    # TODO input form with required data from the log class
    form = LogForm()
    return render_template("main_page.html", form=form)


@app.route("/password_recovery")
def forgot_password():
    """password recovery page"""
    # TODO create a function to recover password
    return render_template("password_recovery.html")


if __name__ == "__main__":
    app.run(debug=True)
