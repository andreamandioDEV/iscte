from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), Length(min=10, max=100)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=80)])
