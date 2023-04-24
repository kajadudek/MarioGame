# general settings
import pygame.image
pygame.font.init()

WINDOW_WIDTH = 900 # 60 x 15
WINDOW_HEIGHT = 720 # 60 x 12
BACKGROUND_COLOR = (124, 189, 245)
FPS = 60
icon = pygame.image.load('./assets/MarioIcon.png')


# background settings
TILE_SIZE = (60, 60)
COIN_SIZE = (30, 40)
FONT = pygame.font.SysFont("Sans", 20)
TEXT_COLOR = (0, 0, 0)

# objects settings
PLAYER_SPEED = 4
ENEMY_SPEED = 2
GRAVITY = 2
COLLISION_TOLERANCE = 15
FALL_COLLISION_TOLERANCE = 25
ENEMY_ANIMATION_DELAY = 20
MARIO_ANIMATION_DELAY = 6
ANIMATION_DELAY = 15
