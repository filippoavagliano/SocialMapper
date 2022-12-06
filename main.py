import os
import schedule
import time
import download
from network_scripts import logohunter_nn, yolo_nn, carrec_nn, ocr_nn
from output_scripts import global_output
from emails_generation import generate_phishing_mail, generate_advertising_mail

INPUT_FOLDER = "pictures"
OUTPUT_FOLDER = "output"


def start_all():
    username = input('\nInserire username:\n')
    folder = os.path.join('pictures', username)
    pictures_folder = os.path.join(INPUT_FOLDER, username)
    output_folder = os.path.join(OUTPUT_FOLDER, username)

    if not os.path.exists(pictures_folder):
        os.mkdir(pictures_folder)

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    has_pictures = False

    while True:
        mode = input('Scaricamento da Instagram? y/n:\n')
        if mode.strip() == 'y':
            download.init_client()
            has_pictures = download.download_media(username)
            break
        elif mode.strip() == 'n':
            has_pictures = len(os.listdir(folder)) > 0
            break
        else:
            print('Inserire un valore valido\n')
            continue

    if has_pictures:
        yolo_nn.yolo_nn(username)
        carrec_nn.car_recognition_nn(username)
        ocr_nn.ocr_nn(username)
        logohunter_nn.logohunter_nn(username)
        global_output.generate_global_output(username)
        emails_folder = os.path.join(OUTPUT_FOLDER, username, 'emails')
        if not os.path.exists(emails_folder):
            os.mkdir(emails_folder)
        generate_phishing_mail.generate(username)
        generate_advertising_mail.generate(username)


schedule.every(3).hours.do(start_all)

start_all()
while True:
    schedule.run_pending()
    time.sleep(1)
