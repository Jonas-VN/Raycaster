from Raycaster.Settings import WIDTH, HEIGHT, RENDER_STEP
from Raycaster.WorldMap import WorldMap
from Raycaster.Player import Player
from Raycaster.Ray import Ray
from Raycaster.Texture import Texture

import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode(
            (self.width, self.height), pygame.RESIZABLE)

        self.world_map = WorldMap()
        self.player = Player(self.world_map)
        self.wall_texture = Texture("wall.png")

        self.render_step = RENDER_STEP
        self.running = True
        self.delta_time = 1e-9

    def main_loop(self):

        while self.running:
            self.clock.tick()
            self.delta_time = self.clock.get_rawtime() / 1000
            pygame.display.set_caption(
                f"Raycaster  FPS: {round(self.clock.get_fps(), 2)}")
            self.screen.fill((0, 0, 0))

            self.handle_keys()

            self.render_walls()

            pygame.display.update()

    # TODO: full wall segments, not 1 coordinate wall

    def render_walls(self):
        ray = None
        start_ray = None

        for column in range(0, self.width + self.render_step, self.render_step):
            prev_ray = ray
            ray = Ray(column)
            ray.calc_ray_direction(self.player.camera.distance_to_player,
                                   self.player.camera.direction, self.player.direction, self.width)
            ray.cast_ray(self.player.coordinate,
                         self.player.direction, self.world_map.map)

            # just for the start
            if start_ray is None:
                start_ray = ray

            # different coordinate
            elif start_ray.map_coordinate != ray.map_coordinate:
                self.render_wall_segment(start_ray, prev_ray)
                start_ray = prev_ray

            # same coordinate but different side of cube
            elif start_ray.map_coordinate == ray.map_coordinate and start_ray.hit_direction != ray.hit_direction:
                self.render_wall_segment(start_ray, prev_ray)
                start_ray = prev_ray

            # end of screen
            elif column >= self.width:
                self.render_wall_segment(start_ray, prev_ray)

    def render_wall_segment(self, start_ray, end_ray):
        start_points = start_ray.get_line(self.height)
        end_points = end_ray.get_line(self.height)
        c = 255 - 100 * start_ray.hit_direction
        pygame.draw.polygon(self.screen, (c, c, c), [
                            start_points[0], start_points[1], end_points[1], end_points[0]])

    def handle_keys(self):
        # Lock mouse in the middle of the screen
        pygame.mouse.set_pos(self.width // 2, self.height // 2)
        pygame.event.set_grab(True)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                self.player.rotate(event.rel[0] * self.delta_time)
            elif event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.w, event.h
                self.screen = pygame.display.set_mode(
                    (self.width, self.height), pygame.RESIZABLE)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.player.move_up(self.delta_time)

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.move_up(-self.delta_time)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move_right(self.delta_time)

        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.player.move_right(-self.delta_time)

        if keys[pygame.K_ESCAPE]:
            self.running = False
