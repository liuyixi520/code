# 介绍基本的标量、向量、矩阵、张量的创建和操作
import torch

# 创建行向量
# x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = torch.arange(10)
print(x)
print(x.shape)
# print x number of elements
print(x.numel())
print('-'*30)

# 转换为一个矩阵
y = x.reshape(2, 5)
print(y)
print(y.shape)
print(y.numel())
print('-' * 30)

# 其他方式创建张量
tensor_zeros = torch.zeros(2, 3)
tensor_ones = torch.ones(2, 3)
tensor_sample = torch.rand(2, 3)
tensor_list = torch.tensor([[1, 2, 3], [4, 5, 6]])
# 创建一个三维的张量
tensor_3d = torch.rand(2, 3, 4)
# 打印出来上面的张量
print(tensor_zeros)
print(tensor_ones)
print(tensor_sample)
print(tensor_list)
print(tensor_3d)
print('-' * 30)

# 访问元素
print(x[1:3])
# y前两行的第三列
print(y[:, 2])

# 创建两个二维张量
x = torch.rand(2, 3)
y = torch.rand(2, 3)
# 演示张量的基本算数运算
print(x)
print(y)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x**y)
print('-' * 30)

# 把两个张量连接起来
x = torch.rand(2, 3)
y = torch.rand(2, 3)
# 在第一个维度上连接，即在每一行上连接
print(torch.cat([x, y], dim=0))
# 在第二个维度上连接，即在每一列上连接
print(torch.cat([x, y], dim=1))
print('-' * 30)

# 演示一个张量的求和
x = torch.rand(2, 3)
print(x)
# 第一个维度上的求和，即每一行的求和
print(x.sum(dim=0))
# 第二个维度上的求和，即每一列的求和
print(x.sum(dim=1))
# 所有的元素的求和
print(x.sum())
print('-' * 30)

# 演示一下广播机制
x = torch.rand(2, 3)
y = torch.rand(3)
print(x)
print(y)
# y少了一行，把y广播到x的每一行上
print(x+y)
print(x * y)
print('-' * 30)

# 演示tensor和numpy的转换
x = torch.rand(2, 3)
print(x)
# 转换为numpy
print(x.numpy())
# 转换为numpy数组
print(x.numpy().shape)
# 转换为tensor
print(torch.from_numpy(x.numpy()))
print('-' * 30)