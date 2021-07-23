import numpy as np
import matplotlib.pyplot as plt


# 显示中文
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.arange(-10, 11, 1)
y = x*x
plt.plot(x, y)

# 添加注释
plt.annotate(s='最低点', xy=(0, 1), xytext=(-2, 22), arrowprops={'headwidth': 10, 'facecolor': 'r'})
# plt.annotate('这是一个示例注释', xy=(-2, 22), xytext=(0, 1))
plt.show()