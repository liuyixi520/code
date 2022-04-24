# 加载mnist数据集
# 这里和书里不一样，书里是把数据集先下载下来的
# 可能是不想用keras这个包，和自己提前说的只用numpy和matplotlib
from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

# 查看一下数据集第一个样本和标签
from PIL import Image
img = Image.fromarray(X_train[0])
img.show()