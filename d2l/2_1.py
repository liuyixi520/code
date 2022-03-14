import torch

# 创建行向量
# x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = torch.arange(10)
print(x)
print(x.shape)
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
# 打印出来上面的张量
print(tensor_zeros)
print(tensor_ones)
print(tensor_sample)
print(tensor_list)
print('-' * 30)