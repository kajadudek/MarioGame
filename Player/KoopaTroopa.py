from os.path import join

from Player.Enemy import Enemy
from Player.Player import flip
from setup import *


class KoopaTroopa(Enemy):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.height = height
        self.width = width
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.update_sprite()
        self.onScreen = False
        self.points = 50

    def load_sprites(self):
        image = "characters.gif"
        path = join(".", "assets", "Player", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        all_sprites = {}

        sprites = []

        # Walk sprite
        for i in range(*self.walk_sprite_coords):
            surface = pygame.Surface((16, 25), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i, 206, 16, 25)
            surface.blit(sprite_sheet, (0, 0), rect)

            sprites.append(pygame.transform.scale(surface, (self.width, self.height)))

        all_sprites[image.replace(".gif", "") + "_walk_right"] = sprites
        all_sprites[image.replace(".gif", "") + "_walk_left"] = flip(sprites)

        sprites = []

        # Dead goomba
        surface = pygame.Surface((16, 16), pygame.SRCALPHA, 32)
        rect = pygame.Rect(333, 214, 16, 18)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale(surface, (50, 40)))

        all_sprites[image.replace(".gif", "") + "_dead"] = sprites

        return all_sprites

    def update_sprite_sheet_name(self, sprite_sheet):
        if self.active:
            sprite_sheet += "_walk"

            if self.direction == "left":
                sprite_sheet += "_left"
            else:
                sprite_sheet += "_right"

        else:
            sprite_sheet += "_dead"

    def update_sprite(self):
        sprite_sheet = "characters"

        if self.active:
            sprite_sheet += "_walk"

            if self.direction == "left":
                sprite_sheet += "_left"
            else:
                sprite_sheet += "_right"

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

