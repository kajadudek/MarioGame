import pygame

from MenuScreens.menu import Menu
from Player.Player import Player
from game_engine import GameEngine
from setup import *


def main():
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("MarioGame")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    selected_level = 1
    mario = Player(10, 590, 16, 16)
    menu = Menu()

    while True:
        clock.tick(FPS)
        pygame.display.update()
        surface.fill(BACKGROUND_COLOR)

        # Menu display
        if menu.active:
            menu.draw(surface)
            selected_level = menu.check_for_input()
            if selected_level:
                engine = GameEngine(surface, mario, selected_level)

        # Game display
        else:
            mario.update_player()
            if engine.collider.check_if_collision():
                engine.win_game()
            engine.draw()
            engine.check_for_event()

            if mario.restart:
                mario = Player(10, 590, 16, 16)
                menu.active = True
                engine = GameEngine(surface, mario, selected_level)
                mario.restart = False


if __name__ == "__main__":
    main()
