import tensorflow as tf
import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
%matplotlib inline


trainsamples = 200
testsamples = 60

# 这里我们定义模型。这个模型中含有一个简单的输入层和一个隐藏的sigmoid激活层。
def model(X, hidden_weights1, hidden_bias1, ow):
    hidden_layer =  tf.nn.sigmoid(tf.matmul(X, hidden_weights1)+ b)
    return tf.matmul(hidden_layer, ow)

# 随机生成数据
dsX = np.linspace(-1, 1, trainsamples + testsamples).transpose() # 在-1到1内返回均匀间隔的数字
dsY = 0.4* pow(dsX,2) +2 * dsX + np.random.randn(*dsX.shape) * 0.22 + 0.8 # 生成Y方向的值

plt.figure() # 创建输出文件
plt.title('Original data')
plt.scatter(dsX,dsY) # 绘制数据点的散点图

