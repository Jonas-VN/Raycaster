from raycaster.renderers.renderer import Renderer
from raycaster.keyboard import Keyboard

import pygame


class PyGameRenderer(Renderer):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def render_line(self, pt1, pt2, color):
        pygame.draw.line(self.screen, color, pt1, pt2)

    def render_rectangle(self, x, y, dx, dy, color):
        pygame.draw.rect(self.screen, color, (x, y, dx, dy))

    def render_parallelogram(self, top_left, bottom_left, top_right, bottom_right, color):
        pygame.draw.polygon(self.screen, color, [
                            bottom_left, top_left, top_right, bottom_right])

    def update_screen(self):
        pygame.display.update()

    def clear_screen(self):
        self.screen.fill((0, 0, 0))

    def destroy(self):
        pygame.quit()

    def handle_keys(self):
        keyboard = Keyboard()

        # Lock mouse in the middle of the screen
        if not pygame.mouse.get_visible():
            pygame.mouse.set_pos(self.width // 2, self.height // 2)
            pygame.event.set_grab(True)

        self.clock.tick()
        delta_time = self.clock.get_rawtime() / 1000
        pygame.display.set_caption(
            f"Raycaster  FPS: {int(self.clock.get_fps())}")

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                keyboard.MOUSE_MOTION = event.rel[0]
            elif event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        # I'm using AZERTY so I have to use Z instead of W
        keyboard.W = keys[pygame.K_z] or keys[pygame.K_w]
        # I'm using AZERTY so I have to use Q instead of A
        keyboard.A = keys[pygame.K_q] or keys[pygame.K_a]
        keyboard.S = keys[pygame.K_s]
        keyboard.D = keys[pygame.K_d]
        keyboard.P = keys[pygame.K_p]
        keyboard.ESCAPE = keys[pygame.K_ESCAPE]
        keyboard.UP = keys[pygame.K_UP]
        keyboard.DOWN = keys[pygame.K_DOWN]

        if self.fps != -1:
            self.clock.tick(self.fps)

        return keyboard, delta_time

    def set_mouse_visibility(self, visible):
        pygame.mouse.set_visible(visible)
