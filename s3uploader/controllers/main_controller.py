import os
import requests
import flask

from s3uploader.utils.presigned_url_generator import PresignedUrlGenerator

bp = flask.Blueprint('main_controller', __name__)


@bp.route('/')
def index() -> str:
    return flask.render_template('index.html')


@bp.route('/upload', methods=['POST'])
def upload_file() -> dict[str, str]:
    file = flask.request.files['file']
    presigned_url_generator = PresignedUrlGenerator(os.environ.get('BUCKET_NAME'), file.filename, 3600)

    presigned_url = presigned_url_generator.generate_post_url()
    files = {"file": file.stream}
    response = requests.post(presigned_url['url'], data=presigned_url['fields'], files=files)

    if response.status_code != 204:
        return {'message': response.reason}

    return {'message': 'File uploaded successfully!'}
