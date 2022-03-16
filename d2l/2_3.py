# 张量的一些基本操作
import torch

# 创建两个标量
x = torch.tensor(1.0)
y = torch.tensor(2.0)
# 演示张量的基本算数运算
print(x)
print(y)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x**y)
print('-' * 30)

# 创建一个向量
x = torch.tensor([1.0, 2.0])
print(x)
print(x.shape)
print(len(x))
print(x[1])
print('-' * 30)

# 创建一个矩阵
x = torch.arange(12).reshape(3, 4)
y = x.T
print(x)
print(y)
print('-' * 30)

# 创建一个三维张量
x = torch.rand(2, 3, 4)
print(x)
print(x.shape)
print(x.size())
print('-' * 30)

# 演示矩阵的求和
x = torch.arange(12).reshape(3, 4)
print(x)
print(x.sum(dim=0))
print(x.sum(dim=0, keepdim=True))
print(x.sum(dim=1))
print(x.sum())
# 累加求和
print(torch.cumsum(x, dim=0))
# 保证维度不丢失
print(x.sum(dim=0, keepdim=True).shape)
print(x.sum(dim=0).shape)
print('-' * 30)

# 向量的范数
x = torch.rand(3, 4)
print(x)
print(x.norm(p=2, dim=1))
print(x.norm(p=1, dim=0))
print(x.norm(p=1, dim=1))
print(x.norm(p=1, dim=1, keepdim=True))
print('-' * 30)

# 在不同维度上的求和
# 使用arange函数创建一个2x3x4的矩阵
# 在哪个维度上求和，就使用哪个维度的索引，求和完了之后，这个维度就会丢失
# 可以使用keepdim=True参数来保证维度不丢失
x = torch.arange(24).reshape(2, 3, 4)
print(x)
# 求和
print(x.sum(dim=0))
print(x.sum(dim=1))
print(x.sum(dim=2))
print(x.sum(dim=0, keepdim=True))
print('-' * 30)