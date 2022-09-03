from Settings import PLAYER_POSITION, PLAYER_DIRECTION

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POSITION
        self.direction = PLAYER_DIRECTION
        