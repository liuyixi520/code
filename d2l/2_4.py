# 介绍pytorch的自动求导
import torch

# 演示自动求导，反向传播
# 这是演示点乘，x是一个向量，y是一个标量
# 为什么要把y设置为标量，因为损失函数是标量函数
# 如果y是一个向量，那么损失函数就是向量函数，那么求导就不好求了
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
