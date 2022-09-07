import pygame
import pygame.gfxdraw
from Raycaster.Settings import WIDTH, HEIGHT
from Raycaster.WorldMap import WorldMap
from Raycaster.Player import Player
from Raycaster.Ray import Ray
from Raycaster.Wall import Wall
from Raycaster.Texture import Texture

class Game:
    def __init__(self):
        self.running = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.world_map = WorldMap()
        self.player = Player(self.world_map)
        pygame.mouse.set_visible(False)
        self.render_step = 5
        self.wall_segments = []
        self.wall_texture = Texture("wall.png")
        self.sign = lambda x: 1 if not x else int(x/abs(x))


    def main_loop(self):      
        while self.running:
            self.clock.tick()
            delta_time = self.clock.get_rawtime() / 1000
            pygame.display.set_caption(f"Raycaster  FPS: {round(self.clock.get_fps(), 2)}")
            self.handle_keys(delta_time)

            self.screen.fill((0, 0, 0))
            
            self.calculate_wall_segments()
            self.render_wall_segments()

            pygame.display.update()

    def calculate_wall_segments(self):
        ray = None
        start_ray = None
        self.wall_segments = []

        for column in range(0, self.width + 1, self.render_step):
            prev_ray = ray
            ray = Ray(column)
            ray.calc_ray_direction(self.player.camera.distance_to_player, self.player.camera.direction, self.player.direction, self.width)
            ray.cast_ray(self.player.coordinate, self.player.direction, self.world_map.map)
            # points = ray.get_line(self.height)
            # c = 255 - 100 * ray.hit_direction
            # pygame.draw.line(self.screen, (c, c, c), points[0], points[1])

            if start_ray is None:
                # Start new wall segment
                start_ray = ray

            elif start_ray.map_coordinate != ray.map_coordinate:
                self.wall_segments.append(Wall(start_ray, prev_ray))
                start_ray = prev_ray

            elif start_ray.map_coordinate == ray.map_coordinate and start_ray.hit_direction != ray.hit_direction:
                self.wall_segments.append(Wall(start_ray, prev_ray))
                start_ray = prev_ray

            elif column == self.width:
                self.wall_segments.append(Wall(start_ray, ray))

    def render_wall_segments(self):
        for wall_segment in self.wall_segments:
            start_points = wall_segment.start_ray.get_line(self.height)
            end_points = wall_segment.end_ray.get_line(self.height)
            c = 255 - 100 * wall_segment.start_ray.hit_direction
            pygame.draw.polygon(self.screen, (c, c, c), [start_points[0], start_points[1], end_points[1], end_points[0]])
            



    def handle_keys(self, delta_time):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                self.player.rotate(event.rel[0] * delta_time)
            elif event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.w, event.h
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
            


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.player.move_up(delta_time)

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.move_up(-delta_time)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move_right(delta_time)

        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.player.move_right(-delta_time)

        if keys[pygame.K_ESCAPE]:
            self.running = False

    def on_resize(self):
        pass
