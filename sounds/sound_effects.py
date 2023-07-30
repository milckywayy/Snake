import pygame
import os

from utils.data_bank import Paths


class SoundEffects:
    def __init__(self):
        pygame.mixer.init()
        self.path = str(Paths.SFX_LOCAL_DIRECTORY.value)
        self.music_channel = pygame.mixer.Channel(0)

        self.sfx = {}
        for file in os.listdir(self.path):
            self.sfx[os.path.basename(file).replace('.mp3', '')] = pygame.mixer.Sound(self.path + file)

    def play_sound(self, sound_name):
        if sound_name in self.sfx:
            pygame.mixer.find_channel(True).play(self.sfx[sound_name])

    def play_music(self, music_name):
        if music_name in self.sfx:
            self.music_channel.play(self.sfx[music_name], -1)

    def pause_music(self):
        self.music_channel.pause()

    def unpause_music(self):
        self.music_channel.unpause()

    def is_music_playing(self):
        return self.music_channel.get_busy()

    def toggle_music(self):
        if self.music_channel.get_volume() <= 0.1:
            self.music_channel.set_volume(1)
        elif self.music_channel.get_volume() >= 0.9:
            self.music_channel.set_volume(0)
