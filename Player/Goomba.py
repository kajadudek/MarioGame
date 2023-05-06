from os.path import join

from Player.Enemy import Enemy
from setup import *


class Goomba(Enemy):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.height = height
        self.width = width
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.update_sprite()
        self.onScreen = False
        self.points = 100

    def load_sprites(self):
        image = "characters.gif"
        path = join(".", "assets", "Player", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        all_sprites = {}

        sprites = []

        # Walk sprite
        for i in range(*self.walk_sprite_coords):
            surface = pygame.Surface((16, 16), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i, 187, 16, 16)
            surface.blit(sprite_sheet, (0, 0), rect)

            sprites.append(pygame.transform.scale(surface, (self.width, self.height)))

        all_sprites[image.replace(".gif", "") + "_walk"] = sprites

        sprites = []

        # Dead goomba
        surface = pygame.Surface((16, 12), pygame.SRCALPHA, 32)
        rect = pygame.Rect(277, 191, 16, 12)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale(surface, (50, 40)))

        all_sprites[image.replace(".gif", "") + "_dead"] = sprites

        return all_sprites

    def update_sprite(self):
        sprite_sheet = "characters"

        if self.active:
            sprite_sheet += "_walk"
        else:
            sprite_sheet += "_dead"

        sprite_sheet_name = sprite_sheet
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

