# YOLO_misc
Build a YOLO project refer v1/v2/v3.

# How to use

## Create train datasets(224/) and label.txt
1. Replace your VOCdevkit dataset path to here `data/gen_data.py`.
``` python
xml_path = r"/home/tensorflow01/workspace/Share/0_Yolo/label"
img_path = r"/home/tensorflow01/workspace/Share/0_Yolo/images"
save_img_224_path = r"/home/tensorflow01/workspace/Share/0_Yolo/224"
save_txt = r"/home/tensorflow01/workspace/Share/0_Yolo/label.txt"
```
2. Execute `data/gen_data.py` to create images of size 224x224 and label.txt(include filename, class, box info. etc.)

## Predict with the pre-trained model parameters
1. Download "yolo_v2_test_100.pkl" at Release page, then copy "yolo_v2_test_100.pkl" to the directory "my_param".
2. Run `detect.py` to predict the bbox of object. 

**Note** : This pre-trained model parameters is just a overfitting one.

## Train the network
1. Modify the path of label / image dataset;
2. Run `train.py` to train the network.
