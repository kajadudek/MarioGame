from os.path import join

import pygame
from setup import *
from Background.Tile import Tile


class Castle(Tile):
    def __init__(self, coordinates, player):
        super().__init__(coordinates)
        self.animation_count = 0
        self.sprite = self.load_sprites()
        self.active = True
        self.player = player

    def load_sprites(self):
        image = "castle.png"
        path = join(".", "assets", "Background", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()

        surface = pygame.Surface((1200, 1200), pygame.SRCALPHA, 32)
        rect = pygame.Rect(0, 0, 1200, 1200)
        surface.blit(sprite_sheet, (0, 0), rect)
        return pygame.transform.scale(surface, (350, 350))

    def update_sprite(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))

    def hit(self):
        self.player.active = False
