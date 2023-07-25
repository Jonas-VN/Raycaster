from raycaster.states.state import State
from time import sleep


class PausedState(State):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.p_pressed = False

    def init_state(self):
        self.renderer.set_fps(60)
        self.renderer.set_mouse_visibility(True)
        sleep(0.1)

    def handle_frame(self):
        keyboard, delta_time = self.renderer.handle_keys()
        self.renderer.update_screen()
        self.renderer.clear_screen()
        return self.__handle_next_state(keyboard)

    def __handle_next_state(self, keyboard):
        next_state = None
        if not keyboard.P and self.p_pressed:
            next_state = "raycaster_state"
        self.p_pressed = keyboard.P
        return next_state
