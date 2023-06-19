from raycaster.renderers.renderer import Renderer
from raycaster.renderers.pygame_renderer import PyGameRenderer
from raycaster.renderers.pysdl2_renderer import PySDL2Renderer

from enum import Enum


class Renderers(Enum):
    PYGAME = PyGameRenderer
    PYSDL2 = PySDL2Renderer


class RendererFactory:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def create_renderer(self) -> Renderer:
        if self.renderer not in Renderers:
            raise ValueError(
                f"Renderer {self.renderer} is not supported.")
        renderer_class = Renderers(self.renderer).value
        return renderer_class()
