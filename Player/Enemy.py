from Player.Player import Player
from setup import WINDOW_WIDTH, ENEMY_ANIMATION_DELAY, ENEMY_SPEED, GRAVITY


class Enemy(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.height = height
        self.width = width
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.update_sprite()
        self.onScreen = False
        self.active = True
        self.counter = 0

    def update_player(self):
        if self.onScreen:
            self.y_vel += min(0.8, (self.fall_count / 60) * GRAVITY)
            self.move(0, self.y_vel)
            self.update_sprite()

            self.fall_count += 1

    def hit(self):
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"

    def draw(self, win, screen_boundary=0):
        if self.counter < 150:
            if (
                self.rect.x - screen_boundary + self.width < 2
                or self.rect.x - screen_boundary - 2 > WINDOW_WIDTH
            ):
                self.onScreen = False
                self.hit()
            else:
                self.onScreen = True

            if self.rect.x < 1:
                self.hit()
            win.blit(self.sprite, (self.rect.x - screen_boundary, self.rect.y))
        else:
            pass

        if not self.active:
            self.counter += 1

    def update_sprite(self):
        pass

    def update_sprite_sheet_name(self, sprite_sheet):
        pass

    def load_sprites(self):
        pass
