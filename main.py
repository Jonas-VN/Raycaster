from raycaster.game import Game
from raycaster.renderers.renderer import Renderers
from raycaster.raycasters.raycaster import Raycasters


def main():
    renderer = Renderers.PYSDL2
    # renderer = Renderers.PYGAME

    # raycaster = Raycasters.RAYCASTER
    # raycaster = Raycasters.PER_WALL_SEGMENT_RAYCASTER
    raycaster = Raycasters.RENDER_STEP_RECTANGLE_RAYCASTER

    game = Game(renderer=renderer, raycaster=raycaster)
    game.run()


if __name__ == "__main__":
    main()
