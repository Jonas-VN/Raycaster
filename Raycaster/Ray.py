import numpy as np
from numba import njit
from Raycaster.Settings import WIDTH, HEIGHT
from Raycaster.Raycast import raycast

class Ray:
    def __init__(self, column = 0):
        self.column = column
        self.direction = None
        self.distance_to_wall = None
        self.map_coordinate = None

        # 0 -> horizontal hit
        # 1 -> vertical hit
        self.hit_direction = None

    def cast_ray(self, player_coordinate, player_direction, map):
        self.distance_to_wall, self.map_coordinate, self.hit_direction = raycast(player_coordinate, player_direction, self.direction, map)

    def get_line(self, height):
        length = 1 / self.distance_to_wall * height
        top_point = (self.column, height / 2 + length / 2)
        bottom_point = (self.column, height / 2 - length / 2)
        return top_point, bottom_point

    def calc_ray_direction(self, camera_distance, camera_direction, player_direction, width):
        self.direction = calculate_ray_direction(camera_distance, camera_direction, player_direction, self.column, width)

@njit()
def calculate_ray_direction(distance_to_camera, camera_direction, player_direction, column, width):
    direction_to_column = distance_to_camera * player_direction + (-1 + (2 * column / width)) * camera_direction
    direction = direction_to_column / np.linalg.norm(direction_to_column)
    return direction

