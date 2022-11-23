import os
import json


def car_recognition_output(carrec_output_path):
    car_output_path = os.path.join(carrec_output_path, 'results.json')
    json_file = open(car_output_path)
    data = json.load(json_file)
    return data
