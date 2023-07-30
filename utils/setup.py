import datetime
import os

from utils.data_bank import Paths


def create_game_directory():
    if not os.path.isdir(str(Paths.USERPROFILE_GAME_DIRECTORY.value)):
        os.makedirs(str(Paths.USERPROFILE_GAME_DIRECTORY.value))

    if not os.path.isfile(str(Paths.HIGHSCORE_DIRECTORY.value)):
        with open(str(Paths.HIGHSCORE_DIRECTORY.value), "w") as f:
            f.write("0")
            f.write('\n' + datetime.datetime.now().strftime("%d-%m-%Y"))
