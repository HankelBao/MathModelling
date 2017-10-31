# numpy
import numpy as np
# pyplot
import matplotlib.pyplot as plt
# 3D
from mpl_toolkits.mplot3d import Axes3D


drone_number = 10
drone_speed = 3
angle = 2 * np.pi / drone_number

center = {}
center['x'] = 0
center['y'] = 200
r = 50


def return_pos(x, y):
    pos = {}
    pos['x'] = x
    pos['y'] = y
    return pos


def f_inital_x(drone_id, n, d):
    return d * (drone_id - 1) - (n - 1) * d / 2


def f_finalPos_x(drone_id):
    return center['x'] + r * np.cos(angle * drone_id)


def f_finalPos_y(drone_id):
    return center['y'] + r * np.sin(angle * drone_id)


def f_circle_x(drone_id, t):
    return center['x'] + r * np.cos(angle * drone_id + drone_speed / r * t)


def f_circle_y(drone_id, t):
    return center['y'] + r * np.sin(angle * drone_id + drone_speed / r * t)


def f_approach(start_x, start_y, end_x, end_y, speed, t):
    step_length = speed / \
        np.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)
    step_length_x = step_length * (end_x - start_x)
    step_length_y = step_length * (end_y - start_y)

    pos_x = start_x + step_length_x * t
    pos_y = start_y + step_length_y * t
    pos_x = np.where(np.absolute(step_length_x) * t > np.absolute(end_x - start_x),
                     end_x, pos_x)
    pos_y = np.where(np.absolute(step_length_y) * t > np.absolute(end_y - start_y),
                     end_y, pos_y)

    return return_pos(pos_x, pos_y)


def f_approach_wait(start_x, start_y, end_x, end_y, speed, t, w):
    pos_x = np.where(t < w,
                     start_x,
                     f_approach(start_x, start_y, end_x, end_y, speed, (t - w))['x'])
    pos_y = np.where(t < w,
                     start_y,
                     f_approach(start_x, start_y, end_x, end_y, speed, (t - w))['y'])
    return return_pos(pos_x, pos_y)


def start_time(id):
    return id * 0.5


for i in range(1, drone_number + 1):
    t = np.arange(0, 5, 0.1)
    plt.plot(f_approach_wait(f_inital_x(i, drone_number, 0.5), 0, f_finalPos_x(i), f_finalPos_y(i), drone_speed, t, start_time(i))['x'],
             f_approach_wait(f_inital_x(i, drone_number, 0.5), 0, f_finalPos_x(
                 i), f_finalPos_y(i), drone_speed, t, start_time(i))['y'],
             "r^")
    t = np.arange(0, 5, 0.1)
    plt.plot(f_circle_x(i, t), f_circle_y(i, t), "b--")
    t = np.arange(0, 5, 0.1)
    plt.plot(f_approach_wait(f_finalPos_x(i), f_finalPos_y(i), f_inital_x(i, drone_number, 0.5), 0,  drone_speed, t, start_time(i))['x'],
             f_approach_wait(f_finalPos_x(i), f_finalPos_y(i), f_inital_x(
                 i, drone_number, 0.5), 0, drone_speed, t, start_time(i))['y'],
             "r^")


plt.axis([-100, 100, 0, 300])
plt.show()
