import json
import pygame

from pygame import *
from setup import *

from Background.Tile import Tile


class GameEngine:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.listOfObjects = []
        self.f = open('./Background/map.json')
        self.data = json.load(self.f)
        self.screen_boundary = 0
        self.camera_speed = 0
        self.map_width = WINDOW_WIDTH

    def draw(self):

        # TODO - Enable player to move back from the end of the map
        # if self.screen_boundary >= self.map_width - WINDOW_WIDTH:
        #     self.player.moving_screen = False
        #     self.camera_speed = 0

        # Scrolling background
        if (self.player.rect.x >= WINDOW_WIDTH / 2) and self.camera_speed > 0:
            self.screen_boundary += self.camera_speed
        elif (self.player.rect.x <= WINDOW_WIDTH / 2) and self.screen_boundary > 0 and self.camera_speed < 0:
            self.screen_boundary += self.camera_speed

        # Enable player to move back to the edge of map
        if self.screen_boundary == 0:
            self.player.moving_screen = False
            self.camera_speed = 0

        # Draw tiles
        for i, coord in enumerate(self.data['map']['objects']['ground_tile']):
            self.listOfObjects[i].draw(self.screen, coord, self.screen_boundary)

        # Draw player
        self.player.draw(self.screen)

    def check_for_event(self):
        events = pygame.event.get()
        self.input_handler()

        # quit the game
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.player.jump_count < 1:
                    self.player.jump()

    def input_handler(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[K_LEFT]:
            if self.player.moving_screen:
                self.player.rect.x = WINDOW_WIDTH / 2
            else:
                self.player.move(-PLAYER_SPEED, 0)
            self.camera_speed = -PLAYER_SPEED
            self.player.direction = "left"

        elif pressed_key[K_RIGHT]:
            if self.player.moving_screen:
                self.player.rect.x = WINDOW_WIDTH / 2
            else:
                self.player.move(PLAYER_SPEED, 0)
            self.camera_speed = PLAYER_SPEED
            self.player.direction = "right"

        else:
            self.player.x = 0
            self.camera_speed = 0

    def check_for_collision_blocks(self):
        for i in self.data['map']['objects']['ground_tile']:
            tile = Tile()
            tile.draw(self.screen, i, self.screen_boundary)
            self.listOfObjects.append(tile)
            self.map_width = max((i[0]+1)*60, self.map_width)

    def check_if_collision(self, player):
        player_obj = player.rect

        for i, block in enumerate(self.listOfObjects):
            block_obj = block.rect

            if block_obj.colliderect(player_obj):

                # Collision from both sides of the object
                if abs(block_obj.left - player_obj.right) < COLLISION_TOLERANCE:
                    player.move(-PLAYER_SPEED, 0)
                elif abs(block_obj.right - player_obj.left) < COLLISION_TOLERANCE:
                    player.move(PLAYER_SPEED, 0)

                # Player hitting the top of the object
                elif abs(block_obj.top - player_obj.bottom) < FALL_COLLISION_TOLERANCE:
                    # print('collide', block_obj.top, player.rect.bottom)
                    player_obj.bottom = block_obj.top
                    player.landed()

                # Hitting object from the bottom
                elif abs(block_obj.bottom - player_obj.top) < COLLISION_TOLERANCE:
                    player_obj.top = block_obj.bottom
                    player.hit_head()
