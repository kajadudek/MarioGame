from setup import SoundPlayer, SpriteLoader, ANIMATION_DELAY
from Background.Tile import Tile


class MysteryTile(Tile):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.animation_count = 0
        self.sprites = self.load_sprites()
        self.active = True
        self.points = 50
        self.sound = SoundPlayer

    def load_sprites(self):
        return SpriteLoader.mystery_tile_sprites(self.width, self.height)

    def update_sprite(self):
        sprite_sheet = "tiles"

        if self.active:
            sprite_sheet += "_coin_inside"
        else:
            sprite_sheet += "_deactivated"

        sprites = self.sprites[sprite_sheet]
        sprite_index = (self.animation_count // ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))

    def hit(self):
        self.active = False

    def update_coins(self, coins):
        if self.active:
            self.sound.play(self.sound.coin)
            return coins + 1
        return coins
