import torch
import numpy as np

a = boxes = [[10, 20, 129, 255],[126, -1, 221, 164]]
a = torch.Tensor(a)
index_neg = torch.lt(a, 0)
print(index_neg)