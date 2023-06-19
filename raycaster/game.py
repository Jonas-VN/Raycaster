from raycaster.raycasters.raycaster import Raycasters
from raycaster.renderers.renderer import Renderers
from raycaster.world_map import WorldMap
from raycaster.player import Player


class Game:
    def __init__(self, renderer=Renderers.PYGAME, raycaster=Raycasters.RAYCASTER):
        if renderer == Renderers.PYGAME:
            from raycaster.renderers.pygame_renderer import PyGameRenderer
            self.renderer = PyGameRenderer()
        elif renderer == Renderers.PYSDL2:
            from raycaster.renderers.pysdl2_renderer import PySDL2Renderer
            self.renderer = PySDL2Renderer()
        else:
            raise ValueError("Invalid renderer")

        self.world_map = WorldMap()
        self.player = Player(self.world_map)

        if raycaster == Raycasters.RAYCASTER:
            from raycaster.raycasters.raycaster import Raycaster
            self.raycaster = Raycaster(
                self.renderer, self.world_map, self.player)
        elif raycaster == Raycasters.PER_WALL_SEGMENT_RAYCASTER:
            from raycaster.raycasters.per_wall_segment_raycaster import PerWallSegmentRaycaster
            self.raycaster = PerWallSegmentRaycaster(
                self.renderer, self.world_map, self.player)
        else:
            raise ValueError("Invalid raycaster")

    def main_loop(self):
        while self.renderer.running:
            dx, dy, rel_mouse_motion = self.renderer.handle_keys()
            self.player.move(dx, dy, rel_mouse_motion)
            self.raycaster.calculate_rays()
            self.raycaster.render_walls()
        self.renderer.destroy()

    def run(self):
        self.main_loop()
