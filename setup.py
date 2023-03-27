# general settings
import pygame.image

WINDOW_WIDTH = 900 # 60 x 15
WINDOW_HEIGHT = 720 # 60 x 12
BACKGROUND_COLOR = (124, 189, 245)
FPS = 60
icon = pygame.image.load('./assets/MarioIcon.png')


# background settings
TILE_SIZE = (60, 60)

# objects settings
PLAYER_SPEED = 4
GRAVITY = 2
COLLISION_TOLERANCE = 15
FALL_COLLISION_TOLERANCE = 25
ANIMATION_DELAY = 6
