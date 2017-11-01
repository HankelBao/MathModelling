import matplotlib.pyplot as plt
import numpy as np


def dragon_line(start_x, start_y, end_x, end_y):
    item = {}
    item['start_x'] = start_x
    item['end_x'] = end_x
    item['start_y'] = start_y
    item['end_y'] = end_y
    return item


def get_length_of_line(line_item):
    return np.sqrt((line_item['end_x'] - line_item['start_x'])**2 + (line_item['end_y'] - line_item['start_y'])**2)


drone_id = np.arange(1, 11)
DRONE_NUMBER = 10
drone_speed = 3
num = 1
points = []
points.append(dragon_line(0,0,11,5.5))
points.append(dragon_line(0, 5.5, 0,29))
#points.append(4.5)
#points.append(29)
#points.append(4.5)
#points.append(30.5)
#points.append(2)
#points.append(30.5)
#points.append(2)
#points.append(30)
#points.append(13)
#points.append(30)
#points.append(13)
#points.append(33)
#points.append(19)
#points.append(33)
#points.append(19)
#points.append(22.5)
#points.append(19)
#points.append(22.5)
#points.append(19)
#points.append(27.5)
#points.append(32)
#points.append(27.5)
#points.append(32)
#points.append(17)
#points.append(21)
#points.append(17)
#points.append(21)
#points.append(19)
#points.append(31)
#points.append(19)
#points.append(31)
#points.append(0)
#points.append(11)

def asign_line(dragon_line, n, id):
    x = dragon_line['start_x'] + (dragon_line['end_x'] - dragon_line['start_x'])*id/n
    y = dragon_line['start_y'] + (dragon_line['end_y'] - dragon_line['start_y'])*id/n
    return return_pos(x,y)


def return_pos(x, y):
    pos = {}
    pos['x'] = x
    pos['y'] = y
    return pos


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

def draw_line(dragon_line, n, t):
    for i in range(0,n):
        pos = f_approach(0,0, asign_line(dragon_line, n-1,i)['x'],asign_line(dragon_line, n-1,i)['y'], 1, t)
        plt.plot(pos['x'], pos['y'], 'r^')

line = dragon_line(5.5,0,29, 4.5)
t = np.arange(0, 100, 0.1)
draw_line(line, 3, t)
plt.show()
