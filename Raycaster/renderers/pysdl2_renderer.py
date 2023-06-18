from raycaster.renderers.renderer import Renderer

import sdl2
import sdl2.ext
import numpy as np


class PySDL2Renderer(Renderer):
    def __init__(self):
        super().__init__()
        sdl2.ext.init()
        sdl2.SDL_SetRelativeMouseMode(True)

        self.window = sdl2.ext.Window(
            "Raycaster FPS: 0", size=(self.width, self.height))
        self.window.show()
        self.clock = sdl2.SDL_GetTicks()

    @staticmethod
    def interpolate(start, end):
        steps = np.abs(end[0] - start[0]) + 1
        x = np.linspace(start[0], end[0], steps).astype(int)
        y = np.linspace(start[1], end[1], steps).astype(int)
        return np.vstack([x, y]).T

    def parallellogram_to_rectangles(self, top_left, bottom_left, top_right, bottom_right):
        top = self.interpolate(top_left, top_right)
        bottom = self.interpolate(bottom_left, bottom_right)

        prev = top[0]
        rectangles = []
        for i in range(len(top)):
            if top[i][1] != prev[1]:
                rectangles.append(
                    (prev[0], bottom[i][1], bottom[i][0] - prev[0], prev[1] - bottom[i][1]))
                prev = top[i]

        # Add the last rectangle
        rectangles.append(
            (prev[0], bottom[-1][1], bottom[-1][0] - prev[0], prev[1] - bottom[-1][1]))

        return rectangles

    def render_line(self, pt1, pt2, color):
        sdl2.ext.line(self.window.get_surface(), color,
                      (int(pt1[0]), int(pt1[1]), int(pt2[0]), int(pt2[1])))

    def render_rectangle(self, x, y, dx, dy, color):
        sdl2.ext.fill(self.window.get_surface(),
                      color, (x, y, dx, dy))

    def render_parallellogram(self, top_left, bottom_left, top_right, bottom_right, color):
        # top = self.interpolate(top_left, top_right)
        # bottom = self.interpolate(bottom_left, bottom_right)
        # points = []
        # # (x1, y1, x2, y2, x3, y3, x4, y4, ...)
        # # |  first line  |  second line  | ...
        # for i in range(len(top)):
        #     points.append(top[i][0])
        #     points.append(top[i][1])
        #     points.append(bottom[i][0])
        #     points.append(bottom[i][1])
        # sdl2.ext.line(self.window.get_surface(), color, points)

        rectangles = self.parallellogram_to_rectangles(
            top_left, bottom_left, top_right, bottom_right)

        # When rendering multiple rects this doesn't work even though it should according to the PySDL2 docs?
        # sdl2.ext.fill(self.window.get_surface(), color, rectangles)

        # Workaround but more draw calls...
        for rect in rectangles:
            sdl2.ext.fill(self.window.get_surface(), color, rect)

    def update_screen(self):
        self.window.refresh()

    def clear_screen(self):
        sdl2.ext.fill(self.window.get_surface(), 0)

    def destroy(self):
        sdl2.ext.quit()

    def handle_keys(self):
        dx, dy, rel_mouse_motion = 0, 0, 0

        current = sdl2.SDL_GetTicks()
        delta_time = (current - self.clock) / 1000
        if delta_time == 0:
            delta_time = 1
        self.clock = current

        sdl2.SDL_SetWindowTitle(
            self.window.window, f"Raycaster  FPS: {round(1 / delta_time, 2)}".encode("utf-8"))

        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_MOUSEMOTION:
                rel_mouse_motion = event.motion.xrel * delta_time
            elif event.type == sdl2.SDL_QUIT:
                self.running = False

        keys = sdl2.SDL_GetKeyboardState(None)
        if keys[sdl2.SDL_SCANCODE_W] or keys[sdl2.SDL_SCANCODE_UP]:
            dy = delta_time
        if keys[sdl2.SDL_SCANCODE_S] or keys[sdl2.SDL_SCANCODE_DOWN]:
            dy = -delta_time
        if keys[sdl2.SDL_SCANCODE_D] or keys[sdl2.SDL_SCANCODE_RIGHT]:
            dx = delta_time
        if keys[sdl2.SDL_SCANCODE_A] or keys[sdl2.SDL_SCANCODE_LEFT]:
            dx = -delta_time
        if keys[sdl2.SDL_SCANCODE_ESCAPE]:
            self.running = False

        return dx, dy, rel_mouse_motion
