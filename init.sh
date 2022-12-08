#!/bin/bash

wget "https://drive.google.com/uc?id=1GSWFdeKqJS_Ic9vIiHcwLUxl4KigrnW_&export=download&confirm=t" -O "profiles.zip"
unzip profiles.zip

wget "https://drive.google.com/uc?id=1waqf1jVw6YCijKvbC7F2nK5u766zgXSe&export=download&confirm=t" -O "output.zip"
unzip output.zip

cd carrecognition
wget "https://drive.google.com/uc?id=1X51eVZPldjiLZDHxx2Zm6aY-kgQUmo4c&export=download&confirm=t" -O "models.zip"
unzip models.zip -d models

cd ../logohunter
mkdir data
cd data
wget "https://drive.google.com/uc?id=1TL-_zg81Ik3pqvM237wwYPEM1GjhjLL7&export=download&confirm=t" -O "data.zip"
unzip data.zip -d test

cd ../src
wget "https://drive.google.com/uc?id=13XjHDEIc3tYR9CenDUAbvZfKxovEy_58&export=download&confirm=t" -O "srcFile.zip"
unzip srcFile.zip

cd keras_yolo3
wget "https://drive.google.com/uc?id=13aahSd1Qxp69VDbUCWzge1hf7GwMUvXF&export=download&confirm=t" -O "keras_yolo_file.zip"
unzip keras_yolo_file.zip




