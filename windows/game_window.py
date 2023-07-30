import pygame
from enum import Enum

from windows.window import Window
from windows.states.main_menu_state import MainMenuState
from sounds.sound_effects import SoundEffects
from utils.config import read_config
from utils.data_bank import Paths


class GameWindow(Window):
    def __init__(self):
        pygame.joystick.init()

        self.config = read_config()
        self.cell_number = 25

        self.window_width = ((self.cell_number * int(self.config['cell-size']))
                             + (int(self.config['outline']) * (self.cell_number + 1)))
        self.window_height = ((self.cell_number * int(self.config['cell-size']))
                              + (int(self.config['outline']) * (self.cell_number + 1)
                                 + int(self.config['score-bar-height'])))

        super().__init__((self.window_width, self.window_height), 60, "Snake alpha")

        self.font_huge = pygame.font.Font(str(Paths.FONT_LOCAL_DIRECTORY.value), int(self.config['font-size-huge']))
        self.font_big = pygame.font.Font(str(Paths.FONT_LOCAL_DIRECTORY.value), int(self.config['font-size-big']))
        self.font_medium = pygame.font.Font(str(Paths.FONT_LOCAL_DIRECTORY.value), int(self.config['font-size-medium']))
        self.font_small = pygame.font.Font(str(Paths.FONT_LOCAL_DIRECTORY.value), int(self.config['font-size-small']))

        self.sfx = SoundEffects()

        class State(Enum):
            MAIN_MENU = MainMenuState(self)
        super().set_state(State.MAIN_MENU.value)

    def get_config(self):
        return self.config
