from raycaster.states.state import State
from raycaster.raycasters.raycaster_factory import RaycasterFactory, Raycasters
from raycaster.raycasters.raycaster import Raycaster
from raycaster.renderers.renderer_factory import Renderers
from raycaster.renderers.renderer import Renderer
from time import sleep


class RaycasterState(State):
    def __init__(self, renderer: Renderer = Renderers.PYGAME, raycaster: Raycaster = Raycasters.RAYCASTER, debug: bool = False):
        super().__init__(renderer)
        self.p_pressed = False

        self.raycaster_factory = RaycasterFactory(self.renderer)
        self.raycaster = self.raycaster_factory.create_raycaster(
            raycaster, debug)

    def init_state(self):
        self.renderer.set_fps(-1)
        self.renderer.set_mouse_visibility(False)
        sleep(0.1)

    def handle_frame(self):
        keyboard, delta_time = self.renderer.handle_keys()
        self.raycaster.player.move(keyboard, delta_time)
        self.raycaster.calculate_rays()
        self.raycaster.render_walls()
        return self.__handle_next_state(keyboard)

    def __handle_next_state(self, keyboard):
        next_state = None
        if not keyboard.P and self.p_pressed:
            next_state = "paused_state"
        self.p_pressed = keyboard.P
        return next_state

    def change_raycaster(self, raycaster):
        self.raycaster = self.raycaster_factory.create_raycaster(raycaster)
