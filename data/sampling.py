import os
import numpy as np
from PIL import Image
from torch.utils import data


class MyDataset(data.Dataset):

    def __init__(self, label_txt):
        self.filelists = open(label_txt).readlines()

    def __getitem__(self, index):
        # strs = self.filelists[index].split("*")
        # img_path = strs[0]
        # img = np.array(Image.open(img_path), dtype=np.float32)/255.0 - 0.5
        # img = np.transpose(img, (2,0,1))

        # 7*7*9*1置信度和 7*7*9*4 offset
        cond = np.zeros(shape=(9, 7, 7, 1))
        offset = np.zeros(shape=(9, 7, 7, 4))

        for i, strs in enumerate(self.filelists[index].split("*")):
            if i == 0:
                img_path = strs
            else:
                # strs =  person,3,3,8,0.0,0.15104166666666666,0.25,-0.265625
                #            0   1 2 3  4   5                    6      7
                str = strs.split(",")
                name = str[0]
                h_index = int(str[1])
                w_index = int(str[2])
                channel_index = int(str[3])
                offset_x1 = np.float32(str[4])
                offset_y1 = np.float32(str[5])
                offset_x2 = np.float32(str[6])
                offset_y2 = np.float32(str[7])

                # 给置信度和offset赋值
                cond[channel_index][h_index][w_index][0] = 1
                offset[channel_index][h_index][w_index][0] = offset_x1
                offset[channel_index][h_index][w_index][1] = offset_y1
                offset[channel_index][h_index][w_index][2] = offset_x2
                offset[channel_index][h_index][w_index][3] = offset_y2

        img = np.array(Image.open(img_path), dtype=np.float32) / 255.0 - 0.5
        img = np.transpose(img, (2, 0, 1))

        return img, cond, offset

    def __len__(self):
        return len(self.filelists)

    def get_batch(self, dataload):
        dataiter = iter(dataload)
        return dataiter.next()


if __name__ == '__main__':
    label_txt = r"../label.txt"

    mydataset = MyDataset(label_txt)
    dataloader = data.DataLoader(mydataset, batch_size=2, shuffle=False)
    for i in range(2):
        img, cond, offset = mydataset.get_batch(dataloader)
        print(img.shape)
        print(cond.shape)
        print(offset.shape)
