#!/bin/bash
cd carrecognition
wget "https://drive.google.com/uc?id=12deopnyKW8ZCX9cFCS3Ov_uPVfOO1qEf&export=download&confirm=t" -O "models.zip"
unzip models.zip -d models

cd ../logohunter
wget "https://drive.google.com/uc?id=13NDUmo8FJv-HMYBzwj1twKxnvcDXbD92&export=download&confirm=t
" -O "data.zip"
unzip data.zip -d data

cd src
wget "https://drive.google.com/uc?id=13XjHDEIc3tYR9CenDUAbvZfKxovEy_58&export=download&confirm=t" -O "srcFile.zip"
unzip srcFile.zip

cd keras_yolo3
wget "https://drive.google.com/uc?id=13aahSd1Qxp69VDbUCWzge1hf7GwMUvXF&export=download&confirm=t" -O "keras_yolo_file.zip"
unzip keras_yolo_file.zip






