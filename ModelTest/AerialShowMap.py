"""
Public Varibles and Functions
"""
import numpy as np

# Environment Settings

# Varibles for one drone
DRONE_SPEED = 3

# Varibles for drone group
DRONE_NUMBER = 11
SAFETY_DISTANCE = 0.5

# Varibles for FerrisWheel
FERRIS = {}
FERRIS['x'] = 0
FERRIS['y'] = 5
FERRIS['R'] = 4
angle = 2 * np.pi / DRONE_NUMBER
circles = 1

# Varibles for Dragon

# Varibles for Clock
HAND_DISTANCE = SAFETY_DISTANCE


# Functions
