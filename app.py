from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define the path for storing uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file extension is allowed
def allowed_file(filename):
    allowed_extensions = {'txt', 'pdf', 'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file was submitted
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # If the user does not select a file, the browser will submit an empty file without a filename
    if file.filename == '':
        return redirect(request.url)

    # If the file exists and has an allowed extension, save it to the upload folder
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return 'File uploaded successfully.'

if __name__ == '__main__':
    app.run(debug=True)
