import pygame

from windows.states.window_state import WindowState
from utils.config import get_color
from windows.interface.button import Button
from windows.interface.text import Text


class MainMenuState(WindowState):
    def __init__(self, window):
        self.active_color = get_color(window.get_config(), 'input-active-color')
        self.inactive_color = get_color(window.get_config(), 'input-inactive-color')
        self.bg_color = get_color(window.get_config(), 'background-color')

        self.buttons = [
            Button((65, 190), 415, 60, 'Play', window.font_medium, self.active_color, self.inactive_color,
                   self.bg_color, window.sfx),
            Button((65, 270), 415, 60, 'Highscore', window.font_medium, self.active_color, self.inactive_color,
                   self.bg_color, window.sfx),
            Button((65, 460), 415, 60, 'Exit game', window.font_medium, self.active_color, self.inactive_color,
                   self.bg_color, window.sfx)]

        self.title = Text((window.resolution[0] / 2, 115), "Snake", window.font_huge, self.inactive_color)

    def handle_event(self, window, event):
        if event.type == pygame.QUIT:
            window.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window.exit(0)

        if self.buttons[0].handle_event(event):
            window.set_state(window.states['game'])
        elif self.buttons[1].handle_event(event):
            window.set_state(window.states['highscore_screen'])
        elif self.buttons[2].handle_event(event):
            window.exit(0)

    def draw(self, window):
        for button in self.buttons:
            button.draw(window.screen)

    def draw_static_background(self, window):
        window.screen.fill(get_color(window.config, 'background-color'))
        self.title.draw(window.screen)

    def reset(self, window):
        pass

    def play_sound(self, window):
        window.sfx.play_music('menu_music')

    def pause_sound(self, window):
        window.sfx.pause_music()
