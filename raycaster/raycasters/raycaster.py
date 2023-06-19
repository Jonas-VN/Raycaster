from raycaster.settings import WIDTH
from raycaster.ray import Ray

import numpy as np
from numba import njit
from enum import Enum, auto


class Raycaster:
    def __init__(self, renderer, world_map, player):
        self.renderer = renderer
        self.world_map = world_map
        self.player = player
        self.rays = np.array([Ray(i) for i in range(WIDTH + 1)])

    def render_walls(self):
        self.renderer.clear_screen()
        for ray in self.rays:
            points = ray.get_line()
            c = 255 - 100 * ray.hit_direction
            self.renderer.render_line(points[0], points[1], (c, c, c))
        self.renderer.update_screen()

    def calculate_rays(self):
        for ray in self.rays:
            ray.calculate_ray_direction(
                self.player.camera.distance_to_player, self.player.camera.direction, self.player.direction)
            self.raycast(ray)

    def raycast(self, ray):
        ray.hit_distance, ray.map_coordinate, ray.hit_direction = self._raycast(
            self.player.coordinate, self.player.direction, ray.direction, self.world_map.map)

    @staticmethod
    @njit
    def _raycast(player_coordinate, player_direction, ray_direction, map):
        x = 0
        y = 0
        delta_v = abs(1 / ray_direction[0])
        delta_h = abs(1 / ray_direction[1])
        distance_to_wall = 0
        hit_direction = 0
        if ray_direction[0] < 0:
            vertical_distance = (
                player_coordinate[0] - int(player_coordinate[0])) * delta_v
        else:
            vertical_distance = (
                int(player_coordinate[0]) + 1 - player_coordinate[0]) * delta_v
        if ray_direction[1] < 0:
            horizontal_disctance = (
                player_coordinate[1] - int(player_coordinate[1])) * delta_h
        else:
            horizontal_disctance = (
                int(player_coordinate[1]) + 1 - player_coordinate[1]) * delta_h
        hit = False
        while not hit:
            if vertical_distance + y * delta_v < horizontal_disctance + x * delta_h:
                vertical_intersection = (
                    vertical_distance + y * delta_v) * ray_direction + player_coordinate
                if ray_direction[0] < 0:
                    if map[int(vertical_intersection[1])][round(vertical_intersection[0]) - 1] == 1:
                        distance_to_wall = (
                            vertical_distance + y * delta_v) * np.dot(player_direction, ray_direction)
                        coordinate = [int(vertical_intersection[1]), round(
                            vertical_intersection[0]) - 1]
                        hit_direction = 1
                        hit = True
                else:
                    if map[int(vertical_intersection[1])][round(vertical_intersection[0])] == 1:
                        distance_to_wall = (
                            vertical_distance + y * delta_v) * np.dot(player_direction, ray_direction)
                        coordinate = [int(vertical_intersection[1]),
                                      round(vertical_intersection[0])]
                        hit_direction = 1
                        hit = True

                y += 1
            else:
                horizontal_intersection = (
                    horizontal_disctance + x * delta_h) * ray_direction + player_coordinate
                if ray_direction[1] < 0:
                    if map[round(horizontal_intersection[1]) - 1][int(horizontal_intersection[0])] == 1:
                        distance_to_wall = (
                            horizontal_disctance + x * delta_h) * np.dot(player_direction, ray_direction)
                        coordinate = [
                            round(horizontal_intersection[1]) - 1, int(horizontal_intersection[0])]
                        hit = True

                else:
                    if map[round(horizontal_intersection[1])][int(horizontal_intersection[0])] == 1:
                        distance_to_wall = (
                            horizontal_disctance + x * delta_h) * np.dot(player_direction, ray_direction)
                        coordinate = [round(horizontal_intersection[1]), int(
                            horizontal_intersection[0])]
                        hit = True
                x += 1

        return distance_to_wall, coordinate, hit_direction


class Raycasters(Enum):
    RAYCASTER = auto()
    PER_WALL_SEGMENT_RAYCASTER = auto()
    RENDER_STEP_RECTANGLE_RAYCASTER = auto()
    RENDER_STEP_PARALLELOGRAM_RAYCASTER = auto()