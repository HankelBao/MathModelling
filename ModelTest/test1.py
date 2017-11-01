# numpy
import numpy as np
# pyplot
import matplotlib.pyplot as plt
# 3D
from mpl_toolkits.mplot3d import Axes3D

aasdfas
def func(x):
    return np.sin(x)


def f(x):
    return x**2 + x * 1 + 5 + np.cos(x)


def fx(x):
    return np.cos(x) + np.sin(x)


def fy(x):
    return np.cos(x + 1.23 * np.pi)


# arange 0.1 means interval
a = np.arange(1, 5, 0.1)
# linspace: 50 means 50 steps
b = np.linspace(1, 101, 40)
# plot里两个参数必须数组大小一样
# subplot 行数+图象数+图像编号
plt.subplot(131)
plt.grid(True)
plt.title("magic title")
plt.xlabel("This is x label")
plt.ylabel("This is y label")
plt.plot(a, b, 'r^')
# plot 就是连线
# scatter就是画点
# bar 就是柱状图

plt.subplot(132)
plt.title("Pic 2")
plt.scatter(a, fx(a) + fy(a))
plt.plot(a, fx(a) + 1.1, "r--")

plt.subplot(133, projection='3d')
z = np.arange(0, 2 * np.pi, 0.01)
plt.plot(z, z, z)

plt.show()
