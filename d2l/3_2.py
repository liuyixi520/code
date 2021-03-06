# 手动实现softmax回归
# 这个是按照d2l中的写出来的，只能理解到accu那儿，后面的有点不能理解
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
# 生成一个num_inputs x num_outputs的权重矩阵
w = torch.normal(0, 0.01, (num_inputs, num_outputs), requires_grad=True)
# 生成一个长度为num_outputs的偏置向量
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
# X.sum()将会是一个标量
# softmax(X)将会是一个 3x4 的矩阵，只是这个矩阵的每一行的总和是1
X = torch.normal(0, 1, (3, 4), requires_grad=True)
print(X)
print(X.sum())
print(softmax(X))
print(softmax(X).sum(dim=1, keepdim=True))
print('-' * 30)

# 实现softmax回归模型
# softmax里面仍然是一个线性模型，这个线性模型的解释如下
# 在这个例子里X是一个28x28的像素矩阵，线性模型先将它拉平成一个 1x784 的矩阵
# 然后和权重向量w相乘，最后加上偏置向量b
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
# range(len(y_hat))会返回样本的索引，要是这个样本的类别是y的话，就返回1，否则返回0
# 所以y_hat[range(len(y_hat)), y]就是每一个样本的真实类别的概率
# 所以就计算出了每一个样本的交叉熵损失，然后求和
# 这时候就只关注了每个样本在实际标签为真时的信息损失
# 如果这个样本的类别为y预测的概率也是1的时候，信息损失就是0，反之信息损失就会很大
def cross_entropy(y_hat, y):
    return -torch.log(y_hat[range(len(y_hat)), y])
# 打印出来两个样本的损失
print(y_hat[range(len(y_hat))])
print(y_hat[range(len(y_hat)), y])
print(cross_entropy(y_hat, y)) 
print('-' * 30)

# 计算正确率
# 观测每一个样本的类别是否是预测的类别，如果是就返回1，否则返回0
# 然后返回预测准确的总共样本个数
def accuracy(y_hat, y):
    return (y_hat.argmax(dim=1) == y).sum().item()
# 测试一下正确率
print(accuracy(y_hat, y)/len(y))
print('-' * 30)