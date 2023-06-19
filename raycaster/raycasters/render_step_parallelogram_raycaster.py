from raycaster.raycasters.raycaster import Raycaster
from raycaster.settings import WIDTH, RENDER_STEP
from raycaster.ray import Ray

import numpy as np


class RenderStepParallelogramRaycaster(Raycaster):
    def __init__(self, renderer, world_map, player, debug):
        super().__init__(renderer, world_map, player, debug)
        self.rays = np.array([Ray(i)
                              for i in range(0, WIDTH + RENDER_STEP, RENDER_STEP)])

    def render_walls(self):
        self.renderer.clear_screen()
        prev_ray = self.rays[0]
        # loop over rays apart from the first one
        for ray in self.rays[1:]:
            self._render_wall_segment(prev_ray, ray)
            prev_ray = ray
        self.renderer.update_screen()

    def _render_wall_segment(self, start_ray, end_ray):
        start_points = start_ray.get_line()
        end_points = end_ray.get_line()
        c = 255 - 100 * start_ray.hit_direction
        self.renderer.render_parallelogram(
            start_points[0], start_points[1], end_points[0], end_points[1], (c, c, c))

        if self.debug:
            self.renderer.render_line(
                start_points[0], start_points[1], self.debug_color)
            self.renderer.render_line(
                end_points[0], end_points[1], self.debug_color)
            self.renderer.render_line(
                start_points[0], end_points[0], self.debug_color)
            self.renderer.render_line(
                start_points[1], end_points[1], self.debug_color)
