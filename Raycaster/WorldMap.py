import numpy as np

_ = False
map = np.array(
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, _, _, _, 1, 1, 1],
        [1, _, _, _, _, 1, 1],
        [1, _, _, _, _, _, 1],
        [1, _, _, _, _, _, 1],
        [1, _, _, _, _, _, 1],
        [1, 1, 1, 1, 1, 1, 1]
     ]
)


class WorldMap:
    def __init__(self, game) -> None:
        self.game = game
        self.map = map
        