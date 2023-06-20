from raycaster.raycasters.raycaster import Raycaster
from raycaster.settings import WIDTH


class PerWallRaycaster(Raycaster):
    def __init__(self, renderer, world_map, player, debug):
        super().__init__(renderer, world_map, player, debug)

    def render_walls(self):
        # TODO: not working fully yet...
        self.renderer.clear_screen()

        start_ray = self.rays[0]
        prev_ray = self.rays[0]
        for ray in self.rays:
            # different coordinate and not lie in line with each other
            if start_ray.map_coordinate[ray.hit_direction] != ray.map_coordinate[ray.hit_direction]:
                # always render with the previous ray because the current ray failed the condition, so it's not the same wall anymore
                self._render_wall_segment(start_ray, prev_ray)
                start_ray = prev_ray

            # same coordinate but different side of cube
            if start_ray.map_coordinate == ray.map_coordinate and start_ray.hit_direction != ray.hit_direction:
                self._render_wall_segment(start_ray, prev_ray)
                start_ray = prev_ray

            # end of screen
            elif ray.column >= WIDTH:
                self._render_wall_segment(start_ray, prev_ray)

            prev_ray = ray
        self.renderer.update_screen()

    def _render_wall_segment(self, start_ray, end_ray):
        start_points = start_ray.get_line()
        end_points = end_ray.get_line()
        c = 255 - 100 * start_ray.hit_direction
        self.renderer.render_parallelogram(
            start_points[0], start_points[1], end_points[0], end_points[1], (c, c, c))

        if self.debug:
            # TODO: fix crash "int() argument must be a string, a bytes-like object or a real number, not 'NoneType'" when debug is True with PySDL2
            self.draw_outlines(
                start_points[0], start_points[1], end_points[0], end_points[1])
