from raycaster.renderers.renderer import Renderer
from raycaster.renderers.pygame_renderer import PyGameRenderer
from raycaster.renderers.pysdl2_renderer import PySDL2Renderer

from enum import Enum


class Renderers(Enum):
    PYGAME = PyGameRenderer
    PYSDL2 = PySDL2Renderer


class RendererFactory:
    def __init__(self):
        pass

    def create_renderer(self, renderer) -> Renderer:
        if renderer not in Renderers:
            raise ValueError(
                f"Renderer {renderer} is not supported.")
        renderer_class = Renderers(renderer).value
        return renderer_class()
