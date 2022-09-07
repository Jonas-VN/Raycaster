from dataclasses import dataclass


@dataclass
class Wall:
    def __init__(self, start_ray, end_ray):
        self.start_ray = start_ray
        self.end_ray = end_ray
   