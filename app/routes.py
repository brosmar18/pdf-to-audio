from flask import render_template, request
from app import app
import PyPDF2
from gtts import gTTS
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        if pdf_file:
           # Read PDF


    return render_template('index.html')
