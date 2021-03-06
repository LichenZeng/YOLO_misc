import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils import data
from torch.autograd import Variable
import os, math, shutil
import numpy as np
from data.sampling import MyDataset
from model.net import Yolo_V2

if __name__ == '__main__':

    yolo_v2 = Yolo_V2()  # 创建网络

    label_txt = r"label.txt"  # 导入数据

    mydataset = MyDataset(label_txt)
    dataloader = data.DataLoader(mydataset, batch_size=5, shuffle=True)

    if torch.cuda.is_available():
        yolo_v2 = yolo_v2.cuda()

    # 加载保存的数据
    yolo_v2_paramater_path = r"my_param/yolo_v2_test_100.pkl"
    if os.path.exists(yolo_v2_paramater_path):
        yolo_v2.load_state_dict(torch.load(yolo_v2_paramater_path))

    # 获得网络的数据
    yolo_v2_paramater_list = []
    yolo_v2_paramater_list.extend(yolo_v2.parameters())

    # 定义优化器
    opt_yolo_v2 = optim.Adam(yolo_v2_paramater_list)

    # 定义损失函数
    loss_cond_fun = nn.BCELoss()
    loss_offset_fun = nn.MSELoss()

    for i in range(2200):
        img, cond, offset = mydataset.get_batch(dataloader)
        img, cond, offset = Variable(img), Variable(cond), Variable(offset)
        if torch.cuda.is_available():
            img, cond, offset = img.cuda(), cond.cuda(), offset.cuda()
        # 将参数传入网络
        out_cond, out_offset = yolo_v2(img)
        out_cond = out_cond.view(-1, 9, 7, 7, 1)  # 维度变形  view
        out_offset = out_offset.view(-1, 9, 4, 7, 7)
        out_offset = out_offset.permute(0, 1, 3, 4, 2)

        # 取出对应的索引计算损失
        idx1 = torch.ne(cond[:, :, :, :, 0], 0)
        # print(cond.shape, idx1.shape)
        # print(offset[idx1])
        # exit()
        cond_1 = cond[idx1].double()
        offset_1 = offset[idx1]

        idx0 = torch.eq(cond[:, :, :, :, 0], 0)
        cond_0 = cond[idx0].double()

        _1_out_cond = out_cond[idx1].double()
        _0_out_cond = out_cond[idx0].double()

        _1_out_offset = out_offset[idx1].double()

        loss_cond = loss_cond_fun(_1_out_cond, cond_1) + loss_cond_fun(_0_out_cond, cond_0)
        loss_offset = loss_offset_fun(_1_out_offset, offset_1)
        loss = loss_cond + loss_offset

        opt_yolo_v2.zero_grad()  # 优化器清零
        loss.backward()  # 损失反向
        opt_yolo_v2.step()  # 更新优化器

        print(i, "-- ", loss.cpu().data.numpy(), "--cond:", loss_cond.cpu().data.numpy(), " --loss_offset:",
              loss_offset.cpu().data.numpy())

        if ((i + 1) % 25 == 0):
            torch.save(yolo_v2.state_dict(), yolo_v2_paramater_path)

        # if ((i + 1) % 25 == 0):
        #     shutil.copyfile(yolo_v2_paramater_path, os.path.join(r"./param_c", "yolo_v2_test_100.pkl"))
