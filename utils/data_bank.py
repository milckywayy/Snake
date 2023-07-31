import os
from enum import Enum


class Paths(Enum):
    USERPROFILE_DIRECTORY = os.environ['USERPROFILE']

    USERPROFILE_GAME_DIRECTORY = os.path.join(str(USERPROFILE_DIRECTORY), 'Documents\\Snake')
    DESIGN_CONFIG_DIRECTORY = os.path.join(str(USERPROFILE_DIRECTORY), 'Documents\\Snake\\design_config.cfg')
    GAMEPLAY_CONFIG_DIRECTORY = os.path.join(str(USERPROFILE_DIRECTORY), 'Documents\\Snake\\gameplay_config.cfg')
    HIGHSCORE_DIRECTORY = os.path.join(str(USERPROFILE_GAME_DIRECTORY), 'highscore.txt')

    SFX_LOCAL_DIRECTORY = 'resources/sfx'
    DESIGN_CONFIG_LOCAL_DIRECTORY = 'resources/design_config.cfg'
    FONT_LOCAL_DIRECTORY = 'resources/Rajdhani-SemiBold.ttf'
