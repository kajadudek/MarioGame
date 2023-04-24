from os.path import join

import self as self

from Background.Tile import Tile
from setup import *


class Coin(Tile):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.active = True
        self.collision = False

    def load_sprites(self):
        image = "tiles.png"
        path = join(".", "assets", "Background", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        all_sprites = {}

        sprites = []

        for i in range(387, 435, 16):
            y = 18
            surface = pygame.Surface((10, 14), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i, y, 10, 14)
            surface.blit(sprite_sheet, (0, 0), rect)

            # Delete white background
            surface.set_colorkey((255, 255, 255))
            surface = surface.convert()

            sprites.append(pygame.transform.scale(surface, COIN_SIZE))

        all_sprites[image.replace(".png", "") + "_coin"] = sprites

        return all_sprites

    def update_sprite(self):
        sprite_sheet = "tiles_coin"

        sprites = self.sprites[sprite_sheet]
        sprite_index = (self.animation_count //
                        ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.sprite.get_rect(topleft=(self.rect.x + (TILE_SIZE[0] - COIN_SIZE[0])/2,
                                                  self.rect.y + (TILE_SIZE[0] - COIN_SIZE[0])/2))

    def hit(self):
        self.active = False

    def update_coins(self, coins):
        if self.active:
            return coins+1
        return coins