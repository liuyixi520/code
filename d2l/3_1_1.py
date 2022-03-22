# 使用torch中的API实现了一个线性回归模型
from pyexpat import features
import torch
import numpy as np
from torch.utils import data
from d2l import torch as d2l

true_w = torch.tensor([[1.0], [2.0]], dtype=torch.float32)
true_b = torch.tensor(0.5, dtype=torch.float32)
features, labels = d2l.synthetic_data(true_w, true_b, num_examples=100)
print(features)
print(labels)
print('-' * 30)

def load_array(data_array, batch_size, is_train=True):
    dataset = data.TensorDataset(*data_array)
    if is_train:
        return data.DataLoader(dataset, batch_size, shuffle=True)
    else:
        return data.DataLoader(dataset, batch_size, shuffle=False)

# 测试一下上面这个load_array函数
batch_size = 10
data_iter = load_array((features, labels), batch_size)
next(iter(data_iter))

# 定义模型
from torch import nn
net = nn.Sequential(nn.Linear(2, 1))
# 初始化模型参数
net[0].weight.data.uniform_(-0.01, 0.01)
net[0].bias.data.fill_(0.0)
# 定义损失函数
loss = nn.MSELoss()
# 定义优化算法
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)

# 训练模型
num_epochs = 10
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X), y)
        optimizer.zero_grad()
        l.backward()
        optimizer.step()
    # 训练完一次，就打印在全体数据上的损失
    train_loss = loss(net(features), labels).item()
    print('epoch %d, loss: %f' % (epoch + 1, train_loss))