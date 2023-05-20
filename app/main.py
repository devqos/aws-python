import logging
import requests
import os
from flask import Flask, request, render_template

from presigned_url_generator import generate_presigned_url

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.DEBUG)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    presigned_url = generate_presigned_url(os.environ.get('VARIABLE_NAME'), file.filename, 3600)
    files = {"file": file.stream}
    response = requests.post(presigned_url['url'], data=presigned_url['fields'], files=files)

    if response.status_code != 204:
        app.logger.error(f"Error code: {response.status_code},\nError message: {response.text}")
        return {'message': response.reason}

    return {'message': 'File uploaded successfully!'}
