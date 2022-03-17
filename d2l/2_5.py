# 手动实现一个线性回归

from turtle import color
import matplotlib.pyplot as plt
import torch
import random

# 生成模拟数据集
# 实现方程：y = w*x + b + noise
# 其中w是各个特征的参数，b是偏置, num_sample是样本数量
# 最后为了模拟效果，加入了一个噪声noise
def synthetic_data(w, b, num_samples):
    x = torch.normal(0, 1, (num_samples, len(w)))
    y = torch.matmul(x, w) + b
    y += torch.normal(0, 0.1, (num_samples,))
    return x, y.reshape(-1, 1)
# 定义两个实际的参数
true_w = torch.tensor([1.0, 2.0], dtype=torch.float32)
# 定义偏置数字
true_b = torch.tensor(0.5, dtype=torch.float32)
# 获得训练数据
features, labels = synthetic_data(true_w, true_b, num_samples=100)
print(features)
print(labels)
print('-' * 30)

# 画出features和labels的散点图
# 大概看一下两个特征和目标是存在线性相关的
plt.scatter(features[:, 0], labels, color='r')
plt.scatter(features[:, 1], labels, color='b')
# plt.show()

# 线性回归中最重要的两个参数：每次训练的批量和学习率
# 每次训练的批量，每次训练的批量是一个batch_size的数量
# 学习率，每次更新参数的时候，更新的参数是每次更新的参数的系数
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    # 生成样本中的索引
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        # 有可能会最后一个i+batch_size超出num_examples，所以要判断
        j = torch.LongTensor(indices[i: min(i + batch_size, num_examples)])
        # yield返回的是一个迭代器，每次迭代的时候，返回的是一个batch_size的数据
        yield features.index_select(0, j), labels.index_select(0, j)
# 测试一下每次返回的数据
batch_size = 10
for X,y in data_iter(batch_size, features, labels):
    print(X, y)
    break
print('-' * 30)

# 定义初始化参数
w  = torch.normal(0, 0.01, (2, 1), requires_grad=True)
b  = torch.zeros(1, requires_grad=True)
# 定义模型
def linreg(X, w, b):
    return torch.matmul(X, w) + b
# 定义损失函数
def squared_loss(y_hat, y):
    return (y_hat - y.view(y_hat.size())) ** 2 / 2
# 定义优化函数
def sgd(params, lr, batch_size):
    with torch.no_grad(): 
        for param in params:
            param.data -= lr * param.grad / batch_size
            param.grad.zero_()

# 训练的过程
lr = 0.03
num_epochs = 20
net = linreg
loss = squared_loss
for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y).sum()
        l.backward()
        sgd([w, b], lr, batch_size)
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print('epoch %d, loss %f' % (epoch + 1, train_l.mean().item()))

# 因为是手工创建的数据集，所以知道真实的参数，看一下预测的结果与真实的结果是否相差太大
print(true_w, w)
print(true_b, b)
print('-' * 30)