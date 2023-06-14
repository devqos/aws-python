import os
import requests
import typing
import flask
import werkzeug.datastructures

from s3Uploader.s3UploaderUtils.presigned_url_generator import PresignedUrlGenerator

bp = flask.Blueprint('main_controller', __name__)


@bp.route('/')
def index() -> str:
    return flask.render_template('index.html')


@bp.route('/upload', methods=['POST'])
def upload_file() -> dict[str, str]:
    file: werkzeug.datastructures.FileStorage = flask.request.files['file']
    presigned_url_generator = PresignedUrlGenerator(os.environ.get('BUCKET_NAME'), file.filename, 3600)

    presigned_url: dict[str, typing.Any] = presigned_url_generator.generate_post_url()
    files: dict[str, typing.IO[bytes]] = {"file": file.stream}
    response: requests.Response = requests.post(presigned_url['url'], data=presigned_url['fields'], files=files)

    if response.status_code != 204:
        return {'message': response.reason}

    return {'message': 'File uploaded successfully!'}
