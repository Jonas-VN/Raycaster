from Raycaster.Settings import FOV
import numpy as np
import math

class Camera:
    def __init__(self, player_direction):
        self.direction = np.array([-player_direction[0], player_direction[1]])
        self.FOV = FOV
        self.distance_to_player = 0
        self._fov_to_distance_to_player()

    def _fov_to_distance_to_player(self):
        self.distance_to_player = math.atan(math.radians(self.FOV))

    def rotate(self, rotationmatrix):
        self.direction = np.dot(rotationmatrix, self.direction)


if __name__ == '__main__':
    camera = Camera([0,0])
    print(camera.FOV)
    print(camera.distance_to_player)
    camera.FOV = 45
    camera._fov_to_distance_to_player()
    print(camera.FOV)
    print(camera.distance_to_player)