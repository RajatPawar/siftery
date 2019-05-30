from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(FlaskForm):
    email      = StringField("Email", validators=[DataRequired()])
    password   = PasswordField('Password', validators=[DataRequired()])
    interests = StringField("Enter your domain, interests or profession keywords separated by a comma", validators=[DataRequired()])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email      = StringField("Use your existing email", validators=[DataRequired()])
    password   = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
