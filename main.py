from raycaster.game import Game
from raycaster.renderers.renderer_factory import Renderers
from raycaster.raycasters.raycaster_factory import Raycasters


def main():
    renderer = Renderers.PYGAME
    raycaster = Raycasters.RAYCASTER
    debug = False
    game = Game(renderer, raycaster, debug)
    game.run()


if __name__ == "__main__":
    main()
