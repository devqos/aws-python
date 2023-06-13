import os
from typing import IO, Any

from flask import (
    Blueprint, render_template, request
)
from requests import Response, post
from werkzeug.datastructures import FileStorage

from .presigned_url_generator import PresignedUrlGenerator

bp = Blueprint('main_controller', __name__)


@bp.route('/')
def index() -> str:
    return render_template('index.html')


@bp.route('/upload', methods=['POST'])
def upload_file() -> dict[str, str]:
    file: FileStorage = request.files['file']
    presigned_url_generator = PresignedUrlGenerator(os.environ.get('BUCKET_NAME'), file.filename, 3600)

    presigned_url: dict[str, Any] = presigned_url_generator.generate_post_url()
    files: dict[str, IO[bytes]] = {"file": file.stream}
    response: Response = post(presigned_url['url'], data=presigned_url['fields'], files=files)

    if response.status_code != 204:
        return {'message': response.reason}

    return {'message': 'File uploaded successfully!'}
