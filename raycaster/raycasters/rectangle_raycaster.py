from raycaster.raycasters.raycaster import Raycaster
from raycaster.settings import RENDER_STEP


class RectangleRaycaster(Raycaster):
    def __init__(self, renderer, world_map, player, debug):
        super().__init__(renderer, world_map, player, debug)

    def render_walls(self):
        self.renderer.clear_screen()
        for ray in self.rays:
            self.__render_wall_segment(ray)
        self.renderer.update_screen()

    def __render_wall_segment(self, ray):
        points = ray.get_line()
        c = 255 - 100 * ray.hit_direction
        self.renderer.render_rectangle(
            points[0][0], points[0][1], RENDER_STEP, points[1][1] - points[0][1], (c, c, c))

        if self.debug:
            self.draw_outlines(
                points[0], points[1], (points[0][0] + RENDER_STEP, points[0][1]), (points[1][0] + RENDER_STEP, points[1][1]))
