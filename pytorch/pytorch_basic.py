import torch
import numpy as np

# torch创建标量、向量、矩阵
t1 = torch.tensor(4.)
t2 = torch.tensor([1., 2., 3., 4.])
t3 = torch.tensor([[1., 2.], [3., 4.]])

print(t1)
print(t1.shape)
print(t1.dtype)
print(t2)
print(t2.shape)
print(t3)
print(t3.shape)
print('-'*40)

# torch中的反向传播、自动求导机制
x = torch.tensor(3.)
w = torch.tensor(4., requires_grad=True)
b = torch.tensor(5., requires_grad=True)
print(x)
print(w)
print(b)
y = x*w + b
print(y)
# 开始反向传播，准备求导
y.backward()
print(x.grad)
print(w.grad)
print(b.grad)

# torch中的张量函数
t4 = torch.full((2, 2), 42)
t5 = torch.cat((t3, t4))
t6 = torch.sin(t5)
t7 = t6.reshape(2, 4)
print(t4)
print(t5)
print(t6)
print(t7)

# tensor和ndarrya互相转换
d = np.array([[1, 2], [3, 4]])
t = torch.from_numpy(d)
d2 = t.numpy()
print(d)
print(t)
print(d2)
