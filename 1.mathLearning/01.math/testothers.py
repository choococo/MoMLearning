import torch
import torch.nn as nn

# # 有问题？？？？？？？error
# # x = torch.tensor(5., requires_grad=True)
# x = torch.Tensor([5.])
# x = torch.nn.Parameter(x)
# b = x **2
#
# opt = torch.optim.SGD([x], lr=0.01)
# for i in range(100):
#     opt.zero_grad()
#     b.backward(retain_graph=True)
#     opt.step()
#     print(x)

import cv2
import numpy as np

a = np.arange(400*400*3).reshape(400, 400, 3)/(400*400*3)
cv2.imshow()