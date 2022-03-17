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
    if isinstance(net, torch.nn.Module):
        net.eval()
    metric = Accumulator(2)
    with torch.no_grad():
        for X, y in data_iter:
            metric.add(accuracy(net(X), y), y.shape[0])
    return metric[0] / metric[1]

class Accumulator:  #@save
    """在n个变量上累加"""
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

print(evaluate_accuracy(test_iter, net))

def train_epoch_ch3(net, train_iter, loss, updater):  #@save
    """训练模型一个迭代周期（定义见第3章）"""
    # 将模型设置为训练模式
    if isinstance(net, torch.nn.Module):
        net.train()
    # 训练损失总和、训练准确度总和、样本数
    metric = Accumulator(3)
    for X, y in train_iter:
        # 计算梯度并更新参数
        y_hat = net(X)
        l = loss(y_hat, y)
        if isinstance(updater, torch.optim.Optimizer):
            # 使用PyTorch内置的优化器和损失函数
            updater.zero_grad()
            l.mean().backward()
            updater.step()
        else:
            # 使用定制的优化器和损失函数
            l.sum().backward()
            updater(X.shape[0])
        metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())
    # 返回训练损失和训练精度
    return metric[0] / metric[2], metric[1] / metric[2]

class Animator:  #@save
    """在动画中绘制数据"""
    def __init__(self, xlabel=None, ylabel=None, legend=None, xlim=None,
                 ylim=None, xscale='linear', yscale='linear',
                 fmts=('-', 'm--', 'g-.', 'r:'), nrows=1, ncols=1,
                 figsize=(3.5, 2.5)):
        # 增量地绘制多条线
        if legend is None:
            legend = []
        d2l.use_svg_display()
        self.fig, self.axes = d2l.plt.subplots(nrows, ncols, figsize=figsize)
        if nrows * ncols == 1:
            self.axes = [self.axes, ]
        # 使用lambda函数捕获参数
        self.config_axes = lambda: d2l.set_axes(
            self.axes[0], xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
        self.X, self.Y, self.fmts = None, None, fmts

    def add(self, x, y):
        # 向图表中添加多个数据点
        if not hasattr(y, "__len__"):
            y = [y]
        n = len(y)
        if not hasattr(x, "__len__"):
            x = [x] * n
        if not self.X:
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        for i, (a, b) in enumerate(zip(x, y)):
            if a is not None and b is not None:
                self.X[i].append(a)
                self.Y[i].append(b)
        self.axes[0].cla()
        for x, y, fmt in zip(self.X, self.Y, self.fmts):
            self.axes[0].plot(x, y, fmt)
        self.config_axes()
        display.display(self.fig)
        display.clear_output(wait=True)

def train_ch3(net, train_iter, test_iter, loss, num_epochs, updater):  #@save
    """训练模型（定义见第3章）"""
    animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0.3, 0.9],
                        legend=['train loss', 'train acc', 'test acc'])
    for epoch in range(num_epochs):
        train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
        test_acc = evaluate_accuracy(net, test_iter)
        animator.add(epoch + 1, train_metrics + (test_acc,))
    train_loss, train_acc = train_metrics
    assert train_loss < 0.5, train_loss
    assert train_acc <= 1 and train_acc > 0.7, train_acc
    assert test_acc <= 1 and test_acc > 0.7, test_acc