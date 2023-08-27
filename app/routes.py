from flask import render_template, request, send_file
from app import app
import PyPDF2
from gtts import gTTS
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    download_link = None  # Initialize the download link
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        if pdf_file:
            # Read PDF
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            # Convert text to audio
            # Specify the absolute or relative path to your static directory
            static_dir = os.path.join(os.getcwd(), 'app', 'static')  
            audio_file_path = os.path.join(static_dir, 'output.mp3')
            tts = gTTS(text)
            tts.save(audio_file_path)

            print("File uploaded and processed")  # Debug print

            # Create a download link
            download_link = f"/static/output.mp3"
            print(f"Download link: {download_link}")  # Debug print

    return render_template('index.html', download_link=download_link)
