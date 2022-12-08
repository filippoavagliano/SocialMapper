wget "https://drive.google.com/uc?id=1GSWFdeKqJS_Ic9vIiHcwLUxl4KigrnW_&export=download&confirm=t" -O "profiles.zip"
tar -xf profiles.zip

wget "https://drive.google.com/uc?id=1waqf1jVw6YCijKvbC7F2nK5u766zgXSe&export=download&confirm=t" -O "output.zip"
tar -xf output.zip

mkdir carrecognition\models
wget "https://drive.google.com/uc?id=1X51eVZPldjiLZDHxx2Zm6aY-kgQUmo4c&export=download&confirm=t"  -O "carrecognition/models.zip"
tar -xf carrecognition\models.zip -C carrecognition\models

mkdir logohunter\data
mkdir logohunter\data\test
wget "https://drive.google.com/uc?id=1TL-_zg81Ik3pqvM237wwYPEM1GjhjLL7&export=download&confirm=t"  -O "logohunter/data.zip"
tar -xf logohunter\data.zip -C logohunter\data\test

wget "https://drive.google.com/uc?id=13XjHDEIc3tYR9CenDUAbvZfKxovEy_58&export=download&confirm=t"  -O "logohunter/src/srcFile.zip"
tar -xf logohunter\src\srcFile.zip -C logohunter\src

wget "https://drive.google.com/uc?id=13aahSd1Qxp69VDbUCWzge1hf7GwMUvXF&export=download&confirm=t"  -O "logohunter/src/keras_yolo3/keras_yolo_file.zip"
tar -xf logohunter\src\keras_yolo3\keras_yolo_file.zip -C logohunter\src\keras_yolo3





