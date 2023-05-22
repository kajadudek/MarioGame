import time

import pygame.draw
from os.path import join
import pygame
from setup import *


class Player:
    def __init__(self, x, y, width, height):
        self.sprite = None
        self.rect = pygame.Rect(x, y, width, height)
        self.x = 0
        self.y_vel = 0
        self.direction = "right"
        self.win = False
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.moving_screen = False
        self.active = True
        self.sprites = SpriteLoader.player_sprites(width, height)
        self.restart = False
        self.sound = SoundPlayer

        self.walk_sprite_coords = (296, 332, 19)
        self.dead_enemy_sprite_coords = (0, 0, 0)

    def jump(self, height=6):
        self.y_vel -= GRAVITY * height
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

        if height == 6:
            self.sound.play(self.sound.jump)

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

        if self.jump_count > 0:
            sprite_sheet += "_jump"
        elif self.x != 0:
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

    def draw(self, win, screen_boundary=0):
        win.blit(self.sprite, (self.rect.x - screen_boundary, self.rect.y))

    def game_over(self, screen):
        surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        surface.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        surface.set_alpha(128)
        self.sound.music_channel.stop()
        self.sound.play(self.sound.death)

        if self.active:
            for i in range(500, 20, -2):
                surface.fill((0, 0, 0))
                pygame.draw.circle(
                    surface,
                    (255, 255, 255),
                    (self.rect.x + 21, self.rect.y + 16),
                    i)
                screen.blit(surface, (0, 0))
                pygame.display.update()

            time.sleep(0.5)
        self.active = False
        self.restart = True
