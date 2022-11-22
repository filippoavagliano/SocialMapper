import os

INPUT_FOLDER = "pictures"
OUTPUT_FOLDER = "output"

def carrecognition_nn(profile):
    print('Lettura del testo nelle immagini\n')
    input_path = os.path.join(OUTPUT_FOLDER, profile, 'yolo', 'crops', 'car')
    print(input_path)
    output_path = os.path.join(OUTPUT_FOLDER, profile, 'car_rec')
    
    print('\n')
   
    if not os.path.exists(input_path):
        print('Non ci sono automobili per il profilo {}'.format(profile))
    else:
    
        demo_path = "carrecognition/demo.py"
    
        cmd = 'python '+demo_path+' --input_images '+ input_path +' --output_folder '+output_path

        os.system(cmd)
        print("Riconoscimento auto terminato!")
        #!python demo.py --input_images {yolo_cars_folder} --output_folder {OUTPUT_FOLDER}/{elem.name}/carrecognition