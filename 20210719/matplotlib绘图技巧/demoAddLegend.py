import numpy as np
import random
import matplotlib.pyplot as plt


# 显示中文
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = random.randint(1, 11)
y1 = x
y2 = x*2
y3 = x*3
y4 = x*4
plt.plot(x, x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.legend(['demo', 'Demo', 'DEMO', 'DEMo'])
plt.show()