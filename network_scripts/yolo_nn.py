import os
import shutil
from yolov5 import detect as yolo

INPUT_FOLDER = "pictures"
OUTPUT_FOLDER = "output"



def yolo_nn(profile):
    
    print('Lettura del testo nelle immagini\n')
    input_path = os.path.join(INPUT_FOLDER, profile)
    output_path = os.path.join(OUTPUT_FOLDER, profile, 'yolo')
    
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    
    yolo.run(save_crop=True, save_txt=True, save_conf=True, source=input_path, project=OUTPUT_FOLDER, name=profile+"yolo")
    print("Object detection completato")
    
    
  
 

  