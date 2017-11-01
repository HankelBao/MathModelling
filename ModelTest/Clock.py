# numpy
import numpy as np
# pyplot
import matplotlib.pyplot as plt
# 3D
from mpl_toolkits.mplot3d import Axes3D
from AerialShowMap import *
from func import *


for i in range(1, DRONE_NUMBER + 1):
    t = np.arange(0, ArriveTime(DRONE_NUMBER, CENTER['y'], R, DRONE_SPEED, SAFETY_DISTANCE), 0.1)
    plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(i, 0), WheelPosY(i, 0), DRONE_SPEED, t, WaitTime(i)),
             WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(i, 0), WheelPosY(i, 0), DRONE_SPEED, t, WaitTime(i)),
             "r^")

    t = np.arange(0, 20, 0.1)
    plt.plot(WheelPosX(i, t), WheelPosY(i, t), "b^")



plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER-1, 0.5), 0, 0, 5, DRONE_SPEED, t, WaitTime(i)),
        WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER-1, 0.5), 0, 0, 5, DRONE_SPEED, t, WaitTime(i)),
        "r^")
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER-2, 0.5), 0, 0, 5.5, DRONE_SPEED, t, WaitTime(i)),
        WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER-2, 0.5), 0, 0, 5.5, DRONE_SPEED, t, WaitTime(i)),
        "r^")
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER-3, 0.5), 0, 0, 6, DRONE_SPEED, t, WaitTime(i)),
        WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER-3, 0.5), 0, 0, 6, DRONE_SPEED, t, WaitTime(i)),
        "r^")
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER-4, 0.5), 0, 0, 6.5, DRONE_SPEED, t, WaitTime(i)),
        WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER-4, 0.5), 0, 0, 6.5, DRONE_SPEED, t, WaitTime(i)),
        "r^")
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER-5, 0.5), 0, 0, 7, DRONE_SPEED, t, WaitTime(i)),
        WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER-5, 0.5), 0, 0, 7, DRONE_SPEED, t, WaitTime(i)),
        "r^")
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER-6, 0.5), 0, 0, 7.5, DRONE_SPEED, t, WaitTime(i)),
        WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER-6, 0.5), 0, 0, 7.5, DRONE_SPEED, t, WaitTime(i)),
        "r^")
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER-7, 0.5), 0, 0, 8, DRONE_SPEED, t, WaitTime(i)),
        WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER-7, 0.5), 0, 0, 8, DRONE_SPEED, t, WaitTime(i)),
        "r^")
plt.show()
