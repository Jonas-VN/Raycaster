from raycaster.raycasters.raycaster import Raycaster


class ParallelogramRaycaster(Raycaster):
    def __init__(self, renderer, world_map, player, debug):
        super().__init__(renderer, world_map, player, debug)

    def render_walls(self):
        self.renderer.clear_screen()
        prev_ray = self.rays[0]
        # loop over rays apart from the first one
        for ray in self.rays[1:]:
            self.__render_wall_segment(prev_ray, ray)
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
