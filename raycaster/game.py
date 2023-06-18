from raycaster.renderers.pygame_renderer import PygameRenderer
from raycaster.renderers.pysdl2_renderer import PySDL2Renderer
from raycaster.settings import RENDER_STEP
from raycaster.world_map import WorldMap
from raycaster.player import Player
from raycaster.ray import Ray


class Game:
    def __init__(self):
        self.renderer = PySDL2Renderer()
        self.world_map = WorldMap()
        self.player = Player(self.world_map)
        self.render_step = RENDER_STEP

    def main_loop(self):
        while self.renderer.running:
            self.renderer.clear_screen()
            dx, dy, rel_mouse_motion = self.renderer.handle_keys()
            self.player.move(dx, dy, rel_mouse_motion)
            self.render_walls()
            self.renderer.update_screen()
        self.renderer.destroy()

    def render_walls(self):
        ray = None
        start_ray = None

        for column in range(0, self.renderer.width + self.render_step, self.render_step):
            prev_ray = ray
            ray = Ray(column)
            ray.calc_ray_direction(self.player.camera.distance_to_player,
                                   self.player.camera.direction, self.player.direction, self.renderer.width)
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
            elif column >= self.renderer.width:
                self.render_wall_segment(start_ray, prev_ray)

    def render_wall_segment(self, start_ray, end_ray):
        start_points = start_ray.get_line(self.renderer.height)
        end_points = end_ray.get_line(self.renderer.height)
        c = 255 - 100 * start_ray.hit_direction
        self.renderer.render_parallellogram(
            start_points[0], start_points[1], end_points[0], end_points[1], (c, c, c))
