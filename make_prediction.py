from image_preprocessing import preprocess_img_from_file
from class_names import create_presentable_labels, class_names
import numpy as np
import requests
from flask import jsonify

import os

# initialise list of class names that will be used later
labels = create_presentable_labels(class_names)
# reads environment variable that contains IP address of TF model server
API_ADDR = os.environ["API_ADDR"]


def make_presentable_predictions(preds: list[float]) -> dict[str, int]:
    """
        Model server returns prediction if form of List that contains prediction probability for each class.
        This function converts top 5 prediction and return them in form of dict that contains probabilities as percentage.

        Params:
            preds (List) - List of prediction probabilities from TF model server
        Returns:
            presentable_predictions (Dict) - Dictionary that contains labels as keys and prediction probabilities as values
    """
    preds = np.array(preds)
    top_5 = preds.argsort()[-5:]
    presentable_predictions = {}
    for pred in top_5:
        presentable_predictions[labels[pred]] = round(preds[pred] * 100)

    return presentable_predictions


def predict(filename):
    """
        Takes path to file and send preprocessed image to TF model server and returns top 5 predictions in json format.

        Params:
            filename (str) - Path to an image that should be used in prediction
        Returns:
            presentable_preds(JSON) - Top 5 predictions in JSON format
    """
    arr_image = preprocess_img_from_file(filename)
    api = f"http://{API_ADDR}/v1/models/food_detector:predict"
    data = {
        "instances": [arr_image]
    }
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    predictions = requests.post(api, json=data, headers=headers).json()
    presentable_preds = make_presentable_predictions(predictions['predictions'][0])
    print(presentable_preds)
    return jsonify(presentable_preds)
