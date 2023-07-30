import os
from enum import Enum


class Paths(Enum):
    USERPROFILE_DIRECTORY = os.environ['USERPROFILE']

    USERPROFILE_GAME_DIRECTORY = os.path.join(str(USERPROFILE_DIRECTORY), 'Documents\\Snake')
    DESIGN_CONFIG_DIRECTORY = os.path.join(str(USERPROFILE_DIRECTORY), 'Documents\\Snake\\snake_config.cfg')
    HIGHSCORE_DIRECTORY = os.path.join(str(USERPROFILE_GAME_DIRECTORY), 'highscore.txt')

    DESIGN_CONFIG_LOCAL_DIRECTORY = 'resources/design_config'
    FONT_LOCAL_DIRECTORY = 'resources/Rajdhani-SemiBold.ttf'

    SFX_LOCAL_DIRECTORY = 'resources/sfx'

