from raycaster.renderers.renderer import Renderer

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

    def render_parallellogram(self, top_left, bottom_left, top_right, bottom_right, color):
        pygame.draw.polygon(self.screen, color, [
                            bottom_left, top_left, top_right, bottom_right])

    def update_screen(self):
        pygame.display.update()

    def clear_screen(self):
        self.screen.fill((0, 0, 0))

    def destroy(self):
        pygame.quit()

    def handle_keys(self):
        dx, dy, rel_mouse_motion = 0, 0, 0

        # Lock mouse in the middle of the screen
        pygame.mouse.set_pos(self.width // 2, self.height // 2)
        pygame.event.set_grab(True)

        self.clock.tick()
        delta_time = self.clock.get_rawtime() / 1000
        pygame.display.set_caption(
            f"Raycaster  FPS: {int(self.clock.get_fps())}")

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                rel_mouse_motion = event.rel[0] * delta_time
            elif event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] or keys[pygame.K_UP]:
            dy = delta_time
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = -delta_time
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = delta_time
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            dx = -delta_time
        if keys[pygame.K_ESCAPE]:
            self.running = False

        return dx, dy, rel_mouse_motion
