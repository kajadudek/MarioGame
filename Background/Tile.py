import pygame

from setup import *


class Tile:
    def __init__(self, coordinates):
        self.img = pygame.image.load('./assets/Background/ground_tile.png')
        self.img = pygame.transform.scale(self.img, TILE_SIZE)
        self.collision = True
        self.coordinates = coordinates
        self.sprite = self.img
        self.rect = self.img.get_rect()
        self.width = TILE_SIZE[0]
        self.height = TILE_SIZE[1]
        self.points = 0

    def draw(self, screen, screen_boundary=0):
        self.rect.x = self.coordinates[0] * TILE_SIZE[0] - screen_boundary
        self.rect.y = self.coordinates[1] * TILE_SIZE[1]
        self.update_sprite()
        self.rect = screen.blit(self.sprite, self.rect)

    def update_sprite(self):
        pass

    def hit(self):
        pass

    def update_coins(self, coins):
        return coins
