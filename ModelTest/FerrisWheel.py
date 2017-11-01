# numpy
import numpy as np
# pyplot
import matplotlib.pyplot as plt
# 3D
from mpl_toolkits.mplot3d import Axes3D
from AerialShowMap import *
from func import *

def return_pos(x, y):
    pos = {}
    pos['x'] = x
    pos['y'] = y
    return pos



for i in range(1, DRONE_NUMBER + 1):
    t = np.arange(0, ArriveTime(DRONE_NUMBER, CENTER['y'], R, DRONE_SPEED, SAFETY_DISTANCE), 0.1)
    plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(i, 0), WheelPosY(i, 0), DRONE_SPEED, t, WaitTime(i)),
             WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(i, 0), WheelPosY(i, 0), DRONE_SPEED, t, WaitTime(i)),
             "r^")

    t = np.arange(0, 20, 0.1)
    plt.plot(WheelPosX(i, t), WheelPosY(i, t), "b^")

    t = np.arange(0, 5, 0.1)
    plt.plot(WaitAndApproachPosX(WheelPosX(i, 0), WheelPosY(i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0,  DRONE_SPEED, t, WaitTime(i)),
             WaitAndApproachPosY(WheelPosX(i, 0), WheelPosY(i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0, DRONE_SPEED, t, WaitTime(i)),
             "r^")

plt.axis([-10, 10, 0, 30])
plt.show()
