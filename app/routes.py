from flask import render_template, request, send_file
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

            # Convert text to audio
            tts = gTTS(text)
            audio_file_path = os.path.join("static", "output.mp3")
            tts.save(audio_file_path)

             # Return audio file
            return send_file(audio_file_path, as_attachment=True, download_name="output.mp3")

    return render_template('index.html')
