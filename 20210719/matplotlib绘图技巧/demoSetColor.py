import numpy as np
import matplotlib.pyplot as plt


# 显示中文
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.arange(1, 5)
plt.plot(x, color='g')
plt.plot(x+1, color='0.5')
plt.plot(x+2, color='#FF00FF')
plt.plot(x+3, color=(0.1, 0.2, 0.3))
plt.show()