from Player.Enemy import Enemy
from setup import SpriteLoader, ENEMY_ANIMATION_DELAY, ENEMY_SPEED


class KoopaTroopa(Enemy):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.height = height
        self.width = width
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.update_sprite()
        self.onScreen = False
        self.points = 50

    def load_sprites(self):
        return SpriteLoader.koopa_troopa_sprites(self.width, self.height)

    def update_sprite(self):
        sprite_sheet = "characters"

        if self.active:
            sprite_sheet += "_walk"

            if self.direction == "left":
                sprite_sheet += "_left"
            else:
                sprite_sheet += "_right"

        else:
            sprite_sheet += "_dead"

        sprite_sheet_name = sprite_sheet
        sprites = self.sprites[sprite_sheet_name]
        sprite_index = (self.animation_count // ENEMY_ANIMATION_DELAY) % len(
            sprites
        )
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        if self.direction == "right" and self.active:
            self.rect.x += ENEMY_SPEED
        elif self.direction == "left" and self.active:
            self.rect.x -= ENEMY_SPEED

        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
