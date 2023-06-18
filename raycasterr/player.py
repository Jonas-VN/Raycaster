from raycaster.settings import PLAYER_START_POSITION, PLAYER_START_DIRECTION, PLAYER_SPEED
from raycaster.camera import Camera

import numpy as np
import math


class Player:
    def __init__(self, world_map):
        self.coordinate = np.array(PLAYER_START_POSITION)
        self.direction = np.array(PLAYER_START_DIRECTION)
        self.camera = Camera(self.direction)
        self.world_map = world_map
        self.speed = PLAYER_SPEED

    def _rotate(self, rel_mouse_motion):
        alfa = -math.atan(rel_mouse_motion / self.camera.distance_to_player)
        rotationmatrix = np.array(
            [
                [math.cos(alfa), -math.sin(alfa)],
                [math.sin(alfa),  math.cos(alfa)]
            ]
        )
        self.direction = np.dot(rotationmatrix, self.direction)
        self.camera.rotate(rotationmatrix)

    def _move_y(self, dy):
        new_coordinate = self.coordinate + self.direction * dy * self.speed
        if self.world_map.check_collision(new_coordinate):
            self.coordinate = new_coordinate

    def _move_x(self, dx):
        new_coordinate = self.coordinate + self.camera.direction * dx * self.speed
        if self.world_map.check_collision(new_coordinate):
            self.coordinate = new_coordinate

    def move(self, dx, dy, rel_mouse_motion):
        self._move_x(dx)
        self._move_y(dy)
        self._rotate(rel_mouse_motion)
