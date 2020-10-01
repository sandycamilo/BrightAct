# import os
# from dotenv import load_dotenv
# load_dotenv()

from flask import Flask, render_template, request, flash, jsonify, request, abort
from form import ContactForm
from flask_mail import Message, Mail
# Google Sheets API setup
import gspread
from oauth2client.sevice_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds"]
credential = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
                                                              
client = gspread.authorize(credential)
gsheet = client.open("BrightAct Get Involved Form").sheet1

lst_of_hashes = gsheet.get_allrecords()
print(lst_of_hashes)