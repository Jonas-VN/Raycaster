from raycaster.settings import WIDTH, HALF_HEIGHT

from numba import njit
import numpy as np


class Ray:
    def __init__(self, column):
        self.column = column
        self.map_coordinate = None
        self.ray_direction = None
        self.hit_direction = None
        self.hit_distance = None

    def calculate_ray_direction(self, distance_to_camera, camera_direction, player_direction):
        self.direction = self._calculate_ray_direction(
            distance_to_camera, camera_direction, player_direction, self.column)

    @staticmethod
    @njit
    def _calculate_ray_direction(distance_to_camera, camera_direction, player_direction, column):
        direction_to_column = distance_to_camera * player_direction + \
            (-1 + (2 * column / WIDTH)) * camera_direction
        direction = direction_to_column / np.linalg.norm(direction_to_column)
        return direction

    def get_line(self):
        return self._get_line(self.hit_distance, self.column)

    @staticmethod
    @njit
    def _get_line(hit_distance, column):
        half_length = 1 / hit_distance * HALF_HEIGHT
        top_point = (column, HALF_HEIGHT - half_length)
        bottom_point = (column, HALF_HEIGHT + half_length)
        return top_point, bottom_point
