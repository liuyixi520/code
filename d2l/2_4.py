import torch

# 演示自动求导，反向传播
# 这是演示点乘，x是一个向量，y是一个标量
x = torch.arange(4.0)
print(x)
x.requires_grad_(True)
print(x.grad)
y = 2*torch.dot(x, x)
print(y)
y.backward()
print(x.grad)
print(x.grad == 4*x)
print('-' * 30)

# 默认情况下要将梯度清零，需要调用.detach()
# 这里演示在计算的过程中需要将梯度清零
x.grad.zero_()
y = x.sum()
y.backward()
print(x.grad)
print('-' * 30)