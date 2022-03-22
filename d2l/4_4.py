# 权重衰退演示
import matplotlib
from torch import nn
from d2l import torch as d2l
import torch

# 模拟生生一个数据集
# 故意将训练样本生成的比较少，这样才容易发生过拟合
n_trian, n_test, num_inputs, batch_size = 20, 100, 200, 5
true_w, true_b = torch.ones(num_inputs, 1) * 0.01, 0.05
train_data = d2l.synthetic_data(true_w, true_b, n_trian)
train_iter = d2l.load_array(train_data, batch_size)
test_data = d2l.synthetic_data(true_w, true_b, n_test)
test_iter = d2l.load_array(test_data, batch_size)

# 初始化模型参数
def init_params():
    w = torch.normal(0, 1, size=(num_inputs, 1), requires_grad=True)
    b = torch.zeros(1, requires_grad=True)
    return [w, b]
# 定义L2范数
def l2_penalty(w):
    return (w ** 2).sum() / 2

# 定义训练过程
def train(lambd):
    w, b = init_params()
    net, loss = lambda X: d2l.linreg(X, w, b), d2l.squared_loss
    num_epochs, lr = 100, 0.003
    animator = d2l.Animator(xlabel='epoch', xlim=[0, num_epochs], ylim=[0.1, 0.9])
    for epoch in range(num_epochs):
        for X, y in train_iter:
            l = loss(net(X), y) + lambd * l2_penalty(w)
            l.backward()
            d2l.sgd([w, b], lr, batch_size)
        if(epoch+1) % 5 == 0:
            animator.add(epoch+1, [d2l.semilogy(loss(net(X), y).item()) for X, y in test_iter])
        print('w的L2范数为：%f' % w.norm().item())

# 显示训练过程
train(lambd=0.1)