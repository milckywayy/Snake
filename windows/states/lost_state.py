import pygame
import datetime

from windows.states.window_state import WindowState
from utils.config import get_color
from utils.highscore_reader import write_highscore, read_highscore
from windows.interface.button import Button
from windows.interface.text import Text


class LostState(WindowState):
    def __init__(self, window):
        self.active_color = get_color(window.get_config(), 'input-active-color')
        self.inactive_color = get_color(window.get_config(), 'input-inactive-color')
        self.bg_color = get_color(window.get_config(), 'background-color')

        self.buttons = [Button((65, 380), 415, 60, 'Restart', window.font_medium, self.active_color, self.inactive_color, self.bg_color, window.sfx),
                        Button((65, 460), 415, 60, 'Main menu', window.font_medium, self.active_color, self.inactive_color, self.bg_color, window.sfx)]

        self.title = Text((window.resolution[0] / 2, 115), "Lost", window.font_huge, self.inactive_color)
        self.points = Text((window.resolution[0] / 2, 250), "", window.font_medium, self.inactive_color)
        self.highscore = Text((window.resolution[0] / 2, 300), "", window.font_medium, self.inactive_color)

    def update_score(self, window):
        if window.score.get_previous_score() > int(read_highscore()[0]):
            write_highscore(window.score.get_previous_score(), datetime.datetime.now().strftime("%d-%m-%Y"))

        self.points.set_text("You've got " + str(window.score.get_previous_score()) + " points!")
        self.highscore.set_text("Highscore: " + window.score.get_highscore()[0] + ' points')

    def handle_event(self, window, event):
        if event.type == pygame.QUIT:
            window.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window.set_state(window.states['main_menu'])

        if self.buttons[0].handle_event(event):
            window.set_state(window.states['game'])
        elif self.buttons[1].handle_event(event):
            window.set_state(window.states['main_menu'])

    def draw(self, window):
        for button in self.buttons:
            button.draw(window.screen)

    def draw_static_background(self, window):
        self.update_score(window)

        window.screen.fill(get_color(window.config, 'background-color'))
        self.title.render_n_draw(window.screen)
        self.points.render_n_draw(window.screen)
        self.highscore.render_n_draw(window.screen)

    def reset(self, window):
        pass
