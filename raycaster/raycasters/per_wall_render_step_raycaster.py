from raycaster.ray import Ray
from raycaster.settings import WIDTH, RENDER_STEP
from raycaster.raycasters.per_wall_raycaster import PerWallRaycaster

import numpy as np


class PerWallRenderStepRaycaster(PerWallRaycaster):
    def __init__(self, renderer, world_map, player, debug):
        super().__init__(renderer, world_map, player, debug)
        self.rays = np.array([Ray(i)
                              for i in range(0, WIDTH + RENDER_STEP, RENDER_STEP)])
