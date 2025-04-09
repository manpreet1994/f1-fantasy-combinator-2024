import os
import os.path
from config import PREDICTION_PATH, PREDICTION_HTML_PATH
from utils import read_json
from webpages.convert_predictions_to_html import convert_prediction_to_html
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--race_no")
args = parser.parse_args()
prediction_filepath = os.path.join(PREDICTION_PATH, f"race_{args.race_no}_predictions.json")

if os.path.exists(prediction_filepath):
    prediction_json = read_json(prediction_filepath)
    ## create html
    html_content = convert_prediction_to_html(prediction_json, args.race_no)
    ## save html
    file_name = f"race_{args.race_no}_predictions.html"
    prediction_html_filepath = os.path.join(PREDICTION_HTML_PATH, file_name)

    with open(prediction_html_filepath, 'wb+') as f:
        f.write(html_content.encode())

else:
    print(f"Prediction for race {args.race_no} do not exists")

