# 手动实现softmax回归
import torch
from IPython import display
from d2l import torch as d2l

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

# 将像素拉平，输入的图像是一个28x28像素的图片
num_inputs = 784
# 输出的是一个10分类的问题
num_outputs = 10
# 定义权重
w = torch.normal(0, 0.01, (num_inputs, num_outputs), requires_grad=True)
b = torch.zeros(num_outputs, requires_grad=True)

# 为了理解下面softmax的定义，会议一下矩阵的计算
X = torch.arange(12).view(3, 4)
print(X)
# 执行exp操作，将e作为底数，当前的值当做幂
print(X.exp())
# 在行的方向上求和
print(X.sum(0, keepdim=True))
# 在列的方向上求和
print(X.sum(1, keepdim=True))
print('-' * 30)

# 定义softmax函数
def softmax(X):
    X_exp = X.exp()
    # 每一行代表了一个样本在不同类别的概率
    partition = X_exp.sum(dim=1, keepdim=True)
    # 这里利用了广播机制
    return X_exp / partition

# 测试一下自定义的softmax函数
X = torch.normal(0, 1, (3, 4), requires_grad=True)
print(X)
print(X.sum())
print(softmax(X))
print(softmax(X).sum(dim=1, keepdim=True))
print('-' * 30)

# 实现softmax回归模型
def net(X):
    return softmax(torch.mm(X.view((-1, num_inputs)), w) + b)

# 为了理解交叉熵损失函数的铺垫
# 创建两个样本的实际标签
y = torch.tensor([0, 2])
# 模型预测出来两个样本的类别概率
y_hat = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
# 两个真实标签的实际概率
print(y_hat[[0, 1], y])
print('-' * 30)

# 定义交叉熵损失函数
def cross_entropy(y_hat, y):
    return -torch.log(y_hat[range(len(y_hat)), y])
# 打印出来两个样本的损失
print(cross_entropy(y_hat, y)) 
print('-' * 30)

# 计算正确率
def accuracy(y_hat, y):
    return (y_hat.argmax(dim=1) == y).float().mean().item()
# 测试一下正确率
print(accuracy(y_hat, y))
print('-' * 30)

# 评估任意模型net的正确率
def evaluate_accuracy(data_iter, net):
    acc_sum, n = 0.0, 0
    for X, y in data_iter:
        acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
        n += y.shape[0]
    return acc_sum / n
# 测试一下自定义的模型
print(evaluate_accuracy(test_iter, net))
print('-' * 30)

# 定义以Accumulator类为基类的类，用于计算损失和正确率
class Accumulator:
    def __init__(self):
        self.sum = 0.0
        self.n = 0

    def add(self, value):
        self.sum += value
        self.n += 1

    def reset(self):
        self.sum = 0.0
        self.n = 0

    def value(self):
        return self.sum / self.n

# softmax回归的训练
def train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size,
              params=None, lr=None, trainer=None):
    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
        for X, y in train_iter:
            y_hat = net(X)
            l = loss(y_hat, y).sum()
            # 打印出损失和正确率
            if trainer is None:
                l.backward()
                d2l.sgd(params, lr, batch_size)
            else:
                trainer.step(batch_size)
            y = y.argmax(dim=1)
            train_l_sum += l.item()
            train_acc_sum += (y_hat.argmax(dim=1) == y).sum().item()
            n += y.shape[0]
        test_acc = evaluate_accuracy(test_iter, net)
        print('epoch %d, loss %.4f, train acc %.3f, test acc %.3f'
              % (epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc)) 
train_ch3(net, train_iter, test_iter, cross_entropy, 20, batch_size)