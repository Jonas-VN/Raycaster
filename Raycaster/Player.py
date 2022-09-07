from Raycaster.Settings import PLAYER_START_POSITION, PLAYER_START_DIRECTION
from Raycaster.Camera import Camera
import numpy as np
import math

class Player:
    def __init__(self, world_map):
        self.coordinate = np.array(PLAYER_START_POSITION)
        self.direction = np.array(PLAYER_START_DIRECTION)
        self.camera = Camera(self.direction)
        self.world_map = world_map
        self.speed = 2.5

    def rotate(self, delta_x):
        alfa = -math.atan(delta_x / self.camera.distance_to_player)
        rotationmatrix = np.array(
                [
                    [math.cos(alfa), -math.sin(alfa)], 
                    [math.sin(alfa),  math.cos(alfa)]
                ]
            )
        self.direction = np.dot(rotationmatrix, self.direction)
        self.camera.rotate(rotationmatrix)

    def move_up(self, delta_time):
        new_coordinate = self.coordinate + self.direction * delta_time * self.speed
        if self.world_map.check_collision(new_coordinate):
            self.coordinate = new_coordinate

    def move_right(self, delta_time):
        new_coordinate = self.coordinate + self.camera.direction * delta_time * self.speed
        if self.world_map.check_collision(new_coordinate):
            self.coordinate = new_coordinate

        