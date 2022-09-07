import pygame as pg
import os

class Texture:
    def __init__(self, path):
        self.path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "src", path)
        print(self.path)
        self.image = pg.image.load(self.path).convert()
        self.width, self. height = self.image.get_size()

