import numpy as np

if __name__ == '__main__':
    # label_txt = r"D:\Deep_Learning_data\yolo\label.txt"
    # filelists = open(label_txt).readlines()
    # list_str = []
    # for i in range(len(filelists)):
    #     str = filelists[i].split("*")
    #     list_str.append(len(str)-1)
    # print(np.max(list_str))
    # index_max = np.where(list_str == np.max(list_str))[0][0]
    # print(index_max)
    # print(filelists[index_max])

    label_txt = r"D:\Deep_Learning_data\yolo\test_2000.txt"
    filelists = open(label_txt).readlines()
    # print(len(filelists))
    # print(filelists[0])

    # 7,7,9,5 is w_index,h_index,channel,(cond+offset)
    feature_box = np.zeros(shape=(7, 7, 9, 5))
    # print(feature_box.shape)
    for index in range(1):
        # print(filelists[index])
        for i, strs in enumerate(filelists[index].split("*")):
            if i == 0:
                img_path = strs
            else:
                str = strs.split(",")
                # for k in range(len(str)):
                #     print(str[k])
                name = str[0]
                h_index = int(str[1])
                w_index = int(str[2])
                channel_index = int(str[3])
                offset_x1 = np.float32(str[4])
                offset_y1 = np.float32(str[5])
                offset_x2 = np.float32(str[6])
                offset_y2 = np.float32(str[7])
                print(name, " ", h_index, " ", w_index, " ", channel_index, " ", offset_x1, " ", offset_y1, " ",
                      offset_x2, " ", offset_y2)
    # for i,str in enumerate()
    # str = filelists[0].split("*")
