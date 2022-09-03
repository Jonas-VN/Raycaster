from Raycaster.Renderer import Renderer
from Raycaster.WorldMap import WorldMap

class Game:
    def __init__(self):
        self.renderer = Renderer()

    def new_game(self):
        self.world_map = WorldMap(self)

    def run(self):
        pass
    