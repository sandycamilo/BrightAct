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

lst_of_hashes = gsheet.get_all_records()
print(lst_of_hashes)
row = ["Minimoni","BH","America","exampl@yahoo.com","78910"]
index = 3
gsheet.insert_row(row, index)