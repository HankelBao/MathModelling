import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from AerialShowMap import *
from func import *

plt.subplot(131)
plt.axis([-40,40,0,80])
for i in range(1, FRAME_DRONE_NUMBER + 1):
    t = np.arange(0, ArriveTime(FRAME_DRONE_NUMBER, FRAME['y'], FRAME['R'], DRONE_SPEED, SAFETY_DISTANCE), 0.1)
    plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FRAME, i, 0), WheelPosY(FRAME, i, 0), DRONE_SPEED, t, WaitTime(i)),
             WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FRAME, i, 0), WheelPosY(FRAME, i, 0), DRONE_SPEED, t, WaitTime(i)),
             "r^")

for i in range(1, 19):
    t = np.arange(0, 10, 0.1)
    plt.plot(ClockPosX(HAND[i], t, ANGULAR_SPEED), ClockPosY(HAND[i], t, ANGULAR_SPEED), "b^")

plt.subplot(132)
plt.axis([-40,40,0,80])
t = np.arange(0, 20, 0.1)
i = 11
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FRAME, i, 0), WheelPosY(FRAME, i, 0), DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FRAME, i, 0), WheelPosY(FRAME, i, 0), DRONE_SPEED, t, WaitTime(i)),
         "r^")

t = np.arange(0, 0, 0.1)
plt.plot(ClockPosX(HAND[i], t, ANGULAR_SPEED), ClockPosY(HAND[i], t, ANGULAR_SPEED), "b^")

plt.subplot(133)
plt.axis([-40,40,0,80])
t = np.arange(0, 0, 0.1)
i = 12
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FRAME, i, 0), WheelPosY(FRAME, i, 0), DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FRAME, i, 0), WheelPosY(FRAME, i, 0), DRONE_SPEED, t, WaitTime(i)),
         "r^")

t = np.arange(0, 30, 0.1)
plt.plot(ClockPosX(HAND[i], t, ANGULAR_SPEED), ClockPosY(HAND[i], t, ANGULAR_SPEED), "b^")

plt.show()