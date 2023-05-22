import json
from os.path import join

from Background.Castle import Castle
from Background.Pipe import Pipe
from setup import *

from Background.Coin import Coin
from Background.MysteryTile import MysteryTile
from Background.Tile import Tile
from Player.Goomba import Goomba
from Player.KoopaTroopa import KoopaTroopa


class LevelCreator:
    def __init__(self, screen, lvl, player):
        self.screen = screen
        self.map_width = 0
        self.list_of_objects = []
        self.enemies = []
        self.player = player
        map_name = "map_" + str(lvl) + ".json"
        map_path = join("./assets", "Maps", map_name)
        self.f = open(map_path)
        self.data = json.load(self.f)

        self.initial_draw()

    def initial_draw(self):
        for coords in self.data['map']['objects']['ground_tile']:
            tile = Tile(coords)
            tile.draw(self.screen)
            self.list_of_objects.append(tile)
            self.map_width = max((coords[0] + 1) * TILE_SIZE[0], self.map_width)

        for coords in self.data['map']['objects']['coin_tile']:
            tile = MysteryTile(coords)
            tile.draw(self.screen)
            self.list_of_objects.append(tile)
            self.map_width = max((coords[0] + 1) * TILE_SIZE[0], self.map_width)

        for coords in self.data['map']['objects']['coins']:
            tile = Coin(coords)
            tile.draw(self.screen)
            self.list_of_objects.append(tile)

        for coords in self.data['map']['objects']['pipes']:
            tile = Pipe(coords)
            tile.draw(self.screen)
            self.list_of_objects.append(tile)

        for coords in self.data['map']['objects']['castle']:
            castle = Castle(coords, self.player)
            self.list_of_objects.append(castle)

        for coords in self.data['map']['enemies']['goomba']:
            enemy = Goomba(*coords, 50, 50)
            self.enemies.append(enemy)

        for coords in self.data['map']['enemies']['koopa']:
            enemy = KoopaTroopa(*coords, 60, 60)
            self.enemies.append(enemy)
