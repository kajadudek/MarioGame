from setup import *


class Settings:
    def __init__(self):
        self.active = False
        self.current_option = 0
        self.list_of_options = {"MUSIC:": TEXT_COLOR,
                                "SOUND EFFECTS:": TEXT_COLOR,
                                "BACK": TEXT_COLOR}
        self.number_of_options = len(self.list_of_options)

    def draw(self, screen):
        # Draw level options
        start_pos = 350
        settings = [" ON", " ON", ""]

        if SoundPlayer.musicOn:
            settings[0] = " ON"
        else:
            settings[0] = " OFF"

        if SoundPlayer.soundOn:
            settings[1] = " ON"
        else:
            settings[1] = " OFF"

        for count, option in enumerate(self.list_of_options):
            screen.blit(MENU_MARIO_FONT.render(option + settings[count], True, self.list_of_options.get(option)),
                        ((WINDOW_WIDTH - 500) / 2 + 20, start_pos))

            start_pos += 70

    def check_for_input(self):
        # Change color of previous option
        for i in self.list_of_options:
            self.list_of_options[i] = TEXT_COLOR

        # Change color of selected option
        if self.current_option == 0:
            selected = "MUSIC:"
        elif self.current_option == 1:
            selected = "SOUND EFFECTS:"
        else:
            selected = "BACK"

        self.list_of_options[selected] = SELECTED_TEXT_COLOR

        events = pygame.event.get()

        for e in events:
            # Select option
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.current_option = (self.current_option - 1) % self.number_of_options
                    if self.current_option < 0:
                        self.current_option = self.number_of_options - 1

                elif e.key == pygame.K_DOWN:
                    self.current_option = (self.current_option + 1) % self.number_of_options

                # Confirm option
                if e.key == pygame.K_RETURN:
                    self.option_action()

                    if self.current_option == 2:
                        return True

            # Quit the game
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

    def option_action(self):
        if self.current_option == 0:
            SoundPlayer.musicOn = not SoundPlayer.musicOn
        elif self.current_option == 1:
            SoundPlayer.soundOn = not SoundPlayer.soundOn
        else:
            self.active = False
