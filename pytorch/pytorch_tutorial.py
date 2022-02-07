import torch
import numpy as np

# tensor的创建
tensor_zeros = torch.zeros([3, 3])
tensor_ones = torch.ones([4, 4])
tensor_rand = torch.rand([5, 5])
print(tensor_zeros)
print(tensor_ones)
print(tensor_rand)
print('-'*40)

# tensor的基本算数操作
x = torch.rand([2, 2])
y = torch.rand([2, 2])
print(x)
print(y)
print(x+y)
print(x*y)
print(x-y)
print(x/y)
print('-'*40)

# tensor的切割
z = torch.rand([4, 4])
print(z)
print(z[:, 1])
print(z[2, :])
print('-'*40)

# tensor取某个特定值, tensor变形
print(z[1, 1])
print(z[1, 1].item())
print(z.view(1, 16))
print(z.view(2, 8))
print('-'*40)

# numpy&tensor
## 将tensor转换成numpy
t = torch.rand(2, 2)
print(t)
n = t.numpy()
print(n)
## 将numpy转换成tensor
n1 = np.ones(4)
print(n1)
t1 = torch.from_numpy(n1)
print(t1)
## 修改其中一个的值，另一个也随之改变
n1 += 1
print(n1)
print(t1)
print('-'*40)
