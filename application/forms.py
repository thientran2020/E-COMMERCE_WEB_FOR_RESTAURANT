from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email       = StringField("Email", validators=[DataRequired(), Email()])
    password    = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=30)])
    submit      = SubmitField("Login")

class RegisterForm(FlaskForm):
    email               = StringField("Email", validators=[DataRequired(), Email()])
    password            = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=30)])
    password_confirm    = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=30), EqualTo('password')])
    username            = StringField("Username", validators=[DataRequired(), Length(min=2, max=30)])
    submit              = SubmitField("Register Now")  
