import json
import pygame

from pygame import *

from Background.Coin import Coin
from Background.MysteryTile import MysteryTile
from Player.KoopaTroopa import KoopaTroopa
from Player.Goomba import Goomba
from setup import *

from Background.Tile import Tile


class GameEngine:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.list_of_objects = []
        self.enemies = []
        self.f = open('./Background/map.json')
        self.data = json.load(self.f)
        self.screen_boundary = 0
        self.camera_speed = 0
        self.map_width = WINDOW_WIDTH
        self.enemy_screen_boundary = 0
        self.collected_coins = 0
        self.points = 0

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
        for i in range(len(self.list_of_objects)):
            self.list_of_objects[i].draw(self.screen, self.screen_boundary)

        # Draw player
        self.player.draw(self.screen)

        for i in range(len(self.enemies)):
            self.enemies[i].update_player()
            self.check_for_enemy_collision(self.enemies[i])
            self.enemies[i].draw(self.screen, self.screen_boundary)

        message = "COINS: " + str(self.collected_coins)
        self.screen.blit(FONT.render(message, True, TEXT_COLOR), (100, 20))

        message = "POINTS: " + str(self.points)
        self.screen.blit(FONT.render(message, True, TEXT_COLOR), (190, 20))

    def check_for_event(self):
        events = pygame.event.get()
        self.input_handler()

        # quit the game
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP and self.player.jump_count < 1:
                    self.player.jump()

    def input_handler(self):
        pressed_key = pygame.key.get_pressed()

        if not self.player.active:
            return

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

    def map_setup(self):
        for coords in self.data['map']['objects']['ground_tile']:
            tile = Tile(coords)
            tile.draw(self.screen, self.screen_boundary)
            self.list_of_objects.append(tile)
            self.map_width = max((coords[0] + 1) * TILE_SIZE[0], self.map_width)

        for coords in self.data['map']['objects']['coin_tile']:
            tile = MysteryTile(coords)
            tile.draw(self.screen, self.screen_boundary)
            self.list_of_objects.append(tile)
            self.map_width = max((coords[0] + 1) * TILE_SIZE[0], self.map_width)

        for coords in self.data['map']['objects']['coins']:
            tile = Coin(coords)
            tile.draw(self.screen, self.screen_boundary)
            self.list_of_objects.append(tile)

        for coords in self.data['map']['enemies']['goomba']:
            enemy = Goomba(*coords, 50, 50)
            self.enemies.append(enemy)

        for coords in self.data['map']['enemies']['koopa']:
            enemy = KoopaTroopa(*coords, 60, 60)
            self.enemies.append(enemy)

    def check_if_collision(self, player):
        player_obj = player.rect

        if player.rect.y > WINDOW_HEIGHT - 20:
            player.game_over(self.screen)
            player.landed()

        for i, block in enumerate(self.list_of_objects):
            block_obj = block.rect
            collect = False

            if block_obj.colliderect(player_obj):

                # Collision from both sides of the object
                if abs(block_obj.left - player_obj.right) < COLLISION_TOLERANCE:
                    if block.collision:
                        player.move(-PLAYER_SPEED, 0)
                    else:
                        collect = True

                elif abs(block_obj.right - player_obj.left) < COLLISION_TOLERANCE:
                    if block.collision:
                        player.move(PLAYER_SPEED, 0)
                    else:
                        collect = True

                # Player hitting the top of the object
                elif abs(block_obj.top - player_obj.bottom) < FALL_COLLISION_TOLERANCE:
                    if block.collision:
                        player_obj.bottom = block_obj.top
                        player.landed()
                    else:
                        collect = True

                # Hitting object from the bottom
                elif abs(block_obj.bottom - player_obj.top) < COLLISION_TOLERANCE:
                    if block.collision:
                        player_obj.top = block_obj.bottom
                        player.hit_head()
                        self.collected_coins = block.update_coins(self.collected_coins)
                        block.hit()
                    else:
                        collect = True

                if collect:
                    self.collected_coins = block.update_coins(self.collected_coins)
                    self.list_of_objects.remove(block)

    def check_for_enemy_collision(self, enemy):
        # Create temporary rect object, that allows us to use colliderect, that has borders of enemy
        # Due to enemy constantly moving and moving screen, we need to create such object
        enemy_obj = pygame.Rect(enemy.rect.x - self.screen_boundary,
                                enemy.rect.y,
                                enemy.rect.height,
                                enemy.rect.width)

        for i, block in enumerate(self.list_of_objects):
            block_obj = block.rect

            if block_obj.colliderect(enemy_obj):

                # Enemy hitting the top of the object - do not change direction because of the tile beneath
                if abs(block_obj.top - enemy_obj.bottom) < FALL_COLLISION_TOLERANCE:
                    if block.collision:
                        enemy.rect.bottom = block_obj.top
                        enemy.landed()

                # Collision from both sides of the object
                elif abs(block_obj.left - enemy_obj.right) < COLLISION_TOLERANCE:
                    if block.collision:
                        enemy.move(-ENEMY_SPEED, 0)
                        enemy.hit()

                elif abs(block_obj.right - enemy_obj.left) < COLLISION_TOLERANCE:
                    if block.collision:
                        enemy.move(ENEMY_SPEED, 0)
                        enemy.hit()

        player_obj = self.player.rect
        if enemy_obj.colliderect(player_obj) and enemy.active:

            # Player hitting the top of the enemy - enemy's death
            if abs(enemy_obj.top + 16 - player_obj.bottom) < COLLISION_TOLERANCE:
                enemy.active = False
                self.points += enemy.points
                player_obj.bottom = enemy_obj.top + 16
                self.player.landed()
                self.player.jump(2)
                return

            # Collision from both sides of the object - player's death
            elif abs(enemy_obj.left - player_obj.right) < COLLISION_TOLERANCE:
                self.player.game_over(self.screen)

            elif abs(enemy_obj.right - player_obj.left) < COLLISION_TOLERANCE:
                self.player.game_over(self.screen)

