import pygame

from pygame import K_LEFT, K_RIGHT
from time import sleep

from src.Utilities.Collider import Collider
from src.settings import (
    SoundPlayer,
    WINDOW_WIDTH,
    TEXT_COLOR,
    MARIO_FONT,
    PLAYER_SPEED,
    BACKGROUND_COLOR,
)
from Background.LevelCreator import LevelCreator


class GameEngine:
    def __init__(self, screen, player, level):
        self.screen = screen
        self.player = player
        level = LevelCreator(screen, level, player)
        self.list_of_objects = level.list_of_objects
        self.enemies = level.enemies
        self.screen_boundary = 0
        self.camera_speed = 0
        self.map_width = level.map_width
        self.enemy_screen_boundary = 0
        self.collected_coins = 0
        self.points = 0
        pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
        self.end_time = 999
        self.collider = Collider(
            self.screen, self.list_of_objects, self.player
        )
        self.sound = SoundPlayer

    def draw(self):
        # Scrolling background
        if self.player.active:
            if (
                self.player.rect.x >= WINDOW_WIDTH / 2
            ) and self.camera_speed > 0:
                self.screen_boundary += self.camera_speed
            elif (
                (self.player.rect.x <= WINDOW_WIDTH / 2)
                and self.screen_boundary > 0
                and self.camera_speed < 0
            ):
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

        # Draw enemies and check collision
        for i in range(len(self.enemies)):
            self.enemies[i].update_player()
            self.collider.check_for_enemy_collision(
                self.enemies[i], self.screen_boundary
            )
            self.enemies[i].draw(self.screen, self.screen_boundary)

        # Draw stats
        message = "COINS:" + str(self.collider.collected_coins)
        self.screen.blit(
            MARIO_FONT.render(message, True, TEXT_COLOR), (170, 20)
        )

        message = "POINTS:" + str(self.collider.points)
        self.screen.blit(
            MARIO_FONT.render(message, True, TEXT_COLOR), (330, 20)
        )

        if self.start_time:
            if not self.player.win:
                self.end_time = (
                    pygame.time.get_ticks() - self.start_time
                ) // 1000
            message = "TIME:" + str(self.end_time)
            self.screen.blit(
                MARIO_FONT.render(message, True, TEXT_COLOR), (20, 20)
            )

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

    # Check keyboard input
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

    # Player going into the castle animation
    def win_game(self):
        self.sound.music_channel.stop()
        player_position = self.player.x
        while self.player.x < player_position + 350 / 2:
            self.player.move(PLAYER_SPEED, 0)
            sleep(0.03)
            self.player.update_sprite()
            pygame.display.update()
            self.screen.fill(BACKGROUND_COLOR)
            self.draw()

        self.player.win = True
        self.calculate_score()

    # Calculate total score
    def calculate_score(self):
        while self.end_time > 0 or self.collider.collected_coins > 0:
            if self.end_time > 0:
                self.end_time -= 5
            elif self.end_time < 0:
                self.end_time = 0

            if self.collider.collected_coins > 0:
                self.collider.collected_coins -= 1
                self.collider.points += 200

            sleep(0.05)
            pygame.display.update()
            self.screen.fill(BACKGROUND_COLOR)
            self.draw()

        pygame.display.update()
        self.screen.fill(BACKGROUND_COLOR)
        self.draw()

        sleep(0.5)
        self.player.restart = True
