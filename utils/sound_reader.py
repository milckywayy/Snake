import os

from utils.data_bank import Paths


def read_sound_value():
    with open(str(Paths.SOUND_VOLUME_DIRECTORY.value), "r") as f:
        return float(f.read())


def write_sound_value(value):
    with open(str(Paths.SOUND_VOLUME_DIRECTORY.value), "w") as f:
        return f.write(str(value))
