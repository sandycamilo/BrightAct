from flask_wtf import FlaskForm, validators
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, DataRequired, ValidationError, Email

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Enter your name")])
    email = StringField("Email", validators=[DataRequired("Enter a valid email address"), Email("Please entera valid email address")])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")