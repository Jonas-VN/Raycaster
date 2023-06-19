from raycaster.settings import WIDTH, HEIGHT

from abc import ABC, abstractmethod
from enum import Enum, auto


class Renderer(ABC):
    def __init__(self):
        self.width, self.height = WIDTH, HEIGHT
        self.clock = None
        self.running = True

    @abstractmethod
    def render_line(self, pt1, pt2, color):
        pass

    @abstractmethod
    def render_rectangle(self, x, y, dx, dy, color):
        pass

    @abstractmethod
    def render_parallelogram(self, x, y, dx, dy, color):
        pass

    @abstractmethod
    def update_screen(self):
        pass

    @abstractmethod
    def clear_screen(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def handle_keys(self):
        pass


class Renderers(Enum):
    PYGAME = auto()
    PYSDL2 = auto()
