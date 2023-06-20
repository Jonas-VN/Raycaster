from raycaster.settings import PLAYER_START_POSITION, PLAYER_START_DIRECTION, PLAYER_SPEED
from raycaster.world_map import WorldMap
from raycaster.keyboard import Keyboard
from raycaster.camera import Camera

import numpy as np
import math


class Player:
    def __init__(self, world_map: WorldMap):
        self.coordinate = np.array(PLAYER_START_POSITION)
        self.direction = np.array(PLAYER_START_DIRECTION)
        self.camera = Camera(self.direction)
        self.world_map = world_map

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
        new_coordinate = self.coordinate + self.direction * dy * PLAYER_SPEED
        if self.world_map.check_collision(new_coordinate):
            self.coordinate = new_coordinate

    def _move_x(self, dx):
        new_coordinate = self.coordinate + self.camera.direction * dx * PLAYER_SPEED
        if self.world_map.check_collision(new_coordinate):
            self.coordinate = new_coordinate

    def move(self, keyboard: Keyboard, delta_time):
        if keyboard.W:
            self._move_y(delta_time)
        if keyboard.S:
            self._move_y(-delta_time)

        if keyboard.D:
            self._move_x(delta_time)
        if keyboard.A:
            self._move_x(-delta_time)

        if keyboard.MOUSE_MOTION:
            self._rotate(keyboard.MOUSE_MOTION * delta_time)
