"""server side script"""
import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

SECRET_KEY = os.urandom(32)
db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sasmad.db"
app.config["SECRET_KEY"] = SECRET_KEY
db.init_app(app)


class LoginForm(FlaskForm):
    """class for the login form"""

    email = StringField("email", validators=[Email()])
    password = PasswordField("password", validators=[Length(max=14), DataRequired()])
    submit = SubmitField(label="Log In")


class User(db.Model):
    """model for all users email and passwords requires email and password attributes"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    is_admin = db.Column(db.Boolean)


class Log(db.Model):
    """model for all logs being handled by the database
    id, record_title, last_name, first_name, start_time, end_time, time in minutes,
    type, communion, num_of_people, comments
    """

    id = db.Column(db.Integer, primary_key=True, unique=True)
    record_title = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.Integer, nullable=False)
    time_in_minutes = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String, nullable=False)
    communion = db.Column(db.Boolean, nullable=False)
    num_of_people = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String, unique=True, nullable=False)


# ----------------------------- use this to remake the database if you need to ------------------#
# user = User(id=None, email=None, password=None, is_admin=None)
# log = Log(
#     id=None,
#     record_title=None,
#     last_name=None,
#     first_name=None,
#     start_time=None,
#     end_time=None,
#     time_in_minutes=None,
#     type=None,
#     communion=None,
#     num_of_people=None,
#     comments=None,
# )
# with app.app_context():
#     db.create_all()
#     db.session.add(user)
#     db.session.add(log)
#     db.session.commit()
# ------------------------------------------------------------------------------------------------#


# TODO fix information of form not going into he database
@app.route("/", methods=["POST", "GET"])
def sign_up():
    """sign up page for first time users"""
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        email = request.form["email"]
        password = request.form["password"]
        with app.app_context():
            user = User(email=email, password=password, is_admin=False)
            db.create_all()
            db.session.add(user)
            db.session.commit()
        return render_template("login.html")
    return render_template("index.html", form=form)


@app.route("/login")
def login():
    """login page for recurring users"""
    # TODO check form input against database to verify if user has been created before allowing them to proceed to the main page
    return render_template("login.html")


@app.route("/input")
def input_page():
    """page where you can input and login to view data"""
    # TODO input form with required data from the log class
    return render_template("main_page.html")


@app.route("/password_recovery")
def forgot_password():
    """password recovery page"""
    # TODO create a function to recover password
    return render_template("password_recovery.html")


if __name__ == "__main__":
    app.run(debug=True)
