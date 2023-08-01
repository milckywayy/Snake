import os
import configparser

from utils.data_bank import Paths


def create_config():
    if not os.path.isfile(Paths.DESIGN_CONFIG_DIRECTORY.value):
        with open(str(Paths.DESIGN_CONFIG_LOCAL_DIRECTORY.value), "r") as f:
            config = f.read()

        with open(str(Paths.DESIGN_CONFIG_DIRECTORY.value), "w") as f:
            f.write(config)

    if not os.path.isfile(Paths.DESIGN_CONFIG_DIRECTORY.value):
        with open(str(Paths.DESIGN_CONFIG_LOCAL_DIRECTORY.value), "r") as f:
            config = f.read()

        with open(str(Paths.GAMEPLAY_CONFIG_DIRECTORY.value), "w") as f:
            f.write(config)

    if not os.path.isfile(Paths.SOUND_VOLUME_DIRECTORY.value):
        with open(str(Paths.SOUND_VOLUME_DIRECTORY.value), "w") as f:
            f.write("1")


def read_config():
    path = str(Paths.DESIGN_CONFIG_DIRECTORY.value)

    config = configparser.RawConfigParser()
    if os.path.isfile(path):
        config.read(path)
        configuration = dict(config.items('Snake configuration'))
        return configuration
    else:
        return False


def get_color(config, name):
    color = list(config[name].split())
    color = [int(i) for i in color]
    return color
