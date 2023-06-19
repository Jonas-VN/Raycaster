from raycaster.raycasters.raycaster_factory import RaycasterFactory, Raycasters
from raycaster.raycasters.raycaster import Raycaster
from raycaster.renderers.renderer_factory import RendererFactory
from raycaster.renderers.renderer import Renderers, Renderer
from raycaster.world_map import WorldMap
from raycaster.player import Player


class Game:
    def __init__(self, renderer: Renderer = Renderers.PYGAME, raycaster: Raycaster = Raycasters.RAYCASTER):
        self.renderer_factory = RendererFactory(renderer)
        self.renderer = self.renderer_factory.create_renderer()

        self.world_map = WorldMap()
        self.player = Player(self.world_map)

        self.raycaster_factory = RaycasterFactory(raycaster)
        self.raycaster = self.raycaster_factory.create_raycaster(
            self.renderer, self.world_map, self.player)

    def main_loop(self):
        while self.renderer.running:
            dx, dy, rel_mouse_motion = self.renderer.handle_keys()
            self.player.move(dx, dy, rel_mouse_motion)
            self.raycaster.calculate_rays()
            self.raycaster.render_walls()
        self.renderer.destroy()

    def run(self):
        self.main_loop()
