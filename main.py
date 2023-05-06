import pygame

from Player.Player import Player
from game_engine import GameEngine
from setup import *


def main():
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("MarioGame")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    mario = Player(10, 590, 16, 16)
    engine = GameEngine(surface, mario)
    engine.map_setup()

    while True:
        clock.tick(FPS)
        pygame.display.update()
        surface.fill(BACKGROUND_COLOR)
        mario.update_player()
        engine.check_if_collision(mario)
        engine.draw()
        engine.check_for_event()

        if start_time:
            time_since_enter = (pygame.time.get_ticks() - start_time)//1000
            message = 'TIME: ' + str(time_since_enter)
            surface.blit(FONT.render(message, True, TEXT_COLOR), (20,20))

        if mario.restart:
            mario = Player(10, 590, 16, 16)
            engine = GameEngine(surface, mario)
            engine.map_setup()
            start_time = pygame.time.get_ticks()
            mario.restart = False


if __name__ == "__main__":
    main()
