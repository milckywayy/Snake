import pygame

from windows.states.window_state import WindowState
from utils.config import get_color


class MainMenuState(WindowState):
    def __init__(self):
        pass

    def handle_event(self, window, event):
        if event.type == pygame.QUIT:
            window.exit(0)

    def draw(self, window):
        window.get_screen().fill(get_color(window.config, 'background-color'))
