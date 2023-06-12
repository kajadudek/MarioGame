from os.path import join

import pygame
from setup import *
from Background.Tile import Tile


class Pipe(Tile):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.animation_count = 0
        self.sprite = self.load_sprites()
        self.active = True

    def load_sprites(self):
        image = "pipe.png"
        path = join(".", "assets", "Background", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()

        surface = pygame.Surface((260, 650), pygame.SRCALPHA, 32)
        rect = pygame.Rect(300, 45, 600, 800)
        surface.blit(sprite_sheet, (0, 0), rect)

        # Delete white background
        surface.set_colorkey((247, 247, 247))
        surface = surface.convert()

        return pygame.transform.scale(surface, (100, 240))

    def update_sprite(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x + 10, self.rect.y))
