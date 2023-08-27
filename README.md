# PDF to Audio Converter

## Introduction

The "PDF to Audio Converter" is a web-based application that allows users to convert PDF documents into audio files. It is built using Python, Flask, JavaScript, HTML, and CSS, offering a seamless user experience.

---

## Technologies Used

### Backend
- **Python**: Core programming language.
- **Flask**: Web application framework.
- **PyPDF2**: Library for reading and manipulating PDF files.
- **gtts (Google Text-to-Speech)**: Text-to-speech conversion library.

### Frontend
- **HTML5**: Markup language for structuring the front end.
- **CSS**: Styling the HTML elements.
- **JavaScript**: Handling client-side functionalities like PDF preview.

---

## Features

### Current Features
1. **Upload PDF**: Users can upload PDF files through a simple web interface.
2. **PDF to Text**: Extracts text from the uploaded PDF files using PyPDF2.
3. **Text to Audio**: Converts the extracted text into audio format using Google's Text-to-Speech API.
4. **Download Audio**: Users can download the converted audio file.
5. **PDF Preview**: Provides a real-time preview of the uploaded PDF on the web interface.

### Additional Features to Consider
1. **Batch Processing**: Allow users to upload and process multiple PDF files simultaneously.
2. **Audio Customization**: Options to adjust the speed, pitch, and language of the audio.
3. **User Authentication**: Implement a user authentication system to allow personalized settings and history.
4. **Progress Bar**: Display a progress bar to indicate the conversion status.

---

## Setup and Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Run the application using `python run.py`.

---

## Future Work

- Improve the user interface for a more intuitive experience.
- Add a RESTful API for programmatic access to the service.
- Implement advanced features like audio customization and batch processing.

---

## Contact Information

For any queries or feedback, please feel free to contact me. 
