import torch
import numpy as np

# 从基本的列表中创建tensor
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(type(data))
print(x_data)
print('-'*40)

# 从ndarray中创建tensor
np_array = np.array(data)
print(type(np_array))
np_data = torch.from_numpy(np_array)
print(np_data)
print('-'*40)

# 按照tensor的形状和数据类型复制张量
x_ones = torch.ones_like(x_data)
x_rand = torch.rand_like(x_data, dtype=torch.float32)
print(x_ones)
print(x_rand)
print('-'*40)

# tensor中的一些属性
tensor = torch.rand(3, 4)
print(f"tensor shape is: {tensor.shape}")
print(f"tensor dtype is: {tensor.dtype}")
print(f"tensor device is: {tensor.device}")

torch.on
