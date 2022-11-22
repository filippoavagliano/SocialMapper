# import the necessary packages
import json
import os
import random
import argparse

import cv2 as cv
import keras.backend as K
import numpy as np
import scipy.io

from utils import load_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument(
        "--input_images", type=str, default='input',
        help = "path to image directory or video to find logos in"
    )

    parser.add_argument(
        "--output_folder", type=str, default='input',
        help = "path to image directory or video to find logos in"
    )

    FLAGS = parser.parse_args()

    input_images = FLAGS.input_images
    output_folder = FLAGS.output_folder

    img_width, img_height = 224, 224
    model = load_model()
    model.load_weights('carrecognition/models/model.96-0.89.hdf5')

    cars_meta = scipy.io.loadmat('carrecognition/devkit/cars_meta')
    class_names = cars_meta['class_names']  # shape=(1, 196)
    class_names = np.transpose(class_names)

    # test_path = '/content/drive/MyDrive/SocialMapper/carrecognition/data/personal'
    test_path = input_images
    test_images = [f for f in os.listdir(test_path) if
                   os.path.isfile(os.path.join(test_path, f)) and f.endswith('.jpg')]
    
    num_samples = len(test_images)
    samples = random.sample(test_images, num_samples)
    results = []
    for i, image_name in enumerate(samples):
        filename = os.path.join(test_path, image_name)
        print('Start processing image: {}'.format(filename))
        bgr_img = cv.imread(filename)
        bgr_img = cv.resize(bgr_img, (img_width, img_height), cv.INTER_CUBIC)
        rgb_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2RGB)
        rgb_img = np.expand_dims(rgb_img, 0)
        preds = model.predict(rgb_img)
        prob = np.max(preds)
        class_id = np.argmax(preds)
        text = ('Predict: {}, prob: {}'.format(class_names[class_id][0][0], prob))
        results.append({'picture' : filename,'label': class_names[class_id][0][0], 'prob': '{:.4}'.format(prob)})
        cv.imwrite('images/{}_out.png'.format(i), bgr_img)

    print(results)
    if not os.path.exists(output_folder):
      os.mkdir(output_folder)
    with open(os.path.join(output_folder, 'results.json'), 'w') as file:
        json.dump(results, file, indent=4)

    K.clear_session()
