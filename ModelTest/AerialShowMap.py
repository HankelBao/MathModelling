"""
Public Varibles and Functions
"""
import numpy as np
import math

# Environment Settings

# Varibles for one drone
DRONE_SPEED = 3

# Varibles for drone group
DRONE_NUMBER = 180
SAFETY_DISTANCE = 1.5

# Varibles for FerrisWheel
FERRIS = {}
FERRIS['x'] = 0
FERRIS['y'] = 50
FERRIS['R'] = 40
FERRIS['A'] = 2 * np.pi / DRONE_NUMBER
circles = 1

# Varibles for Dragon

# Varibles for Clock
HAND_DISTANCE = SAFETY_DISTANCE
FRAME_R = 19*1.5
FRAME_DRONE_NUMBER = 180
FRAME = {
    'x': 0,
    "y": 50,
    "R": FRAME_R,
    "A": 2 * np.pi / FRAME_DRONE_NUMBER ,
}

HAND = []
HAND_DRONE_NUMBER = 19
ANGULAR_SPEED = 2 * np.pi / 60
for i in range(0,19):
    HAND.append({
        "x": 0,
        "y": 50,
        "R": HAND_DISTANCE*i,
    })

# Functions
