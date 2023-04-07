import pygame.draw
from os.path import join
import pygame
from setup import *


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprites(width, height):
    image = "MarioSprite.png"
    path = join("./assets", "Player", image)
    sprite_sheet = pygame.image.load(path).convert_alpha()
    all_sprites = {}

    sprites = []

    # Running sprite
    for i in range(240, 330, 30):
        y = 0
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(i, y, width, height)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale(surface, (50, 50)))

    all_sprites[image.replace(".png", "") + "_run_right"] = sprites
    all_sprites[image.replace(".png", "") + "_run_left"] = flip(sprites)

    sprites = []

    # Idle sprite
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    rect = pygame.Rect(210, 0, width, height)
    surface.blit(sprite_sheet, (0, 0), rect)
    sprites.append(pygame.transform.scale(surface, (50, 50)))

    all_sprites[image.replace(".png", "") + "_idle_right"] = sprites
    all_sprites[image.replace(".png", "") + "_idle_left"] = flip(sprites)

    return all_sprites


class Player:
    def __init__(self, x, y, width, height):
        self.sprite = None
        self.rect = pygame.Rect(x, y, width, height)
        self.x = 0
        self.y_vel = 0
        self.direction = "right"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.moving_screen = False
        self.sprites = load_sprites(width, height)

    def jump(self):
        self.y_vel -= GRAVITY * 6
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        if self.rect.x + dx < 0:
            self.rect.x = 0
        else:
            self.rect.x += dx

        if self.rect.x + dx >= WINDOW_WIDTH - self.rect.width:
            self.rect.x = WINDOW_WIDTH - self.rect.width
        else:
            self.rect.y += dy

        self.x += dx

    def update_player(self):
        self.y_vel += min(0.8, (self.fall_count / 60) * GRAVITY)
        self.move(0, self.y_vel)
        self.update_sprite()

        if self.rect.x >= WINDOW_WIDTH / 2:
            self.moving_screen = True
        else:
            self.moving_screen = False

        self.fall_count += 1

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.y_vel *= -0.2

    def update_sprite(self):
        sprite_sheet = "MarioSprite"

        if self.x != 0:
            sprite_sheet += "_run"
        else:
            sprite_sheet += "_idle"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.sprites[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        MARIO_ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))

    def draw(self, win, screen_boundary = 0):
        win.blit(self.sprite, (self.rect.x, self.rect.y))
