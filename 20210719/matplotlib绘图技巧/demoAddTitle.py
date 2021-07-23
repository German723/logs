import numpy as np
import matplotlib.pyplot as plt


# 显示中文
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
# %matplotlib inline
x = np.arange(0,10)
plt.title('这是一个示例标题')
plt.plot(x, x*x)
plt.show()


