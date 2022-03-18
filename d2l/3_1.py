# 手动实现一个多层感知机
from pickletools import optimize
import torch 
from torch import nn
from d2l import torch as d2l

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

num_inputs, num_outputs, num_hiddens = 784, 10, 256
W1 = nn.Parameter(torch.randn(num_inputs, num_hiddens, requires_grad=True))
b1 = nn.Parameter(torch.zeros(num_hiddens, requires_grad=True))
W2 = nn.Parameter(torch.randn(num_hiddens, num_outputs, requires_grad=True))
b2 = nn.Parameter(torch.zeros(num_outputs, requires_grad=True))
parmamter = [W1, b1, W2, b2]

# 实现ReLU函数
def relu(X):
    return torch.max(X, torch.zeros_like(X))

# 实现模型
def net(X):
    X = X.view((-1, num_inputs))
    X = relu(torch.matmul(X, W1) + b1)
    return torch.matmul(X, W2) + b2

# 定义损失函数
loss = nn.CrossEntropyLoss()

num_epochs, lr = 5, 0.1
optimize = torch.optim.SGD(parmamter, lr=lr)
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, optimize)