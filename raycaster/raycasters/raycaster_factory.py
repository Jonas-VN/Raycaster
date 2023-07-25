from raycaster.raycasters.raycaster import Raycaster
from raycaster.raycasters.per_wall_raycaster import PerWallRaycaster
from raycaster.raycasters.rectangle_raycaster import RectangleRaycaster
from raycaster.raycasters.per_wall_segment_raycaster import PerWallSegmentRaycaster
from raycaster.raycasters.parallelogram_raycaster import ParallelogramRaycaster
from raycaster.renderers.renderer import Renderer
from raycaster.world_map import WorldMap
from raycaster.player import Player
from enum import Enum


class Raycasters(Enum):
    RAYCASTER = Raycaster
    PER_WALL_RAYCASTER = PerWallRaycaster
    PER_WALL_SEGMENT_RAYCASTER = PerWallSegmentRaycaster
    RECTANGLE_RAYCASTER = RectangleRaycaster
    PARALLELOGRAM_RAYCASTER = ParallelogramRaycaster


class RaycasterFactory:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer
        self.world_map = WorldMap()
        self.player = Player(self.world_map)

    def create_raycaster(self, raycaster_type, debug) -> Raycaster:
        if raycaster_type not in Raycasters:
            raise ValueError(
                f"Raycaster type {raycaster_type} is not supported.")
        raycaster_class = Raycasters(raycaster_type).value
        return raycaster_class(self.renderer, self.world_map, self.player, debug)
