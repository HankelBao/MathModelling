# numpy
import numpy as np
# pyplot
import matplotlib.pyplot as plt
# 3D
from mpl_toolkits.mplot3d import Axes3D
from AerialShowMap import *
from func import *

for i in range(1, FRAME_DRONE_NUMBER + 1):
    t = np.arange(0, ArriveTime(FRAME_DRONE_NUMBER, FRAME['y'], FRAME['R'], DRONE_SPEED, SAFETY_DISTANCE), 0.1)
    plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FRAME, i, 0), WheelPosY(FRAME, i, 0), DRONE_SPEED, t, WaitTime(i)),
             WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FRAME, i, 0), WheelPosY(FRAME, i, 0), DRONE_SPEED, t, WaitTime(i)),
             "r^")

for i in range(1, 4):
    t = np.arange(0, 10, 0.1)
    plt.plot(ClockPosX(HAND[i], t, ANGULAR_SPEED), ClockPosY(HAND[i], t, ANGULAR_SPEED), "b^")

plt.show()
