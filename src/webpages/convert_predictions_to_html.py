import os
from config import UI_NAME_DICT
from . import template_content
import jinja2
from jinja2 import Environment, FileSystemLoader, Template
label_list = ["driver_1", "driver_2", "driver_3", "driver_4", "driver_5", "team_1", "team_2", "two_x_driver"]

def convert_prediction_to_html(prediction_json, race_no):
    
    template = jinja2.Template(template_content)

    #Data dictionary to be supplied to our HTML file.
    input_dict = {}
    for label,content in zip(label_list, prediction_json["prediction"]):
        input_dict[label] = UI_NAME_DICT[content]
    input_dict["two_x_driver"] = UI_NAME_DICT[prediction_json["2x_driver"]]
    input_dict["race_no"] = race_no
    input_dict["race_name"] = prediction_json["race_name"]

    output = template.render(input_dict)
    return output


