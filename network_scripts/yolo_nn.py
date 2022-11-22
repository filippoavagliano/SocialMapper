import os
import shutil
from yolov5 import detect
import subprocess

INPUT_FOLDER = "pictures"
OUTPUT_FOLDER = "output"



def yolo_nn(profile):
    
    print('\nRiconoscimento degli oggetti in corso\n')
    input_path = os.path.join(INPUT_FOLDER, profile)
    output_path = os.path.join(OUTPUT_FOLDER, profile, 'yolo')
    
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    
    '''
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    '''
    
    #result = subprocess.run(["python", "detect.py","--save-crop","--save-txt", "--save-conf","--source", inputpath, ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #print(result.stdout)
    yolo_folder = os.path.join(profile,"yolo")
    detect_path = "yolov5/detect.py"
    
    cmd = 'python '+detect_path+' --save-crop --save-txt --save-conf --source '+ input_path +' --project '+OUTPUT_FOLDER+' --name '+yolo_folder

    os.system(cmd)
    
    
    #yolo.run(save_crop=True, save_txt=True, save_conf=True, source=input_path, project=OUTPUT_FOLDER, name=profile+"yolo")
    print("Object detection completato")
    
    
  
 

  