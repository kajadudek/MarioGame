from os import listdir
from os.path import join

import pygame

from setup import (
    TEXT_COLOR,
    MENU_MARIO_FONT,
    WINDOW_WIDTH,
    SELECTED_TEXT_COLOR,
)


def create_list_of_levels():
    path = join("./assets", "Maps")
    number_of_options = len(listdir(path))
    list_of_options = {}

    for i in range(1, number_of_options + 1):
        list_of_options["Level " + str(i)] = TEXT_COLOR

    return list_of_options


class LevelsScreen:
    def __init__(self):
        self.active = False
        self.current_option = 0
        self.list_of_options = create_list_of_levels()
        self.number_of_options = len(self.list_of_options)

    def draw(self, screen):
        # Draw level options
        start_pos = 350
        for i in self.list_of_options:
            screen.blit(
                MENU_MARIO_FONT.render(i, True, self.list_of_options.get(i)),
                ((WINDOW_WIDTH - 500) / 2 + 20, start_pos),
            )

            start_pos += 70

    def check_for_input(self):
        # Change color of previous option
        for i in self.list_of_options:
            self.list_of_options[i] = TEXT_COLOR

        # Change color of selected option
        self.list_of_options[
            "Level " + str(self.current_option + 1)
        ] = SELECTED_TEXT_COLOR

        events = pygame.event.get()

        for e in events:
            # Select option
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.current_option = (
                        self.current_option - 1
                    ) % self.number_of_options
                    if self.current_option < 0:
                        self.current_option = self.number_of_options - 1

                elif e.key == pygame.K_DOWN:
                    self.current_option = (
                        self.current_option + 1
                    ) % self.number_of_options

                # Confirm option
                if e.key == pygame.K_RETURN:
                    return self.current_option + 1

            # Quit the game
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
