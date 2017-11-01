import matplotlib.pyplot as plt
import numpy as np
from AerialShowMap import *
from func import *
import math

def DragonLine(start_x, start_y, end_x, end_y):
    item = {}
    item['start_x'] = start_x
    item['end_x'] = end_x
    item['start_y'] = start_y
    item['end_y'] = end_y
    return item


def GetLengthOfLine(line_item):
    return np.sqrt((line_item['end_x'] - line_item['start_x'])**2 + (line_item['end_y'] - line_item['start_y'])**2)


drone_id = np.arange(1, 11)
DRONE_NUMBER = 10
drone_speed = 3
num = 1

lines = []
lines.append(DragonLine(0,11,5.5,0))
lines.append(DragonLine(5.5,0,29,4.5))
lines.append(DragonLine(29,4.5,30.5,2))
lines.append(DragonLine(30.5,2,30,13))
lines.append(DragonLine(30,13,33,19))
lines.append(DragonLine(33,19,22.5,19))
lines.append(DragonLine(22.5,19,27.5,32))
lines.append(DragonLine(27.5,32,17,21))
lines.append(DragonLine(17,21,19,31))
lines.append(DragonLine(19,31,0,11))


def AssignLineX(DragonLine, n, id):
    x = DragonLine['start_x'] + (DragonLine['end_x'] - DragonLine['start_x'])*id/n
    return x
def AssignLineY(DragonLine, n, id):
    y = DragonLine['start_y'] + (DragonLine['end_y'] - DragonLine['start_y'])*id/n
    return y


def ReturnPos(x, y):
    pos = {}
    pos['x'] = x
    pos['y'] = y
    return pos





def DrawLine(DragonLine, n, t, id):
    for i in range(1,n):
        posX = WaitAndApproachPosX(0,0, AssignLineX(DragonLine, 10,i),AssignLineY(DragonLine, 10,i), 3, t, WaitTime(id))
        posY = WaitAndApproachPosY(0,0, AssignLineX(DragonLine, 10,i),AssignLineY(DragonLine, 10,i), 3, t, WaitTime(id))
        #print(AssignLine(DragonLine, n, i))
        plt.plot(posX, posY, 'r--')

def AssignDrone(lines, id):
    line_id = 0
    point_id = 0
    relative_id = 0
    points = 0
    while True:
        points = math.floor(GetLengthOfLine(lines[line_id])/SAFETY_DISTANCE)
        point_id = point_id + points
        if id < point_id:
            relative_id =id - (point_id - points)
            break
        line_id = line_id + 1
        if line_id > 9:
            line_id = 9
            break
    return line_id, relative_id, points
#line = DragonLine(2,0,3,5)
t = np.arange(0, 100, 0.1)


for i in range(0,300):
    plt.scatter(AssignLineX(lines[AssignDrone(lines, i)[0]],AssignDrone(lines, i)[2],AssignDrone(lines, i)[1]),
                AssignLineY(lines[AssignDrone(lines, i)[0]],AssignDrone(lines, i)[2],AssignDrone(lines, i)[1]),
                )
    # DrawLine(lines[AssignDrone(lines, i)[0]],AssignDrone(lines, i)[2],t, AssignDrone(lines, i)[1]  )
    # DrawLine(lines[AssignDrone(lines, i)[0]],AssignDrone(lines, i)[2],t, AssignDrone(lines, i)[1]  )
#     DrawLine(lines[i-1], 10, t, i)
    #print(GetLengthOfLine(lines[i]))
    # DrawLine(lines[i-1], 10, t, i)
    # DrawLine(lines[i-1], 10, t, i)
    # DrawLine(lines[i-1], 10, t, i)
    # DrawLine(lines[i-1], 10, t, i)
    # DrawLine(lines[i-1], 10, t, i)
    # DrawLine(lines[i-1], 10, t, i)
    # DrawLine(lines[i-1], 10, t, i)
    # DrawLine(lines[i-1], 10, t, i)
    # DrawLine(lines[i-1], 10, t, i)

# for i in range(0,20):
#     print(AssignDrone(lines, i))

    
plt.show()