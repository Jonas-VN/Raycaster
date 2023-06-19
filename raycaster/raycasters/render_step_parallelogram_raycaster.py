from raycaster.raycasters.raycaster import Raycaster
from raycaster.settings import WIDTH, RENDER_STEP
from raycaster.ray import Ray

import numpy as np


class RenderStepParallelogramRaycaster(Raycaster):
    def __init__(self, renderer, world_map, player):
        super().__init__(renderer, world_map, player)
        self.rays = np.array([Ray(i)
                              for i in range(0, WIDTH + RENDER_STEP, RENDER_STEP)])

    def render_walls(self):
        self.renderer.clear_screen()
        prev_points = self.rays[0].get_line()
        # loop over rays apart from the first one
        for ray in self.rays[1:]:
            points = ray.get_line()
            c = 255 - 100 * ray.hit_direction
            self.renderer.render_parallelogram(
                prev_points[0], prev_points[1], points[0], points[1], (c, c, c))
            prev_points = points
        self.renderer.update_screen()
