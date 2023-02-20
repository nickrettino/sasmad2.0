from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    DateTimeField,
    IntegerField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    """class for the login form"""

    email = StringField("email", validators=[Email()])
    password = PasswordField("password", validators=[Length(max=14), DataRequired()])
    submit = SubmitField(label="Log In")


class LogForm(FlaskForm):
    """form to input visitation data by user"""

    record_title = StringField("Record Title")
    last_name = StringField("Last Name")
    first_name = StringField("First Name")
    start_time = DateTimeField("Start Time")
    end_time = DateTimeField("End Time")
    time_in_minutes = IntegerField("Time In Minutes")
    type = SelectField(
        "Type",
        choices=[
            "Individual Visit",
            "Telephone Visit",
            "Group Visit",
            "Communion Visit",
        ],
    )
    communion = BooleanField("Communion")
    num_of_people = IntegerField("Number Of People")
    comments = TextAreaField("Comments")
