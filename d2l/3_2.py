# 查看过拟合和欠拟合的例子
from cProfile import label
from pickletools import optimize
from pyexpat import features
import torch
from torch import nn
import math
import numpy as np
from d2l import torch as d2l

# 生成一个三阶多项式的数据集
# 多项式最高的阶数
max_degree = 20
n_train, n_test = 100, 100
true_w = np.zeros(max_degree)
true_w[:4] = np.array([5, 1.2, -3, 0.7])

# shape = [200, 1]
features = np.random.normal(size=(n_train + n_test, 1))
np.random.shuffle(features)
# shape = [200, 20]
poly_features = np.power(features, np.arange(max_degree).reshape(1, -1))
# 把每个样本的第i个特征除以i!，因为前面i次方了，所以这里把他们要放小一点
for i in range(max_degree):
    poly_features[:, i] = poly_features[:, i] / math.gamma(i+1)
labels = np.dot(poly_features, true_w) + np.random.normal(scale=0.1, size=n_train + n_test)

# 定义模型的损失函数
def evaluate_loss(net, data_iter, loss):
    metric = d2l.Accumulator(2)
    for X, y in data_iter:
        metric.add(loss(net(X), y).sum(), d2l.size(y))
    return metric[0] / metric[1]

# 定义训练过程
def train(train_features, test_features, train_labels, test_labels, num_epochs=400):
    loss = nn.MSELoss()
    input_shape = train_features.shape[-1]
    net = nn.Sequential(nn.Linear(input_shape, 1, bias=False))
    batch_size = min(10, train_labels.shape[0])
    train_iter = d2l.load_array((train_features, train_labels.reshape(-1, 1)), batch_size)
    test_iter = d2l.load_array((test_features, test_labels.reshape(-1, 1)), batch_size)
    optimize = torch.optim.SGD(net.parameters(), lr=0.01)
    animator = d2l.Animator(xlabel='epoch', xlim=[0, num_epochs], ylim=[0.1, 0.9])
    for epoch in range(num_epochs):
        d2l.train_ch3(net, train_iter, loss, optimize)
        if epoch==0 or (epoch+1)%20==0:
            animator.add(epoch+1, evaluate_loss(net, test_iter, loss), 
            evaluate_loss(net, train_iter, loss))
    print('weight:', net[0].weight.data.numpy())

train(poly_features[:n_train, :4], poly_features[n_train:, :4], labels[:n_train], labels[n_train:], num_epochs=400)


# print(true_w)
# print(features)
# print(features.shape)
# print(poly_features)
# print(poly_features.shape)
# print(labels)