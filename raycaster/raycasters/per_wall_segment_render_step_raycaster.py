from raycaster.raycasters.per_wall_segment_raycaster import PerWallSegmentRaycaster
from raycaster.settings import RENDER_STEP, WIDTH
from raycaster.ray import Ray

import numpy as np


class PerWallSegmentRenderStepRaycaster(PerWallSegmentRaycaster):
    def __init__(self, renderer, world_map, player, debug):
        super().__init__(renderer, world_map, player, debug)
        self.rays = np.array([Ray(i)
                              for i in range(0, WIDTH + RENDER_STEP, RENDER_STEP)])
