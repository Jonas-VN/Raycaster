from raycaster.settings import WIDTH, HEIGHT


class Renderer:
    def __init__(self):
        self.width, self.height = WIDTH, HEIGHT
        self.screen = None
        self.clock = None
        self.running = True

    def render_line(self, x, y, x2, y2, color):
        pass

    def render_rectangle(self, x, y, dx, dy, color):
        pass

    def render_parallellogram(self, x, y, dx, dy, color):
        pass

    def update_screen(self):
        pass

    def clear_screen(self):
        pass

    def handle_keys(self):
        pass
