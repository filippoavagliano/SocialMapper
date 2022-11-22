#!/bin/bash

python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --save-crop --save-txt --save-conf --source {elem.path} --project {OUTPUT_FOLDER} --name