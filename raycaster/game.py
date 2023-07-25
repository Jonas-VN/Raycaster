from raycaster.raycasters.raycaster_factory import Raycasters
from raycaster.renderers.renderer_factory import RendererFactory, Renderers
from raycaster.states.state_controller import StateController
from raycaster.raycasters.raycaster_factory import Raycasters
from raycaster.renderers.renderer_factory import Renderers


class Game:
    def __init__(self, renderer: Renderers = Renderers.PYSDL2, raycaster: Raycasters = Raycasters.RAYCASTER, debug: bool = False):
        if debug and renderer == Renderers.PYSDL2:
            raise ValueError(
                "Debug mode is not supported with PySDL2 renderer yet, use PyGame renderer instead for debug mode.")

        self.renderer_factory = RendererFactory()
        self.renderer = self.renderer_factory.create_renderer(renderer)

        self.state_controller = StateController(self.renderer)
        self.state_controller.init_raycaster_state(raycaster, debug)
        self.state_controller.init_paused_state()

        self.current_state = self.state_controller.get_state()

    def __main_loop(self):
        while self.renderer.running:
            next_state = self.current_state.handle_frame()
            if next_state is not None:
                self.current_state = self.state_controller.change_state(
                    next_state)
                self.current_state.init_state()
        self.renderer.destroy()

    def run(self):
        self.__main_loop()
