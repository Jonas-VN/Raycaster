from raycaster.game import Game
from raycaster.renderers.renderer_factory import Renderers
from raycaster.raycasters.raycaster_factory import Raycasters


def main():
    # renderer = Renderers.PYSDL2
    renderer = Renderers.PYGAME

    # raycaster = Raycasters.RAYCASTER
    # raycaster = Raycasters.PER_WALL_SEGMENT_RAYCASTER
    # raycaster = Raycasters.RENDER_STEP_RECTANGLE_RAYCASTER
    # raycaster = Raycasters.RENDER_STEP_PARALLELOGRAM_RAYCASTER
    # raycaster = Raycasters.PER_WALL_SEGMENT_RENDER_STEP_RAYCASTER
    raycaster = Raycasters.PER_WALL_RAYCASTER

    debug = True

    game = Game(renderer=renderer, raycaster=raycaster, debug=debug)
    game.run()


if __name__ == "__main__":
    main()
