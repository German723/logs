import numpy as np
import matplotlib.pyplot as plt


# 显示中文
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.arange(-10, 11, 1)
y = x*x
plt.plot(x, y)
plt.title('这是一个示例标题')

# 添加文字
plt.text(-2.5, 30, 'function y=x*x')
plt.show()