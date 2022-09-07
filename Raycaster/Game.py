import pygame as pg
from Raycaster.Settings import WIDTH, HEIGHT
from Raycaster.WorldMap import WorldMap
from Raycaster.Player import Player
from Raycaster.Ray import Ray
from Raycaster.Wall import Wall

from random import randint

class Game:
    def __init__(self):
        self.running = True
        pg.init()
        self.clock = pg.time.Clock()
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        self.world_map = WorldMap()
        self.player = Player(self.world_map)
        pg.mouse.set_visible(False)
        self.render_step = 1
        self.wall_segments = []


    def main_loop(self):      
        while self.running:
            self.clock.tick()
            delta_time = self.clock.get_rawtime() / 1000
            fps = 1 / delta_time
            pg.display.set_caption(f"Raycaster  FPS: {round(self.clock.get_fps(), 2)}")
            self.handle_keys(delta_time)

            self.screen.fill((0, 0, 0))
            
            self.calculate_wall_segments()
            self.render_wall_segments()

            pg.display.update()

    def calculate_wall_segments(self):
        start_ray = None
        self.wall_segments = []

        for column in range(0, self.width, self.render_step):
            ray = Ray(column, self.player, self.width)
            ray.cast_ray(self.world_map.map)

            if start_ray is None:
                # Start new wall segment
                start_ray = ray
            elif start_ray.hit_direction != ray.hit_direction:
                # End current wall segment
                self.wall_segments.append(Wall(start_ray, ray))
                start_ray = None
            elif column == self.width - 1:
                self.wall_segments.append(Wall(start_ray, ray))
                start_ray = None

    def render_wall_segments(self):
        for wall_segment in self.wall_segments:
            start_points = wall_segment.start_ray.get_line(self.height)
            end_points = wall_segment.end_ray.get_line(self.height)
            pg.draw.polygon(self.screen, (255, 250, 100), [start_points[0], start_points[1], end_points[1], end_points[0]])



    def handle_keys(self, delta_time):
        events = pg.event.get()
        for event in events:
            if event.type == pg.MOUSEMOTION:
                self.player.rotate(event.rel[0] * delta_time)
            elif event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.VIDEORESIZE:
                self.width, self.height = event.w, event.h
                self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
            


        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_z]:
            self.player.move_up(delta_time)

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.player.move_up(-delta_time)

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.player.move_right(delta_time)

        if keys[pg.K_LEFT] or keys[pg.K_q]:
            self.player.move_right(-delta_time)

        if keys[pg.K_ESCAPE]:
            self.running = False

    def on_resize(self):
        pass
