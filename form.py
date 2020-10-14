from flask_wtf import FlaskForm, validators
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import SelectMultipleField, RadioField
from wtforms.validators import Required, DataRequired, ValidationError, Email
from wtforms.fields.html5 import TelField
from wtforms.widgets import Select

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Enter your name")])
    email = StringField("Email", validators=[DataRequired("Enter a valid email address"), Email("Please entera valid email address")])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")

class GetInvolvedForm(FlaskForm):
    name = StringField("Your Name:", validators=[DataRequired("Enter your name")])
    org_name = StringField("Name of Organization:", validators=[DataRequired("Enter the name of your organization")])
    country = StringField("Country:", validators=[DataRequired("Please enter the name of the country in which your organization exists")])
    role = StringField("Role:", validators=[DataRequired("Enter your job title or organizational role")])
    email = StringField("Email:", validators=[DataRequired("Enter a valid email address"), Email("Please entera valid email address")])
    phone = TelField("Phone Number:", validators=[DataRequired()])
    found = StringField("How you found BrightAct:")
    # reason_list = [
    #     ('collaboration', 'collaboration'),
    #     ('information', 'information'),
    #     ('research', "research"),
    #     ('support', "support"),
    #     ('sales', "sales"),
    #     ('other', "other")
    #     ]
    # reason = SelectMultipleField(
    #     "Reason for Contact",
    #     choices=reason_list,
    #     coerce='unicode',
    #     option_widget=None)
    reason = RadioField("Reason for Contact:", choices=[('1','collaboration'),('2','information'), ('3','research'), ('4','support'), ('5','sales'), ('6','other')])
    info = RadioField("I want more information:", choices=[("yes, please"), ('no thank you')])
    sector = RadioField("To which sector does your organization belong?:", choices=[("NGO/Help"), ("Public Sector"), ("University"), ("Civic/Law")], coerce="unicode")
    submit = SubmitField("Submit")

