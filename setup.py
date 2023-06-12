# general settings
import pygame.image

from Utilities.Sound import Sound
from Utilities.SpriteLoad import SpriteLoader

pygame.font.init()

WINDOW_WIDTH = 900  # 60 x 15
WINDOW_HEIGHT = 720  # 60 x 12
BACKGROUND_COLOR = (37, 177, 238)
FPS = 60
icon = pygame.image.load("./assets/MarioIcon.png")

# background settings
TILE_SIZE = (60, 60)
COIN_SIZE = (30, 40)

# objects settings
PLAYER_SPEED = 4
ENEMY_SPEED = 2
GRAVITY = 2
COLLISION_TOLERANCE = 15
FALL_COLLISION_TOLERANCE = 25
ENEMY_ANIMATION_DELAY = 20
MARIO_ANIMATION_DELAY = 6
ANIMATION_DELAY = 15

# font
MARIO_FONT = pygame.font.Font("./assets/Fonts/SuperMarioBros.ttf", 16)
MENU_MARIO_FONT = pygame.font.Font("./assets/Fonts/SuperMarioBros.ttf", 28)
TEXT_COLOR = (255, 255, 255)
SELECTED_TEXT_COLOR = (56, 85, 144)

# sounds
SoundPlayer = Sound()

# sprites
SpriteLoader = SpriteLoader()
