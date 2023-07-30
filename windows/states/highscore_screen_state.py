import pygame

from windows.states.window_state import WindowState
from utils.config import get_color
from windows.interface.button import Button
from windows.interface.text import Text


class HighscoreScreenState(WindowState):
    def __init__(self, window):
        self.active_color = get_color(window.get_config(), 'input-active-color')
        self.inactive_color = get_color(window.get_config(), 'input-inactive-color')
        self.bg_color = get_color(window.get_config(), 'background-color')

        self.buttons = [Button((65, 460), 415, 60, 'Exit', window.font_medium, self.active_color, self.inactive_color, self.bg_color, window.sfx)]

        self.title = Text((window.resolution[0] / 2, 70), "Highscore", window.font_huge, self.inactive_color, window.resolution[0])
        self.points = Text((window.resolution[0] / 2, 240), "You've got xxx points!", window.font_medium, self.inactive_color, window.resolution[0])
        self.text = Text((window.resolution[0] / 2, 290), "On dd-mm-yyyy", window.font_medium, self.inactive_color, window.resolution[0])

    def handle_event(self, window, event):
        if event.type == pygame.QUIT:
            window.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window.set_state(window.states['main_menu'])

        if self.buttons[0].handle_event(event):
            window.set_state(window.states['main_menu'])

    def draw(self, window):
        for button in self.buttons:
            button.draw(window.screen)

    def draw_static_background(self, window):
        window.screen.fill(get_color(window.config, 'background-color'))
        self.title.draw(window.screen)
        self.points.draw(window.screen)
        self.text.draw(window.screen)

    def reset(self, window):
        pass
