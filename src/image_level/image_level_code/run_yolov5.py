"""
    기존 code on kaggle 과 다르게 새로운 코드 작성
    1. 기존 코드
        1. siim-covid-19-yolo-txt
        2. siim-covid-19 512 img png 600 study png
        3. yolov5 -1 yaml (config file)
        4. YOLOv5 Official v3.1 Dataset(yolo v5 model)

    2. 새 코드
        yolo 는 딱히 다를 부분은 없어보이고, 그대로 옮기면 되겠다.
"""

import numpy as np
import pandas as pd
from glob import glob
import shutil, os, sys
from sklearn.model_selection import GroupKFold
from tqdm.notebook import tqdm
import cv2
import wandb

competition_path = "/home/madquer/programming/kaggle/siim"
data_path = os.path.join(competition_path, 'data')
original_data_path = os.path.join(data_path, 'original_data')
resized_data_path = os.path.join(data_path, 'resized_data')
yolo_txt_path = os.path.join(data_path, 'yolotxt')
resized_data_path = os.path.join(resized_data_path, 'siim_512_img_png_600_study_png')
resized_data_study_path = os.path.join(resized_data_path, 'study')
resized_data_image_path = os.path.join(resized_data_path, 'image')



if __name__ == '__main__':
    print('yes')