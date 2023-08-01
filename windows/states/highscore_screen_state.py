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

        self.buttons = [Button((65, 380), 415, 60, 'Reset highscore', window.font_medium, self.active_color, self.inactive_color, self.bg_color, window.sfx),
                        Button((65, 460), 415, 60, 'Go back', window.font_medium, self.active_color, self.inactive_color, self.bg_color, window.sfx)]

        self.title = Text((window.resolution[0] / 2, 115), "Highscore", window.font_huge, self.inactive_color)
        self.points = Text((window.resolution[0] / 2, 250), "", window.font_medium, self.inactive_color)
        self.date = Text((window.resolution[0] / 2, 300), "", window.font_medium, self.inactive_color)

    def handle_event(self, window, event):
        if event.type == pygame.QUIT:
            window.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window.set_state(window.states['main_menu'])

        if self.buttons[0].handle_event(event):
            window.score.highscore_reset()
            self.draw_static_background(window)
        elif self.buttons[1].handle_event(event):
            window.set_state(window.states['main_menu'])

    def draw(self, window):
        for button in self.buttons:
            button.draw(window.screen)

    def draw_static_background(self, window):
        self.points.set_text("You've reached " + str(window.score.get_highscore()[0]) + " points!")
        self.date.set_text("On: " + str(window.score.get_highscore()[1]))

        window.screen.fill(get_color(window.config, 'background-color'))
        self.title.render_n_draw(window.screen)
        self.points.render_n_draw(window.screen)
        self.date.render_n_draw(window.screen)

    def reset(self, window):
        pass

    def play_sound(self, window):
        window.sfx.play_music('menu_music')

    def pause_sound(self, window):
        window.sfx.pause_music()
