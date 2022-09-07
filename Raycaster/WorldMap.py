import numpy as np

_ = False
map = np.array(
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
     ]
)


class WorldMap:
    def __init__(self):
        self.map = map
    
    def check_collision(self, coordinate):
        return not self.map[int(coordinate[1])][int(coordinate[0])]