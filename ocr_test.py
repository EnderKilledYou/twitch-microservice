import os

import pytest
import json

import requests

os_environ_ocr_url_ = os.environ.get('ocr_url')

from app import app


@pytest.fixture(scope='module')
def client():
    flask_app = app
    testing_client = app.test_client()
    yield requests.session()


def test_image_upload(client: requests.Session):
    """Make image upload works."""
    with open('test_image.png', 'rb') as test_image:

        response = client.post(f'{os_environ_ocr_url_}/ocr?testing=1', files=[('image', test_image)])
        assert response.status_code == 200
        json_obj = None
        try:
            json_obj = json.loads(response.text)
        except:
            pass
        assert json_obj is not None
        assert 'success' in json_obj
        assert 'event' in json_obj
        assert 'error_message' in json_obj
        assert 'text' in json_obj
        assert json_obj['success']
        assert len(json_obj['event']) == 1
        assert json_obj['event'][0] == 'google'
