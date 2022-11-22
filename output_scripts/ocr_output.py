import os
import json


def ocr_user_output(ocr_output_path):
    words_array = []
    for elem in os.scandir(ocr_output_path):
        json_file = open(elem.path)
        data = json.load(json_file)
        for word in data:
            words_array.append(word['text'])
    return words_array


