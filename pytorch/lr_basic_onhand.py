import torch
import numpy as np

torch.manual_seed(42)

# 最简单的方式来描述线性回归
# 假设权重参数和偏置参数我们都已经知道了
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
inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)
print(inputs)
print(targets)

w = torch.randn(2, 3, requires_grad=True)
b = torch.randn(2, requires_grad=True)
print(w)
print(b)
print('-'*40)
# 这里稍微麻烦一点，输入是一个5x3的矩阵
# w参数初始化的时候是一个2x3的矩阵，这里要做矩阵乘法
# 所以先要把w这个参数矩阵，转置一下，再做矩阵乘法
# w的第一列就是预测apples的参数，第二列就是预测oranges的参数
def model(x):
    return x @ w.t() + b

pred = model(inputs)
print(pred)

# 均方差损失函数
def mse(t1, t2):
    diff = t1 - t2
    return torch.sum(diff*diff)/diff.numel()
loss = mse(pred, targets)
print(loss)
print('-'*40)
# 计算损失函数时，开始反向传播
loss.backward()
# 计算损失函数时，w参数的梯度和b的梯度
# 这里为了深度理解一下梯度这个概念
# 我花了一晚上的时间，手动写了一个脚本
# 利用微积分求导的知识，手动计算出来了权重参数第一个的梯度
print(w)
print(w.grad)
print(b)
print(b.grad)
print('-'*40)

# Adjust weights & reset gradients
with torch.no_grad():
    w -= w.grad * 1e-5
    b -= b.grad * 1e-5
    w.grad.zero_()
    b.grad.zero_()
print(w)
print(b)
pred = model(inputs)
loss = mse(pred, targets)
print(loss)
print('-'*40)

# 多练几次，让问题收敛的更快
for i in range(100):
    pred = model(inputs)
    loss = mse(pred, targets)
    loss.backward()
    with torch.no_grad():
        w -= w.grad * 1e-5
        b -= b.grad * 1e-5
        w.grad.zero_()
        b.grad.zero_()
print(w)
print(w.grad)
print(b)
print(b.grad)
pred = model(inputs)
loss = mse(pred, targets)
print(pred)
print(targets)
print(loss)
