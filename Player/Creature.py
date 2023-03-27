from setup import *


class Creature(object):
    def __init__(self, x, y, screen):
        self.rect = None
        self.screen = screen
        self.x = x
        self.y = y
        self.alive = True
        self.falling_count = 0
