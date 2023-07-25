from raycaster.settings import WIDTH, HEIGHT

from abc import ABC, abstractmethod


class Renderer(ABC):
    def __init__(self):
        self.width, self.height = WIDTH, HEIGHT
        self.clock = None
        self.running = True
        self.fps = -1

    @abstractmethod
    def render_line(self, pt1, pt2, color):
        pass

    @abstractmethod
    def render_rectangle(self, x, y, dx, dy, color):
        pass

    @abstractmethod
    def render_parallelogram(self, top_left, bottom_left, top_right, bottom_right, color):
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

    def set_fps(self, fps):
        self.fps = fps

    @abstractmethod
    def set_mouse_visibility(self, visible):
        pass
