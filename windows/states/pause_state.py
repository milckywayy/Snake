import pygame

from windows.states.window_state import WindowState
from utils.config import get_color
from windows.interface.button import Button
from windows.interface.text import Text


class PauseState(WindowState):
    def __init__(self, window):
        self.active_color = get_color(window.get_config(), 'input-active-color')
        self.inactive_color = get_color(window.get_config(), 'input-inactive-color')
        self.bg_color = get_color(window.get_config(), 'background-color')
        self.pause_color = get_color(window.get_config(), 'pause-overlay')

        self.buttons = [Button((65, 235), 415, 60, 'Resume', window.font_medium, self.active_color, self.inactive_color, self.bg_color, window.sfx),
                        Button((65, 460), 415, 60, 'Main menu', window.font_medium, self.active_color, self.inactive_color,  self.bg_color, window.sfx)]

        self.title = Text((window.resolution[0] / 2, 160), "Paused", window.font_huge, self.inactive_color)

    def handle_event(self, window, event):
        if event.type == pygame.QUIT:
            window.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window.set_state(window.states['game'])
        if self.buttons[0].handle_event(event):
            window.set_state(window.states['game'])
        elif self.buttons[1].handle_event(event):
            window.states['game'].reset(window)
            window.set_state(window.states['main_menu'])

    def draw(self, window):
        for button in self.buttons:
            button.draw(window.screen)

    def draw_static_background(self, window):
        overlay = pygame.Surface(window.resolution).convert_alpha()
        overlay.fill(self.pause_color)
        window.screen.blit(overlay, (0, 0))

        self.title.draw(window.screen)

    def reset(self, window):
        pass
