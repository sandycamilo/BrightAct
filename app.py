import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, flash
from form import ContactForm, GetInvolvedForm
from flask_mail import Message, Mail

app = Flask(__name__)
mail = Mail()
# config
# app.run('host'=localhost, debug=True)
# app.config.from_pyfile('config.py')

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

@app.route('/get_involved', methods=['GET', 'POST'])
def get_involved():
    form = GetInvolvedForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('get_involved.html', form=form)
        else:
            msg = Message(subject="Get Involved Form",
                        sender=form.name.data,
                        recipients=[os.getenv('MAIL_USERNAME')])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.org_name.data, form.country.data, form.role.data, form.email.data, form.found.data, form.info.data)
            # removed:  form.reason.data, for debugging
            mail.send(msg)

            return render_template('get_involved.html', success=True)

    elif request.method == 'GET':
        return render_template('get_involved.html', form=form)

@app.route('/about')
def about_page():
    return render_template('about_page.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.eviron.get('PORT', 5000))
