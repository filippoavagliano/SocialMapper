import os
import json
from output_scripts.ocr_output import ocr_user_output
from output_scripts.yolo_output import yolo_user_output
from output_scripts.carrec_output import car_recognition_output
from output_scripts.logohunter_output import logohunter_output

OUTPUT_FOLDER = "output"


def generate_global_output(profile):
    output_path = os.path.join(OUTPUT_FOLDER, profile)
    print(f'\nGenero output per il profilo {profile}')
    json_path = os.path.join(output_path, "result.json")
    result_dict = {}
    for res_folder in os.scandir(output_path):
        if res_folder.name == "yolo":
            object_dict = yolo_user_output(res_folder.path)
            result_dict['yolo'] = object_dict
        elif res_folder.name == "car_rec":
            car_dict = car_recognition_output(res_folder.path)
            result_dict['car_recognition'] = car_dict
        elif res_folder.name == "logohunter":
            logo_dict = logohunter_output(res_folder.path)
            result_dict['logohunter'] = logo_dict
            pass
        elif res_folder.name == "ocr":
            ocr_dict = ocr_user_output(res_folder.path)
            result_dict['ocr'] = ocr_dict
    # print(result_dict)

    with open(json_path, "w") as outfile:
        json.dump(result_dict, outfile, ensure_ascii=False)

    print('Generazione output completata')
