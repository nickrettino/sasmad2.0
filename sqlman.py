from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
