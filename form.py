from flask_wtf import FlaskForm, validators
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import SelectMultipleField, RadioField
from wtforms import HiddenField
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
    id_field = HiddenField("involved_sector")  ## Needed or no?
    name = StringField("Your Name:", validators=[DataRequired("Enter your name")])
    org_name = StringField("Name of Organization:", validators=[DataRequired("Enter the name of your organization")])
    country = StringField("Country:", validators=[DataRequired("Please enter the name of the country in which your organization exists")])
    role = StringField("Role:", validators=[DataRequired("Enter your job title or organizational role")])
    email = StringField("Email:", validators=[DataRequired("Enter a valid email address"), Email("Please entera valid email address")])
    phone = TelField("Phone Number:", validators=[DataRequired()])
    found = StringField("How you found BrightAct:")
    reason_list = [
        ('collaboration', 'collaboration'),
        ('information', 'information'),
        ('research', "research"),
        ('support', "support"),
        ('sales', "sales"),
        ('other', "other")
        ]
    # reason = SelectMultipleField(
    #     "Reason for Contact",
    #     choices=reason_list,
    #     coerce='unicode',
    #     option_widget=None)
    reason = RadioField("Reason for Contact:", choices=reason_list)
    info = RadioField("I want more information:", choices=[('1',"yes, please"), ('2','no thank you')])
    other = StringField("If 'Other', please specify: ")
    sector = RadioField("To which sector does your organization belong?:", choices=[('1', "NGO/Help"), ('2', "Public Sector"), ('3', "University"), ('4', "Civic/Law")])
    submit = SubmitField("Submit")

class NgoForm(FlaskForm):
    # NGO Details form fields
    target_group = StringField("What is your organization's target group? ", validators=[DataRequired("Please type a target group, i.e. students, staff, security")])
    branded_profile = RadioField("Are you interested in a branded profile for your organization in the app/website? ", choices=[('1',"yes, please"), ('2','no thank you')])
    # collab_options = [('1', 'Chat Functions'), ('2', 'Education'), ('3', 'Other Support'), ('4', 'Profile Page'), ('5', 'Network'),('6', 'Other')]
    collaboration = SelectMultipleField("What kind of collaboration are you interested in? ", choices=[('1', 'Chat Functions'), ('2', 'Education'), ('3', 'Other Support'), ('4', 'Profile Page'), ('5', 'Network'),('6', 'Other')])
    other = StringField("If 'Other', please specify: ")
    submit = SubmitField("Submit")


class CivForm(FlaskForm):
    # Civic Sector details
    support = RadioField("What kind of legal support does your firm have documented experience in? ", choices = [('1',"Domestic abuse or violence"), ('2', "Financial"), ('3', "Other")])
    offer = RadioField("What do we want to offer for the users? ", choices=[('1', "Free chat support"), ('2', "Pro bono cases"), ('3', "Other")])
    other1 = StringField("If 'Other', please specify: ")
    other2 = StringField("If 'Other', please specify: ")
    submit = SubmitField("Submit")


class PubForm(FlaskForm):
    # Public Sector details fields
    org_type = StringField("What kind of organization? (municipality, local government, government, police, legal etc)", validators=[DataRequired("Please share what type of organization you represent")])
    org_part = StringField("What part of the organization do you represent? ")
    branded_profile = RadioField("Are you interested in a branded profile for your organization in the app/website? ", choices=[('1',"yes, please"), ('2','no thank you')])
    submit = SubmitField("Submit")


class UnivForm(FlaskForm):
        # University details fields
        department = StringField("What department of the university? ", validators=[DataRequired("Please share the department within the University with which you are associated")])
        level = StringField("What is the level of your studies? ")
        research = RadioField("Is it for new or upcoming research? ", choices=[('yes', 'yes'), ('no', 'no')])
        branded_profile = RadioField("Are you interested in a branded profile for your organization in the app/website? ", choices=[('1',"yes, please"), ('2','no thank you')])

        submit = SubmitField("Submit")
