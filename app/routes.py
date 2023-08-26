from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        if pdf_file:
            # For now, let's just print the name of the uploaded file
            print(f"Uploaded file: {pdf_file.filename}")

    return render_template('index.html')
