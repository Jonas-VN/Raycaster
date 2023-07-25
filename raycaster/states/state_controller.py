from raycaster.states.raycaster_state import RaycasterState
from raycaster.states.paused_state import PausedState


class StateController:
    def __init__(self, renderer):
        self.renderer = renderer
        self.states = {}
        self.current_state = None

    def init_raycaster_state(self, raycaster, debug):
        self.states["raycaster_state"] = RaycasterState(
            self.renderer, raycaster, debug)
        self.current_state = self.states["raycaster_state"]

    def init_paused_state(self):
        self.states["paused_state"] = PausedState(self.renderer)

    def change_state(self, state):
        self.current_state = self.states[state]
        return self.current_state

    def get_state(self):
        return self.current_state
