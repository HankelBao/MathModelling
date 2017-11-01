# numpy
import numpy as np
# pyplot
import matplotlib.pyplot as plt
# 3D
from mpl_toolkits.mplot3d import Axes3D
from AerialShowMap import *
from func import *


for i in range(1, DRONE_NUMBER + 1):
    t = np.arange(0, ArriveTime(DRONE_NUMBER, FERRIS['y'], FERRIS['R'], DRONE_SPEED, SAFETY_DISTANCE), 0.1)
    plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
             WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
             "r^")

    t = np.arange(0, 20, 0.1)
    plt.plot(WheelPosX(FERRIS, i, t), WheelPosY(FERRIS, i, t), "b^")

    t = np.arange(0, 5, 0.1)
    plt.plot(WaitAndApproachPosX(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0,  DRONE_SPEED, t, WaitTime(i)),
             WaitAndApproachPosY(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0, DRONE_SPEED, t, WaitTime(i)),
             "r^")

plt.axis([-10, 10, 0, 30])
plt.show()
