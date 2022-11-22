import schedule
import time
import download
from network_scripts import yolo_nn
from output_scripts import global_output


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
    
    yolo_nn(username)
    
    

schedule.every(3).hours.do(start_all)

start_all()
while True:
    schedule.run_pending()
    time.sleep(1)
