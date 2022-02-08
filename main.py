import flask
from flask import request
import requests
import shutil
from utils import get_file_extension
from make_prediction import predict

app = flask.Flask("food_detector_api")


@app.route('/test', methods=['GET'])
def image_via_file():
    return predict("image.jpg")


@app.route('/url', methods=['GET'])
def image_via_url():
    """
        This route predicts the image sent as url.
    """
    url = request.args.get("url")
    extension = get_file_extension(url)
    filename = f"user_image{extension}"
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        return predict(filename)

    else:
        return "Failed to download the image"


@app.route('/local', methods=['POST'])
def image_from_local_storage():
    """
        This route predicts image sent as file with application/multipart HTTP request
    """
    if request.files["file"]:
        file = request.files["file"]
        ext = get_file_extension(request.form.get("name"))
        filename = "user_image" + ext
        file.save(filename)

        return predict(filename)


app.run(port=6000, host='0.0.0.0')
