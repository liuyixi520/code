from statistics import mode
import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

# Input (temp, rainfall, humidity)
inputs = np.array([[73, 67, 43],
                   [91, 88, 64],
                   [87, 134, 58],
                   [102, 43, 37],
                   [69, 96, 70],
                   [74, 66, 43],
                   [91, 87, 65],
                   [88, 134, 59],
                   [101, 44, 37],
                   [68, 96, 71],
                   [73, 66, 44],
                   [92, 87, 64],
                   [87, 135, 57],
                   [103, 43, 36],
                   [68, 97, 70]],
                  dtype='float32')
# Targets (apples, oranges)
targets = np.array([[56, 70],
                    [81, 101],
                    [119, 133],
                    [22, 37],
                    [103, 119],
                    [57, 69],
                    [80, 102],
                    [118, 132],
                    [21, 38],
                    [104, 118],
                    [57, 69],
                    [82, 100],
                    [118, 134],
                    [20, 38],
                    [102, 120]],
                   dtype='float32')

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)
print(inputs)
print(targets)
print(inputs.shape)
print(targets.shape)
print('-'*40)

train_ds = TensorDataset(inputs, targets)
print(train_ds[0:7])

batch_size = 5
train_dl = DataLoader(train_ds, batch_size, shuffle=True)
for inp, tar in train_dl:
    print(inp)
    print(tar)
print('-'*40)

model = nn.Linear(3, 2)
print(model.weight)
print(model.bias)
print(list(model.parameters()))

# 到这里，瞎蒙的过程就完成了
# 随机初始化参数，然后计算出来预测结果
pred = model(inputs)
print(pred)
print(targets)
print('-'*40)

# 引入损失函数，评估一下瞎猜的结果的好坏
import torch.nn.functional as F
loss_fn = F.mse_loss
loss = loss_fn(pred, targets)
print(loss)
print('-'*40)

# 引入优化器
opt = torch.optim.SGD(model.parameters(), lr=1e-5)
print(opt)
print('-'*40)

# Utility function to train the model
def fit(num_epochs, model, loss_fn, opt, train_dl):

    # Repeat for given number of epochs
    for epoch in range(num_epochs):

        # Train with batches of data
        for xb,yb in train_dl:

            # 1. Generate predictions
            pred = model(xb)

            # 2. Calculate loss
            loss = loss_fn(pred, yb)

            # 3. Compute gradients
            loss.backward()

            # 4. Update parameters using gradients
            opt.step()

            # 5. Reset the gradients to zero
            opt.zero_grad()

        # Print the progress
        if (epoch+1) % 10 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

fit(3000, model, loss_fn, opt, train_dl)
pred = model(inputs)
print(pred)
print(targets)
