import pygame
import os

from utils.data_bank import Paths


class SoundEffects:
    def __init__(self):
        pygame.mixer.init()
        self.path = str(Paths.SFX_LOCAL_DIRECTORY.value)
        self.music_channel = pygame.mixer.Channel(0)

        self.sfx = {}
        # for file in os.listdir(self.path):
        #     self.sfx[os.path.basename(file).replace('.mp3', '')] = pygame.mixer.Sound(self.path + '/' + file)

        for file in os.listdir(self.path):
            if file.lower().endswith('.mp3') or file.lower().endswith('.wav') or file.lower().endswith('.ogg'):
                sound_name = os.path.splitext(file)[0]
                self.sfx[sound_name] = pygame.mixer.Sound(os.path.join(self.path, file))

    def play_sound(self, sound_name):
        if sound_name in self.sfx:
            pygame.mixer.find_channel(True).play(self.sfx[sound_name])

    def play_music(self, music_name):
        if music_name in self.sfx:
            if self.music_channel.get_sound() == self.sfx[music_name]:
                self.music_channel.unpause()
            else:
                self.music_channel.play(self.sfx[music_name], -1)

    def pause_music(self):
        self.music_channel.pause()

    def stop_music(self):
        self.music_channel.stop()

    def is_music_playing(self):
        return self.music_channel.get_busy()

    def toggle_music(self):
        if self.music_channel.get_volume() <= 0.1:
            self.music_channel.set_volume(1)
        elif self.music_channel.get_volume() >= 0.9:
            self.music_channel.set_volume(0)
