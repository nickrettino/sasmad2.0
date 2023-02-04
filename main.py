"""server side script"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sasmad.db"

db.init_app(app)


class User(db.Model):
    """model for all users email and passwords requires email and password attributes"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)


class Log(db.Model):
    """model for all logs being handled by the database
    id, record_title, last_name, first_name, start_time, end_time, time in minutes, type, communion, num_of_people, comments
    """

    id = db.Column(db.Integer, primary_key=True, unique=True)
    record_title = db.Column(db.String, unique=True, Nullable=False)
    last_name = db.Column(db.String, unique=True, Nullable=False)
    first_name = db.Column(db.String, unique=True, Nullable=False)
    start_time = db.Column(db.String, unique=True, Nullable=False)
    end_time = db.column(db.Integer, unique=True, nullable=False)
    time_in_minutes = db.column(db.Integer, unique=True, nullable=False)
    type = db.Column(db.String, unique=True, Nullable=False)
    communion = db.Column(db.Boolean, unique=False, nullable=False)
    num_of_people = db.Column(db.Integer, unique=True, nullable=False)
    comments = db.Column(db.String, unique=True, Nullable=False)


class Admin(db.Model):
    """used for admin access to view and query all the data in the database
    id,email,password"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)


user = User()
log = Log()
admin = Admin()
with app.app_context():
    db.create_all()
    db.session.add(user)
    db.session.add(log)
    db.session.add(admin)
    db.session.commit()


@app.route("/", methods=["GET"])
def sign_up():
    """sign up page for first time users"""

    if request.method == "GET":
        email = request.signup_form["email"]
        password = request.signup_form["password"]

    return render_template("index.html")


@app.route("/login")
def login():
    """login page for recurring users"""
    return render_template("login.html")


@app.route("/input")
def input_page():
    """page where you can input and login to view data"""
    return render_template("main_page.html")


@app.route("/password_recovery")
def forgot_password():
    """password recovery page"""
    return render_template("password_recovery.html")


if __name__ == "__main__":
    app.run(debug=True)
