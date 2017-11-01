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

lines = []
lines.append(dragon_line(0,11,5.5,0))
lines.append(dragon_line(5.5,0,29,4.5))
lines.append(dragon_line(29,4.5,30.5,2))
lines.append(dragon_line(30.5,2,30,13))
lines.append(dragon_line(30,13,33,19))
lines.append(dragon_line(33,19,22.5,19))
lines.append(dragon_line(22.5,19,27.5,32))
lines.append(dragon_line(27.5,32,17,21))
lines.append(dragon_line(17,21,19,31))
lines.append(dragon_line(19,31,0,11))


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
    for i in range(1,n):
        pos = f_approach(0,0, asign_line(dragon_line, 10,i)['x'],asign_line(dragon_line, 10,i)['y'], 3, t)
        print(asign_line(dragon_line, n, i))
        plt.plot(pos['x'], pos['y'], 'r--')


#line = dragon_line(2,0,3,5)
t = np.arange(0, 100, 0.1)
   
draw_line(lines[0], 10, t)
draw_line(lines[1], 10, t)
draw_line(lines[2], 10, t)
draw_line(lines[3], 10, t)
draw_line(lines[4], 10, t)
draw_line(lines[5], 10, t)
draw_line(lines[6], 10, t)
draw_line(lines[7], 10, t)
draw_line(lines[8], 10, t)
draw_line(lines[9], 10, t)


    
plt.show()