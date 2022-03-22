# 手动实现softmax回归的另一个版本

import torch
import torchvision
from torch import nn
import numpy as np
import torchvision.transforms as transforms
from d2l import torch as d2l

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

num_input=28*28#输入的维度
num_output=10#预测的维度
def softMaxReg(X,w,b):
    #将x的维度重新拉平为[:,num_input],w的维度为[num_input,num_outpput]
    linValue = torch.mm(X, w) + b
    exp_linValue = linValue.exp()
    sum_exp_linValue = exp_linValue.sum(axis=1)
    softmax_value = exp_linValue / (sum_exp_linValue).view(-1, 1)
    return softmax_value
# 交叉熵损失函数
def cross_entropy(y_hat, y):
    return - torch.log(y_hat.gather(1, y.view(-1, 1)))
def sgd(params,lr,batch_size):
    for param in params:
        param.data-=lr*param.grad/batch_size
w=torch.tensor(np.random.normal(0,0.01,(num_input,num_output)),dtype=torch.float32)
b=torch.zeros(num_output,dtype=torch.float32)
w.requires_grad_(requires_grad=True)
b.requires_grad_(requires_grad=True)

net=softMaxReg

loss=cross_entropy#pytorch中的交叉熵损失函数已经包含了softmax计算，所以直接输入原始的线性结果就行，出来的就是概率
import torch.optim as optim
# optimizer=optim.SGD([w,b],lr=0.03)
lr=0.03
num_epochs=10
for epoch in range(1,num_epochs+1):
    for Xx,yy in train_iter:
        Xx = Xx.view(-1, num_input)
        output=net(Xx,w,b)
        l=loss(output,yy).sum()/len(yy)
        #反向传播求梯度，梯度之后更新，
        l.backward()
        sgd([w,b],lr,batch_size)
        w.grad.data.zero_()
        b.grad.data.zero_()
        # 训练集上的正确率
    allTrain = 0
    rightTrain = 0
    allTest = 0
    rightTest = 0
    for train_x, train_y in train_iter:
        allTrain += len(train_y)
        train_x = train_x.view(-1, num_input)
        trainOut = net(train_x,w,b)
        correct = torch.softmax(trainOut.view(trainOut.size()[0], -1), dim=1).argmax(dim=1) == train_y
        rightTrain += sum(correct).item()
    # 测试集上的正确率
    for test_x, test_y in test_iter:
        allTest += len(test_y)
        test_x = test_x.view(-1, num_input)
        testOut = net(test_x,w,b)
        correct = torch.softmax(testOut.view(testOut.size()[0], -1), dim=1).argmax(dim=1) == test_y
        rightTest += sum(correct).item()
    print("epoch%d,损失:%f,训练集上正确率%f,测试集上的正确率%f" % (epoch, l.item(), rightTrain / allTrain, rightTest / allTest))
