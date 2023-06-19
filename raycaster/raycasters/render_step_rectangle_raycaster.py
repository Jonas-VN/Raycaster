from raycaster.raycasters.raycaster import Raycaster
from raycaster.ray import Ray
from raycaster.settings import WIDTH, RENDER_STEP


class RenderStepRectangleRaycaster(Raycaster):
    def __init__(self, renderer, world_map, player):
        super().__init__(renderer, world_map, player)
        self.rays = [Ray(i)
                     for i in range(0, WIDTH + RENDER_STEP, RENDER_STEP)]

    def render_walls(self):
        self.renderer.clear_screen()
        for ray in self.rays:
            points = ray.get_line()
            c = 255 - 100 * ray.hit_direction
            self.renderer.render_rectangle(
                points[0][0], points[0][1], RENDER_STEP, points[1][1] - points[0][1], (c, c, c))
        self.renderer.update_screen()
