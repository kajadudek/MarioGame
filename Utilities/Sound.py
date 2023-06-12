from os.path import join
from pygame import mixer


class Sound:
    def __init__(self):
        mixer.init()
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.2)

        self.soundOn = True
        self.musicOn = True

        path = join("./assets", "Sounds/")
        self.soundtrack = mixer.Sound(path + "main_theme.ogg")
        self.coin = mixer.Sound(path + "coin.ogg")
        self.bump = mixer.Sound(path + "bump.ogg")
        self.stomp = mixer.Sound(path + "stomp.ogg")
        self.jump = mixer.Sound(path + "small_jump.ogg")
        self.death = mixer.Sound(path + "death.wav")
        self.kick = mixer.Sound(path + "kick.ogg")
        self.brick_bump = mixer.Sound(path + "brick-bump.ogg")
        self.powerup = mixer.Sound(path + "powerup.ogg")
        self.powerup_appear = mixer.Sound(path + "powerup_appears.ogg")
        self.pipe = mixer.Sound(path + "pipe.ogg")

    def play(self, sound):
        if self.soundOn:
            self.sfx_channel.play(sound)

    def play_music(self, music):
        if self.musicOn:
            self.music_channel.play(music)
