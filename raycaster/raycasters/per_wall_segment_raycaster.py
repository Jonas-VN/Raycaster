from raycaster.raycasters.raycaster import Raycaster
from raycaster.settings import WIDTH


class PerWallSegmentRaycaster(Raycaster):
    def __init__(self, renderer, world_map, player, debug):
        super().__init__(renderer, world_map, player, debug)

    def render_walls(self):
        self.renderer.clear_screen()

        start_ray = self.rays[0]
        prev_ray = self.rays[0]
        for ray in self.rays:
            # different coordinate
            if start_ray.map_coordinate != ray.map_coordinate:
                self.__render_wall_segment(start_ray, prev_ray)
                start_ray = prev_ray

            # same coordinate but different side of cube
            elif start_ray.map_coordinate == ray.map_coordinate and start_ray.hit_direction != ray.hit_direction:
                self.__render_wall_segment(start_ray, prev_ray)
                start_ray = prev_ray

            # end of screen
            elif ray.column >= WIDTH:
                self.__render_wall_segment(start_ray, prev_ray)

            prev_ray = ray
        self.renderer.update_screen()

    def __render_wall_segment(self, start_ray, end_ray):
        start_points = start_ray.get_line()
        end_points = end_ray.get_line()
        c = 255 - 100 * start_ray.hit_direction
        self.renderer.render_parallelogram(
            start_points[0], start_points[1], end_points[0], end_points[1], (c, c, c))

        if self.debug:
            self.draw_outlines(
                start_points[0], start_points[1], end_points[0], end_points[1])
