# 使用torch的API实现多层感知机
from pandas import lreshape
import torch
from torch import nn
from d2l import torch as d2l

# 定义模型
# 记样本的个数为n，那么输入就是n*28*28，先使用Flatten展平，就变成n*784
net = nn.Sequential(nn.Flatten(), nn.Linear(784, 256), nn.ReLU(), nn.Linear(256, 10))
# 初始化参数
for param in net.parameters():
    nn.init.normal_(param, mean=0, std=0.01)
# 定义损失函数
loss = nn.CrossEntropyLoss()
# 定义优化器
optimizer = torch.optim.SGD(net.parameters(), lr=0.1)
# 开始训练
num_epochs = 5
batch_size, lr = 256, 0.1

# 开始训练
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, optimizer)