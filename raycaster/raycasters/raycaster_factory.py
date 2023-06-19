from raycaster.raycasters.raycaster import Raycaster
from raycaster.raycasters.per_wall_raycaster import PerWallRaycaster
from raycaster.raycasters.per_wall_segment_raycaster import PerWallSegmentRaycaster
from raycaster.raycasters.render_step_rectangle_raycaster import RenderStepRectangleRaycaster
from raycaster.raycasters.render_step_parallelogram_raycaster import RenderStepParallelogramRaycaster
from raycaster.raycasters.per_wall_segment_render_step_raycaster import PerWallSegmentRenderStepRaycaster
from raycaster.renderers.renderer import Renderer
from raycaster.world_map import WorldMap
from raycaster.player import Player

from enum import Enum


class Raycasters(Enum):
    RAYCASTER = Raycaster
    PER_WALL_RAYCASTER = PerWallRaycaster
    PER_WALL_SEGMENT_RAYCASTER = PerWallSegmentRaycaster
    RENDER_STEP_RECTANGLE_RAYCASTER = RenderStepRectangleRaycaster
    RENDER_STEP_PARALLELOGRAM_RAYCASTER = RenderStepParallelogramRaycaster
    PER_WALL_SEGMENT_RENDER_STEP_RAYCASTER = PerWallSegmentRenderStepRaycaster


class RaycasterFactory:
    def __init__(self, raycaster_type: Raycaster = Raycasters.RAYCASTER):
        self.raycaster_type = raycaster_type

    def create_raycaster(self, renderer: Renderer, world_map: WorldMap, player: Player, debug: bool) -> Raycaster:
        if self.raycaster_type not in Raycasters:
            raise ValueError(
                f"Raycaster type {self.raycaster_type} is not supported.")
        raycaster_class = Raycasters(self.raycaster_type).value
        return raycaster_class(renderer, world_map, player, debug)
