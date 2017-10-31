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
points.append(0)
points.append(0)
points.append(11)
points.append(5.5)
points.append(0)
points.append(5.5)
points.append(0)
points.append(29)
points.append(4.5)
points.append(29)
points.append(4.5)
points.append(30.5)
points.append(2)
points.append(30.5)
points.append(2)
points.append(30)
points.append(13)
points.append(30)
points.append(13)
points.append(33)
points.append(19)
points.append(33)
points.append(19)
points.append(22.5)
points.append(19)
points.append(22.5)
points.append(19)
points.append(27.5)
points.append(32)
points.append(27.5)
points.append(32)
points.append(17)
points.append(21)
points.append(17)
points.append(21)
points.append(19)
points.append(31)
points.append(19)
points.append(31)
points.append(0)
points.append(11)


def return_pos(x, y):
    pos = {}
    pos['x'] = x
    pos['y'] = y
    return pos


ix = 1
fx = 3
iy = 2
fy = 4


def approchingForDragon(start_x, start_y, end_x, end_y, speed, t):
    step = np.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)
    step_length_x = step * (end_x - start_x)
    step_length_y = step * (end_y - start_y)

    pos_x = start_x + step_length_x * t
    pos_y = start_y + step_length_y * t
    pos_x = np.where(step_length_x * t > (end_x - start_x), end_x, pos_x)
    pos_y = np.where(step_length_y * t > (end_y - start_y), end_y, pos_y)

    return return_pos(pos_x, pos_y)


j = 0.1
while fy <= 40:

    while j <= 1:
        print("running...")
        end_x = points[ix] + ((points[fx] - points[ix]) * j)
        print(points[ix])
        print(points[fx])
        print(points[ix])
        print("0")
        end_y = points[iy] + ((points[fy] - points[iy]) * j)
        print(points[iy])
        print(points[fy])
        print(points[iy])
        print("0")

        t = np.arange(0, 10, 0.001)
        i = 3
        plt.plot(approchingForDragon(0, 0, end_x, end_y, drone_speed, t)['x'],
                 approchingForDragon(0, 0, end_x, end_y, drone_speed, t)['y'], "r--")
        j = j + 0.1
    print(points[ix])
    ix = ix + 2
    fx = fx + 2
    iy = iy + 2
    fy = fy + 2


print("draw")
plt.show()
