import io
import json
import os
import traceback

import requests
from PIL import Image
os_environ_ocr_url = os.environ.get('ocr_url')
if os_environ_ocr_url is None:
    raise Exception("Forgot to set up env")
from Ocr.ocr_result import OcrResult


def image_to_string(image: Image) ->OcrResult:

    try:
        buf = io.BytesIO()
        image.save(buf,format='PNG' )
        buf.seek(0)
        response = requests.post(f'{os_environ_ocr_url}/ocr', files=[('image', buf)])
        json_ob = json.loads(response.text)
        return  OcrResult(json_ob)

    except BaseException as e:
        traceback.print_exc()
        return None
