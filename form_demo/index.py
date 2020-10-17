import os
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
# config
# app.run('host'=localhost, debug=True)
# app.config.from_pyfile('config.py')

@app.route('/')
def landing_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.eviron.get('PORT', 5000))
