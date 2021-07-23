from re import X
import numpy as np
import matplotlib.pyplot as plt


# 显示中文
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 制作图表
x = np.arange(1, 20)
y = x*x
plt.xlabel('示例x轴')
plt.ylabel('示例y轴')
plt.plot(x, y)
plt.show()