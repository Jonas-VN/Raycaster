from raycaster.raycasters.raycaster_factory import RaycasterFactory, Raycasters
from raycaster.raycasters.raycaster import Raycaster
from raycaster.renderers.renderer_factory import RendererFactory, Renderers
from raycaster.renderers.renderer import Renderer
from raycaster.world_map import WorldMap
from raycaster.player import Player


class Game:
    def __init__(self, renderer: Renderer = Renderers.PYGAME, raycaster: Raycaster = Raycasters.RAYCASTER, debug: bool = False):
        self.renderer_factory = RendererFactory(renderer)
        self.renderer = self.renderer_factory.create_renderer()

        self.world_map = WorldMap()
        self.player = Player(self.world_map)

        self.raycaster_factory = RaycasterFactory(raycaster)
        self.raycaster = self.raycaster_factory.create_raycaster(
            self.renderer, self.world_map, self.player, debug)

    def main_loop(self):
        while self.renderer.running:
            keyboard, delta_time = self.renderer.handle_keys()
            if keyboard.ESCAPE:
                break
            self.player.move(keyboard, delta_time)
            self.raycaster.calculate_rays()
            self.raycaster.render_walls()
        self.renderer.destroy()

    def run(self):
        self.main_loop()
