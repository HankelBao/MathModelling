# numpy
import numpy as np
# pyplot
import matplotlib.pyplot as plt
from AerialShowMap import *

def InitialPos(drone_id, n, d):
    return d * (drone_id - 1) - (n - 1) * d / 2

def WaitTime(drone_id):
    d = SAFETY_DISTANCE
    v = DRONE_SPEED
    return drone_id * d / v

def ApproachPosX(start_x, start_y, end_x, end_y, speed, t):
    step_length = speed / \
        np.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)
    step_length_x = step_length * (end_x - start_x)
    pos_x = start_x + step_length_x * t
    pos_x = np.where(np.absolute(step_length_x) * t > np.absolute(end_x - start_x),
                     end_x, pos_x)
    return pos_x

def ApproachPosY(start_x, start_y, end_x, end_y, speed, t):
    step_length = speed / \
        np.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)
    step_length_y = step_length * (end_y - start_y)
    pos_y = start_y + step_length_y * t
    pos_y = np.where(np.absolute(step_length_y) * t > np.absolute(end_y - start_y),
                     end_y, pos_y)
    return pos_y

def WaitAndApproachPosX(start_x, start_y, end_x, end_y, speed, t, w):
    pos_x = np.where(t < w,
                     start_x,
                     ApproachPosX(start_x, start_y, end_x, end_y, speed, (t - w)))
    return pos_x

def WaitAndApproachPosY(start_x, start_y, end_x, end_y, speed, t, w):
    pos_y = np.where(t < w,
                     start_y,
                     ApproachPosY(start_x, start_y, end_x, end_y, speed, (t - w)))
    return pos_y

def WheelPosX(drone_id, t):
    return CENTER['x'] + R * np.cos(angle * drone_id + DRONE_SPEED / R * t)

def WheelPosY(drone_id, t):
    return CENTER['y'] + R * np.sin(angle * drone_id + DRONE_SPEED / R * t)

def ArriveTime(n, y, r, d, v):
    return np.sqrt((y+r)**2+InitialPos(n/4, n, d)**2)/v + WaitTime(n/4)
