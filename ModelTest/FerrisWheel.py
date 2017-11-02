import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from AerialShowMap import *
from func import *

def set_t(time):
    global t
    t = np.arange(0, time, 1)

def set_t_takeoff():
    global t
    t = np.arange(0, ArriveTime(DRONE_NUMBER, FERRIS['y'], FERRIS['R'], DRONE_SPEED, SAFETY_DISTANCE), 1)

def set_t_round():
    global t
    t = np.arange(0, 50, 1)

def set_t_land():
    global t
    t = np.arange(0, ArriveTime(DRONE_NUMBER, FERRIS['y'], FERRIS['R'], DRONE_SPEED, SAFETY_DISTANCE), 1)

plt.subplot(231)
plt.title("Drone Id 155's trail")
plt.axis([-100, 100, 0, 100])
i = 155
set_t_takeoff()
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         "r^")

set_t_round()
plt.plot(WheelPosX(FERRIS, i, t), WheelPosY(FERRIS, i, t), "b^")

set_t_land()
plt.plot(WaitAndApproachPosX(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0,  DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0, DRONE_SPEED, t, WaitTime(i)),
         "r^")

plt.subplot(232)
plt.title("Drone Id 0's trail")
plt.axis([-100, 100, 0, 100])
i = 0
set_t_takeoff()
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         "r^")

set_t_round()
plt.plot(WheelPosX(FERRIS, i, t), WheelPosY(FERRIS, i, t), "b^")

set_t_land()
plt.plot(WaitAndApproachPosX(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0,  DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0, DRONE_SPEED, t, WaitTime(i)),
         "r^")

plt.subplot(233)
plt.title("Trail of all Drones")
plt.axis([-100, 100, 0, 100])
for i in range(1, DRONE_NUMBER + 1):
    set_t_takeoff()
    plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
             WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
             "r^")

    set_t(200)
    plt.plot(WheelPosX(FERRIS, i, t), WheelPosY(FERRIS, i, t), "b^")

    set_t_land()
    plt.plot(WaitAndApproachPosX(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0,  DRONE_SPEED, t, WaitTime(i)),
             WaitAndApproachPosY(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0, DRONE_SPEED, t, WaitTime(i)),
             "r^")

plt.subplot(234)
plt.title("Go to right position in the Ferri in sequence")
plt.axis([-100, 100, 0, 100])
i = 0
set_t(20)
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         "r^")

set_t(0)
plt.plot(WheelPosX(FERRIS, i, t), WheelPosY(FERRIS, i, t), "b^")

set_t(0)
plt.plot(WaitAndApproachPosX(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0,  DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0, DRONE_SPEED, t, WaitTime(i)),
         "r^")
plt.subplot(235)
plt.title("Rotate as part of the Ferri")
plt.axis([-100, 100, 0, 100])
i = 0
set_t(0)
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         "r^")

set_t(20)
plt.plot(WheelPosX(FERRIS, i, t), WheelPosY(FERRIS, i, t), "b^")

set_t(0)
plt.plot(WaitAndApproachPosX(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0,  DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0, DRONE_SPEED, t, WaitTime(i)),
         "r^")
plt.subplot(236)
plt.title("Come back")
plt.axis([-100, 100, 0, 100])
i = 0
set_t(0)
plt.plot(WaitAndApproachPosX(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(InitialPos(i, DRONE_NUMBER, 0.5), 0, WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), DRONE_SPEED, t, WaitTime(i)),
         "r^")

set_t(0)
plt.plot(WheelPosX(FERRIS, i, t), WheelPosY(FERRIS, i, t), "b^")

set_t(20)
plt.plot(WaitAndApproachPosX(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0,  DRONE_SPEED, t, WaitTime(i)),
         WaitAndApproachPosY(WheelPosX(FERRIS, i, 0), WheelPosY(FERRIS, i, 0), InitialPos(i, DRONE_NUMBER, 0.5), 0, DRONE_SPEED, t, WaitTime(i)),
         "r^")
plt.axis([-100, 100, 0, 100])

plt.show()
