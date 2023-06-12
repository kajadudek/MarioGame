from Background.Tile import Tile
from setup import (
    SoundPlayer,
    SpriteLoader,
    COIN_SIZE,
    ANIMATION_DELAY,
    TILE_SIZE,
)


class Coin(Tile):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.active = True
        self.collision = False
        self.sound = SoundPlayer

    def load_sprites(self):
        return SpriteLoader.coin_sprites(COIN_SIZE)

    def update_sprite(self):
        sprite_sheet = "tiles_coin"

        sprites = self.sprites[sprite_sheet]
        sprite_index = (self.animation_count // ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.sprite.get_rect(
            topleft=(
                self.rect.x + (TILE_SIZE[0] - COIN_SIZE[0]) / 2,
                self.rect.y + (TILE_SIZE[0] - COIN_SIZE[0]) / 2,
            )
        )

    def hit(self):
        self.active = False

    def update_coins(self, coins):
        if self.active:
            self.sound.play(self.sound.coin)
            return coins + 1
        return coins
