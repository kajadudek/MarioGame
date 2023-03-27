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

    mario = Player(10, 590, 16, 16)
    engine = GameEngine(surface, mario)
    engine.check_for_collision_blocks()


    while True:
        clock.tick(FPS)
        pygame.display.update()
        surface.fill(BACKGROUND_COLOR)
        mario.update_player()
        engine.check_if_collision(mario)
        engine.draw()
        engine.check_for_event()

if __name__ == "__main__":
    main()
    print("There will be Mario game project")

