from raycaster.renderers.renderer import Renderer, Renderers
from raycaster.renderers.pygame_renderer import PyGameRenderer
from raycaster.renderers.pysdl2_renderer import PySDL2Renderer


class RendererFactory:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer
        self.renderer_classes = {
            Renderers.PYGAME: PyGameRenderer,
            Renderers.PYSDL2: PySDL2Renderer
        }

    def create_renderer(self) -> Renderer:
        if self.renderer not in self.renderer_classes:
            raise ValueError(
                f"Renderer {self.renderer} is not supported.")
        return self.renderer_classes[self.renderer]()
