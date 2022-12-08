import os
import json
import easyocr

INPUT_FOLDER = "profiles"
OUTPUT_FOLDER = "output"

reader = easyocr.Reader(['en', 'it'])


def ocr_nn(profile):
    print('\nLettura del testo nelle immagini')
    input_path = os.path.join(INPUT_FOLDER, profile)
    output_path = os.path.join(OUTPUT_FOLDER, profile, 'ocr')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    for picture in os.scandir(input_path):
        filename, file_extension = os.path.splitext(picture.name)
        if file_extension in ['.jpg', '.jpeg', '.png']:
            image_result = reader.readtext(picture.path, detail=1)
            if image_result:
                json_path = os.path.join(output_path, filename + '.json')
                result_json = []
                for text_elem in image_result:
                    text_obj = {
                        'text': text_elem[1],
                        'confidence': text_elem[2]
                    }
                    result_json.append(text_obj)
                with open(json_path, "w") as outfile:
                    json.dump(result_json, outfile, ensure_ascii=False)
    print('OCR profilo {} completato'.format(profile))
