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
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

    return render_template('index.html')
