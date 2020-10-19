import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, flash, redirect
from form import ContactForm, GetInvolvedForm
from form import UnivForm, CivForm, NgoForm, PubForm
from flask_mail import Message, Mail
from flask_bootstrap import Bootstrap

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

@app.route('/about')
def about_page():
    return render_template('about_page.html')

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
            print("**** Validate False ****")
            print(form.errors)
            return render_template('get_involved.html', form=form)
        else:
            msg = Message(subject="Get Involved Form",
                        sender=form.name.data,
                        recipients=[os.getenv('MAIL_USERNAME')])
            sector = str(form.sector.data)
            print("---------")
            print(form.name.data, form.org_name.data)
            print(form.country.data, form.role.data)
            print("----------")
            msg.body = """
            From: %s <%s>
            %s %s %s %s %s %s
            """ % (form.name.data, form.org_name.data, form.country.data, form.role.data, form.email.data, form.found.data, form.reason.data, form.info.data)

            mail.send(msg)
            print("Sector:", sector)
            flash('Submitted Successfully')
            if sector == '1':
                return redirect('/ngo_details')
            elif sector == '2':
                return redirect('/pub_details')
            elif sector == '3':
                return redirect('/uni_details')
            elif sector == '4':
                return redirect('/civ_details')
            else:
                return redirect('/')

    elif request.method == 'GET':
        return render_template('get_involved.html', form=form)


@app.route('/ngo_details', methods=['GET', 'POST'])
def ngo_details():
    form = NgoForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('ngo_details.html', form=form)
        else:
            msg = Message(subject="Get Involved - NGO Details",
                        sender=form.name.data,
                        recipients=[os.getenv('MAIL_USERNAME')])
            sector = str(form.sector.data)
            # One %s per data field!
            msg.body = """
            From: %s <%s>
            %s %s
            """ % (form.branded_profile.data, form.target_group.data, form.collaboration.data, form.other.data)

            mail.send(msg)
            print("Sector:", sector)
            flash('Submitted Successfully')

            return redirect('/')

    elif request.method == 'GET':
        return render_template('ngo_details.html', form=form)


@app.route('/pub_details', methods=['GET', 'POST'])
def pub_details():
    form = PubForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('pub_details.html', form=form)
        else:
            msg = Message(subject="Get Involved - Public Sector Details",
                        sender=form.name.data,
                        recipients=[os.getenv('MAIL_USERNAME')])
            sector = str(form.sector.data)
            # One %s per data field!
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.form_field.data)
            # replace form_field with actual name of the form fields, seperate each with a comma

            mail.send(msg)
            flash('Submitted Successfully')

            return redirect('/')

    elif request.method == 'GET':
        return render_template('pub_details.html', form=form)


@app.route('/uni_details', methods=['GET', 'POST'])
def uni_details():
    form = UnivForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('uni_details.html', form=form)
        else:
            msg = Message(subject="Get Involved - University Details",
                        sender=form.name.data,
                        recipients=[os.getenv('MAIL_USERNAME')])
            sector = str(form.sector.data)
            # One %s per data field! <<<<<<
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.form_field.data)
            # replace form_field with actual name of the form fields, seperate each with a comma

            mail.send(msg)
            print("Sector:", sector)
            flash('Submitted Successfully')

            return redirect('/')

    elif request.method == 'GET':
        return render_template('uni_details.html', form=form)


@app.route('/civ_details', methods=['GET', 'POST'])
def civ_details():
    form = CivForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('civ_details.html', form=form)
        else:
            msg = Message(subject="Get Involved - Civic Sector Details",
                        sender=form.name.data,
                        recipients=[os.getenv('MAIL_USERNAME')])
            # One %s per data field!
            msg.body = """
            From: %s <%s>
            %s %s
            """ % (form.form_field.data)
            # ^^ change this to current data fields ^^
            # replace form_field with actual name of the form fields, seperate each with a comma

            mail.send(msg)
            print("Sector:", sector)
            flash('Submitted Successfully')

            return redirect('/')

    elif request.method == 'GET':
        return render_template('civ_details.html', form=form)

# wtf ... comment to push new changes

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.eviron.get('PORT', 5000))
