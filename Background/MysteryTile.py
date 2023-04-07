from os.path import join

import pygame
from setup import *
from Background.Tile import Tile


class MysteryTile(Tile):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.active = True

    def load_sprites(self):
        image = "tiles.png"
        path = join(".", "assets", "Background", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        all_sprites = {}

        sprites = []

        # Mystery tile sprite
        for i in range(384, 417, 16):
            y = 0
            surface = pygame.Surface((16, 16), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i, y, self.width, self.height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale(surface, (self.width, self.height)))

        all_sprites[image.replace(".png", "") + "_coin_inside"] = sprites

        sprites = []

        # Deactivated tile sprite
        surface = pygame.Surface((16, 16), pygame.SRCALPHA, 32)
        rect = pygame.Rect(432, 0, self.width, self.height)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale(surface, (self.width, self.height)))

        all_sprites[image.replace(".png", "") + "_deactivated"] = sprites

        return all_sprites

    def update_sprite(self):
        sprite_sheet = "tiles"

        if self.active:
            sprite_sheet += "_coin_inside"
        else:
            sprite_sheet += "_deactivated"

        sprites = self.sprites[sprite_sheet]
        sprite_index = (self.animation_count //
                        ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))

    def hit(self):
        self.active = False
