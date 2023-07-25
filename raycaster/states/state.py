from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    def init_state(self):
        pass

    @abstractmethod
    def handle_frame(self):
        pass
