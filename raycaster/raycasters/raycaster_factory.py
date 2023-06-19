from raycaster.raycasters.raycaster import Raycaster, Raycasters
from raycaster.raycasters.per_wall_segment_raycaster import PerWallSegmentRaycaster
from raycaster.raycasters.render_step_rectangle_raycaster import RenderStepRectangleRaycaster
from raycaster.raycasters.render_step_parallelogram_raycaster import RenderStepParallelogramRaycaster
from raycaster.renderers.renderer import Renderer
from raycaster.world_map import WorldMap
from raycaster.player import Player


class RaycasterFactory:
    def __init__(self, raycaster_type: Raycaster = Raycasters.RAYCASTER):
        self.raycaster_type = raycaster_type
        self.raycaster_classes = {
            Raycasters.RAYCASTER: Raycaster,
            Raycasters.PER_WALL_SEGMENT_RAYCASTER: PerWallSegmentRaycaster,
            Raycasters.RENDER_STEP_RECTANGLE_RAYCASTER: RenderStepRectangleRaycaster,
            Raycasters.RENDER_STEP_PARALLELOGRAM_RAYCASTER: RenderStepParallelogramRaycaster
        }

    def create_raycaster(self, renderer: Renderer, world_map: WorldMap, player: Player) -> Raycaster:
        if self.raycaster_type not in self.raycaster_classes:
            raise ValueError(
                f"Raycaster type {self.raycaster_type} is not supported.")
        return self.raycaster_classes[self.raycaster_type](renderer, world_map, player)
