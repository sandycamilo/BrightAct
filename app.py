import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, flash, jsonify, request, abort
from form import ContactForm
from flask_mail import Message, Mail
# Google Sheets API setup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes)
                                                              
client = gspread.authorize(credentials)
gsheet = client.open("BrightAct Get Involved Form").sheet1

app = Flask(__name__)
mail = Mail()
# config
# app.run('host'=localhost, debug=True)
# app.config.from_pyfile('config.py')

lst_of_hashes = gsheet.get_all_records()
print(lst_of_hashes)

app.secret_key = os.getenv('SECRET_KEY')

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv('MAIL_USERNAME'),
    "MAIL_PASSWORD": os.getenv('MAIL_PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact_page.html', form=form)
        else:
            msg = Message(subject=form.subject.data, 
                        sender=form.name.data, 
                        recipients=[os.getenv('MAIL_USERNAME')])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact_page.html', success=True)

    elif request.method == 'GET':
        return render_template('contact_page.html', form=form)

@app.route('/about')
def about_page():
    return render_template('about_page.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.eviron.get('PORT', 5000))
