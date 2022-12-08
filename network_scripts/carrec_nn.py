import os

INPUT_FOLDER = "profiles"
OUTPUT_FOLDER = "output"


def car_recognition_nn(profile):
    print('\nRiconoscimento di automobili in corso\n')
    input_path = os.path.join(OUTPUT_FOLDER, profile, 'yolo', 'crops', 'car')
    output_path = os.path.join(OUTPUT_FOLDER, profile, 'car_rec')

    if not os.path.exists(input_path):
        print('Non ci sono automobili per il profilo {}'.format(profile))
    else:
        demo_path = "carrecognition/demo.py"
        cmd = 'python ' + demo_path + ' --input_images ' + input_path + ' --output_folder ' + output_path
        os.system(cmd)
        print("Riconoscimento auto terminato!")