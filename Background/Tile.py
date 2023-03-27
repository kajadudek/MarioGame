import pygame

from setup import *


class Tile:
    def __init__(self):
        self.img = pygame.image.load('./assets/Background/ground_tile.png')
        self.img = pygame.transform.scale(self.img, TILE_SIZE)
        self.collision = True
        self.rect = self.img.get_rect()

    def draw(self, screen, coordinates, screen_boundary):
        self.rect.x = coordinates[0]*TILE_SIZE[0] - screen_boundary
        self.rect.y = coordinates[1]*TILE_SIZE[1]
        self.rect = screen.blit(self.img, self.rect)
