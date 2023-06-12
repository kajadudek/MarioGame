from enum import Enum
from os.path import join

import pygame

from MenuScreens.levels_screen import LevelsScreen
from MenuScreens.settings import Settings
from setup import (
    TEXT_COLOR,
    SoundPlayer,
    WINDOW_WIDTH,
    MENU_MARIO_FONT,
    SELECTED_TEXT_COLOR,
)


class MenuOptions(Enum):
    START_GAME = 0
    LEVEL = 1
    SETTINGS = 2


def create_list_of_options():
    list_of_options = {}

    for i in MenuOptions:
        list_of_options[i.name] = TEXT_COLOR

    return list_of_options


def load_sprites(width, height):
    image = "menu_screen.png"
    path = join(".", "assets", "Menu", image)
    sprite_sheet = pygame.image.load(path).convert_alpha()

    surface = pygame.Surface((180, 88), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 60, 180, 88)
    surface.blit(sprite_sheet, (0, 0), rect)

    # Delete white background
    surface.set_colorkey((255, 0, 220))
    surface = surface.convert()

    return pygame.transform.scale(surface, (width, height))


class Menu:
    def __init__(self):
        self.active = True
        self.current_option = 0
        self.selected_level = 1
        self.title_menu_size = (500, 240)
        self.list_of_options = create_list_of_options()
        self.number_of_options = len(self.list_of_options)
        self.spritesheet = load_sprites(*self.title_menu_size)
        self.levels_screen = LevelsScreen()
        self.settings = Settings()
        self.sound = SoundPlayer

    def draw(self, screen):
        screen.blit(
            self.spritesheet,
            ((WINDOW_WIDTH - self.title_menu_size[0]) / 2, 60),
        )

        if self.levels_screen.active:
            self.levels_screen.draw(screen)
        elif self.settings.active:
            self.settings.draw(screen)
        else:
            # Draw menu options
            start_pos = 350
            for i in self.list_of_options:
                screen.blit(
                    MENU_MARIO_FONT.render(
                        i, True, self.list_of_options.get(i)
                    ),
                    (
                        (WINDOW_WIDTH - self.title_menu_size[0]) / 2 + 20,
                        start_pos,
                    ),
                )

                start_pos += 70

    def check_for_input(self):
        if self.levels_screen.active:
            level = self.levels_screen.check_for_input()

            if level:
                self.selected_level = level
                self.active = False
                self.sound.play_music(self.sound.soundtrack)
                self.levels_screen.active = False
                return level

        elif self.settings.active:
            if self.settings.check_for_input():
                self.settings.active = False

        else:
            # Change color of selected option
            self.list_of_options[
                MenuOptions(self.current_option).name
            ] = SELECTED_TEXT_COLOR

            # Change color of previous option
            self.list_of_options[
                MenuOptions(
                    (self.current_option + 1) % self.number_of_options
                ).name
            ] = TEXT_COLOR
            self.list_of_options[
                MenuOptions(
                    (self.current_option - 1) % self.number_of_options
                ).name
            ] = TEXT_COLOR

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
                        if (
                            MenuOptions(self.current_option)
                            == MenuOptions.START_GAME
                        ):
                            self.active = False
                            self.sound.play_music(self.sound.soundtrack)
                            return self.selected_level

                        if (
                            MenuOptions(self.current_option)
                            == MenuOptions.LEVEL
                        ):
                            self.levels_screen.active = True
                        elif (
                            MenuOptions(self.current_option)
                            == MenuOptions.SETTINGS
                        ):
                            self.settings.active = True

                # Quit the game
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
