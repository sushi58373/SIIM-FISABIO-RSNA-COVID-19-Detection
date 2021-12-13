# SIIM-FISABIO-RSNA-COVID-19-Detection
![header](https://user-images.githubusercontent.com/62593594/145750150-c6645ba1-128f-44a4-a660-26f3e0935870.png)  
Source code of the 73th / 1305(6%) place solution for [SIIM-FISABIO-RSNA COVID-19 Detection Challenge](https://www.kaggle.com/c/siim-covid19-detection).  

[SIIM COVID LEADERBOARD](https://www.kaggle.com/c/siim-covid19-detection/leaderboard)

---  

## 1. ENVIRONMENT  
---  
* HARDWARE : RTX 3070 8GB VRAM / kaggle docker GPU (P100-16GB) & TPU v3.8 (16GB x 8core)
* Ubuntu 20.04.2 LTS  
* CUDA 11.3  
* Python 3.7.9  

---  

## 2. DATASET  
---  
1. SIIM COVID 19 DATASET  
* download competition dataset at [link](https://www.kaggle.com/c/siim-covid19-detection/data)  
```
$ kaggle competitions download -c siim-covid19-detection # kaggle API
```
128GB  

---
## 3. SOLUTION SUMMARY
### 3.1 SOLUTION

1. MODEL
  * STUDY LEVEL (CLASSIFICATION)
    * Classification Model : `EfficientNetV2 Large w/ TTA` 
  * IMAGE LEVEL (OBJECT DETECTION)  
    * 2 Classifier Model : `EfficientNetB7`
    * Object Detection Model : `YoloV5x6 w/ TTA`
2. Cross Validation Strategy  
    * Study Level : GroupKFold by Study level id - 5 Folds      
    * Image Level : GroupKFold by Study level id - 5 Folds  

3. Data Handling  
[[Discussion] Recommendations for handling duplicates on the train dataset
](https://www.kaggle.com/c/siim-covid19-detection/discussion/246597)  

* `During this competition, the annotation error issues was found. So, checked All data and Remove some data. And then train again with clean dataset. (Improve score)`
  

### 3.2 DIRECTORY STRUCTURE
```
.
├── image_level
│   ├── image_level_code
│   │   ├── hyp.scratch.yaml
│   │   ├── run_yolov5.py
│   │   ├── view_checkpoint
│   │   ├── yolo_v5l6_train.ipynb
│   │   ├── yolo_v5x6_train.ipynb
│   │   ├── yolo_v5x_alldata.ipynb
│   │   ├── yolo_v5x_kfold.ipynb
│   │   └── yolo_v5x_train.ipynb
│   ├── infer-siim-cov19-yolov5-image.ipynb
│   └── train-siim-cov19-yolov5-image.ipynb
├── infer-siim-cov19-efnb7-study-image.ipynb
├── structure.txt
├── study_level
│   ├── infer-siim-cov19-efnb7-infer-study.ipynb
│   └── train-siim-study-level.ipynb
├── two_classifier
│   └── train-2-classifier.ipynb
└── utils
    ├── convert-image-size.ipynb
    ├── data-annotating.ipynb
    ├── data-stratified-k-fold-and-create-mask.ipynb
    ├── kfold_df.csv
    ├── resized_data
    │   ├── new_resized_data
    │   └── new_resized_data2
    ├── result_view
    │   ├── 2class_visualize.ipynb
    │   ├── image_model
    │   ├── model_list.rtf
    │   ├── study_model
    │   ├── study_model_result.ipynb
    │   ├── two_class
    │   └── yolo_results.ipynb
    ├── siim-eda.ipynb
    └── weighted_box_fusion.ipynb

13 directories, 24 files

```

---  
## 4. TRAIN MODEL
---
### 4.1 Classification
#### 4.1.1 Multi head classification

### 4.2 Opacity Detection
#### 4.2.1 Yolov5x6

---
#### 4.2.2 Ensembling
---
5 GroupKFolds  
1. `Classification` : Blending Probability  
2. `2 classifier` : Blending Probability  
3. `Object Detection` : WBF Weighted Boxes Fusion  
---
## 5. FINAL SUBMISSION
---
|Public LB|Private LB|Rank|Model|
|-|-|-|-|
|0.608|0.625|73 / 1305|EffNetV2 L w/ TTA + EffNetB7 + YoloV5x6 w/ TTA|

---
