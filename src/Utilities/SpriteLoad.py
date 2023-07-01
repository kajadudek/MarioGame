from os.path import join
import pygame


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


class SpriteLoader:
    def __init__(self):
        self.path = "./assets"

    def player_sprites(self, width, height):
        image = "MarioSprite.png"
        path = join(self.path, "Player", image)
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

        sprites = []

        # Jump sprite
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(360, 0, width, height)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale(surface, (50, 50)))

        all_sprites[image.replace(".png", "") + "_jump_right"] = sprites
        all_sprites[image.replace(".png", "") + "_jump_left"] = flip(sprites)

        return all_sprites

    def koopa_troopa_sprites(self, width, height):
        image = "characters.gif"
        path = join(self.path, "Player", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        all_sprites = {}

        sprites = []

        # Walk sprite
        for i in range(296, 332, 19):
            surface = pygame.Surface((16, 25), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i, 206, 16, 25)
            surface.blit(sprite_sheet, (0, 0), rect)

            sprites.append(pygame.transform.scale(surface, (width, height)))

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

    def goomba_sprites(self, width, height):
        image = "characters.gif"
        path = join(self.path, "Player", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        all_sprites = {}

        sprites = []

        # Walk sprite
        for i in range(296, 332, 19):
            surface = pygame.Surface((16, 16), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i, 187, 16, 16)
            surface.blit(sprite_sheet, (0, 0), rect)

            sprites.append(pygame.transform.scale(surface, (width, height)))

        all_sprites[image.replace(".gif", "") + "_walk"] = sprites

        sprites = []

        # Dead goomba
        surface = pygame.Surface((16, 12), pygame.SRCALPHA, 32)
        rect = pygame.Rect(277, 191, 16, 12)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale(surface, (50, 40)))

        all_sprites[image.replace(".gif", "") + "_dead"] = sprites

        return all_sprites

    def mystery_tile_sprites(self, width, height):
        image = "tiles.png"
        path = join(self.path, "Background", image)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        all_sprites = {}

        sprites = []

        # Mystery tile sprite
        for i in range(384, 417, 16):
            y = 0
            surface = pygame.Surface((16, 16), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i, y, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale(surface, (width, height)))

        all_sprites[image.replace(".png", "") + "_coin_inside"] = sprites

        sprites = []

        # Deactivated tile sprite
        surface = pygame.Surface((16, 16), pygame.SRCALPHA, 32)
        rect = pygame.Rect(432, 0, width, height)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale(surface, (width, height)))

        all_sprites[image.replace(".png", "") + "_deactivated"] = sprites

        return all_sprites

    def coin_sprites(self, size):
        image = "tiles.png"
        path = join(self.path, "Background", image)
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

            sprites.append(pygame.transform.scale(surface, size))

        all_sprites[image.replace(".png", "") + "_coin"] = sprites

        return all_sprites
