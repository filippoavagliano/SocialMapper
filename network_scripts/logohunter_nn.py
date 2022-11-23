import os
import shutil


INPUT_FOLDER = "pictures"
OUTPUT_FOLDER = "output"


def logohunter_nn(profile):
    print('\nRiconoscimento di loghi e marche in corso\n')
    input_path = os.path.join(INPUT_FOLDER, profile)
    output_path = os.path.join(OUTPUT_FOLDER, profile, 'logohunter')

    logohunter_path = "logohunter/src/logohunter.py"
    brands_folder = "logohunter/data/test/logos"
    confidence = 0.50

    cmd = 'python ' + logohunter_path + ' --image --input_brands ' + brands_folder + ' --input_images ' + input_path \
          + ' --output ' + output_path + ' --outtxt  --confidence ' + str(confidence)

    print(cmd)

    os.system(cmd)

    print("Detection loghi completata")
