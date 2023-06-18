from raycaster.settings import FOV

import numpy as np
import math


class Camera:
    def __init__(self, player_direction):
        self.direction = np.array([-player_direction[0], player_direction[1]])
        self.FOV = FOV
        self.distance_to_player = self.fov_to_distance_to_player(self.FOV)

    @staticmethod
    def fov_to_distance_to_player(fov):
        return math.atan(math.radians(fov))

    def rotate(self, rotationmatrix):
        self.direction = np.dot(rotationmatrix, self.direction)
