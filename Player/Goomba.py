from os.path import join

from Player.Player import Player
from setup import *


class Goomba(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.height = 16
        self.width = 16
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.active = True
        self.update_sprite()

    def update_player(self):
        self.y_vel += min(0.8, (self.fall_count / 60) * GRAVITY)
        self.move(0, self.y_vel)
        self.update_sprite()

        self.fall_count += 1

    def load_sprites(self):
        image = "characters.gif"
        path = join(".", "assets", "Player", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        all_sprites = {}

        sprites = []

        # Walk sprite
        for i in range(296, 332, 19):
            surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i, 187, self.width, self.height)
            surface.blit(sprite_sheet, (0, 0), rect)

            sprites.append(pygame.transform.scale(surface, (50, 50)))

        all_sprites[image.replace(".gif", "") + "_walk"] = sprites

        sprites = []

        # Dead goomba
        surface = pygame.Surface((16, 12), pygame.SRCALPHA, 32)
        rect = pygame.Rect(277, 191, self.width, 12)
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
        if self.direction == "right":
            self.rect.x += ENEMY_SPEED
        else:
            self.rect.x -= ENEMY_SPEED
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))

    def hit(self):
        print("hit")
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"
