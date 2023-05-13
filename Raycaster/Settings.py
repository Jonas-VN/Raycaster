import math

"""Screen settings"""
RESOLUTION = WIDTH, HEIGHT = 1600, 900
HALF_HEIGHT = HEIGHT // 2
HALF_WIDTH = WIDTH // 2
RENDER_STEP = 3


"""Player settings"""
PLAYER_START_POSITION = [3 + 1 / math.sqrt(2), 4 - 1 / math.sqrt(2)]
PLAYER_START_DIRECTION = [1 / math.sqrt(2), -1 / math.sqrt(2)]
PLAYER_SPEED = 2.5

"""Camera settings"""
FOV = 90
