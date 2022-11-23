import schedule
import time
import download
from network_scripts import logohunter_nn, yolo_nn, carrec_nn, ocr_nn
from output_scripts import global_output
from emails_generation import generate_phishing_mail  # generate_advertising_mail


def start_all():
    username = input('Inserire username:\n')
    '''
    download.init_client()
    has_pictures = download.download_media(username)
    if has_pictures:
        ocr_nn.ocr_nn(username)
        global_output.generate_global_output(username)
    '''

    '''
    ocr_nn.ocr_nn(username)
    global_output.generate_global_output(username)
    
    '''

    yolo_nn.yolo_nn(username)
    carrec_nn.car_recognition_nn(username)
    ocr_nn.ocr_nn(username)
    logohunter_nn.logohunter_nn(username)
    global_output.generate_global_output(username)
    generate_phishing_mail.generate(username)


schedule.every(3).hours.do(start_all)

start_all()
while True:
    schedule.run_pending()
    time.sleep(1)
