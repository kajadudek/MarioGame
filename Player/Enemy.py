from os.path import join

import pygame

from Player.Player import Player
from setup import *


class Enemy(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.height = height
        self.width = width
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.update_sprite()
        self.onScreen = False
        self.active = True
        self.counter = 0

    def update_player(self):
        if self.onScreen:
            self.y_vel += min(0.8, (self.fall_count / 60) * GRAVITY)
            self.move(0, self.y_vel)
            self.update_sprite()

            self.fall_count += 1

    def hit(self):
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"

    def draw(self, win, screen_boundary=0):
        if self.counter < 150:
            if self.rect.x - screen_boundary + self.width < 2 \
                    or self.rect.x - screen_boundary - 2 > WINDOW_WIDTH:
                self.onScreen = False
                self.hit()
            else:
                self.onScreen = True
            win.blit(self.sprite, (self.rect.x - screen_boundary, self.rect.y))
        else:
            pass

        if not self.active:
            self.counter += 1

    def update_sprite(self):
        sprite_sheet = "characters"

        sprite_sheet_name = self.update_sprite_sheet_name(sprite_sheet)
        sprites = self.sprites[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        ENEMY_ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        if self.direction == "right" and self.active:
            self.rect.x += ENEMY_SPEED
        elif self.direction == "left" and self.active:
            self.rect.x -= ENEMY_SPEED

        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))

    def update_sprite_sheet_name(self, sprite_sheet):
        pass

    def load_sprites(self):
        pass
