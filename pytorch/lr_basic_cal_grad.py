import torch
import numpy as np
# 正向传播时，kanto地区的苹果产量是这样计算出来的
kanto_con = 73.*0.3367 + 67.*0.1288 + 43.*0.2345 + 2.2082
print(f"kanto area apple con is: {kanto_con}")

# 反向传播时，求解梯度，以求解w11的梯度为例说明
# Input (temp, rainfall, humidity)
inputs = np.array([[73, 67, 43],
                   [91, 88, 64],
                   [87, 134, 58],
                   [102, 43, 37],
                   [69, 96, 70]], dtype='float32')
# Targets (apples, oranges)
targets = np.array([[56, 70],
                    [81, 101],
                    [119, 133],
                    [22, 37],
                    [103, 119]], dtype='float32')
# Convert inputs and targets to tensors
inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)
print(inputs)
print(targets)

# Weights and biases
torch.manual_seed(42)
w = torch.randn(2, 3, requires_grad=True)
b = torch.randn(2, requires_grad=True)
print(w)
print(b)
print('-'*40)

inputs_cut = inputs[:, 1:3]
inputs_self = inputs[:, 0:1]
target_cut = targets[:, 0:1]
w_cut = w[0:1, 1:3]
b_cut = b[0:1]
# 这个是第一行的后两个参数与原来输入形成的矩阵
matrix_w_i= inputs_cut@w_cut.t()
# 这个是加上偏置，然后再减去目标值形成的矩阵
matrix_const = matrix_w_i + b_cut - target_cut


print(inputs_cut)
print(target_cut)
print(w_cut)
print(b_cut)

print(inputs_self)
print(matrix_const)

# 使用求导公式手动计算w11的梯度
res = 2*0.3367*(torch.sum(inputs_self*inputs_self)) + 2*(torch.sum(inputs_self*matrix_const))
print(res/10)

