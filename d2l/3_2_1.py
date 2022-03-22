# 使用torch高级API实现softmax回归模型
import torch
from torch import nn
from d2l import torch as d2l

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

# Flatten函数可以将多维数组展平
# 后面那个是指定输出的维度，前面是输入张量，后面是输出张量
net = nn.Sequential(nn.Flatten(), nn.Linear(784, 10))
def init_weights(m):
    if type(m)==nn.Linear:
        nn.init.normal_(m.weight, mean=0, std=0.01)
# 完成初始化
net.apply(init_weights)

# 定义损失函数
loss = nn.CrossEntropyLoss()
# 定义优化器
optimizer = torch.optim.SGD(net.parameters(), lr=0.1)

# 开始训练
num_epochs = 5
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, optimizer)