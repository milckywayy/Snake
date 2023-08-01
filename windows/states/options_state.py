import pygame

from windows.states.window_state import WindowState
from utils.config import get_color
from windows.interface.button import Button
from windows.interface.text import Text
from windows.interface.slider import Slider


class OptionsState(WindowState):
    def __init__(self, window):
        self.active_color = get_color(window.get_config(), 'input-active-color')
        self.inactive_color = get_color(window.get_config(), 'input-inactive-color')
        self.bg_color = get_color(window.get_config(), 'background-color')

        self.title = Text((window.resolution[0] / 2, 115), "Options", window.font_huge, self.inactive_color)

        self.buttons = [Button((65, 460), 415, 60, 'Go back', window.font_medium, self.active_color, self.inactive_color, self.bg_color, window.sfx)]

        self.sound_slider_text = Text((window.resolution[0] / 2, 220), "Sound volume", window.font_small, self.inactive_color)
        self.sound_slider = Slider((65, 245), 415, 40, 20, self.inactive_color, self.bg_color, self.active_color, window.sfx.get_volume(), window.font_small)

    def handle_event(self, window, event):
        if event.type == pygame.QUIT:
            window.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window.set_state(window.states['main_menu'])

        if self.buttons[0].handle_event(event):
            window.set_state(window.states['main_menu'])

        if self.sound_slider.handle_event(event):
            window.sfx.set_volume(self.sound_slider.get_value())

    def draw(self, window):
        for button in self.buttons:
            button.draw(window.screen)
        self.sound_slider.draw(window.screen)

    def draw_static_background(self, window):
        window.screen.fill(get_color(window.config, 'background-color'))
        self.title.render_n_draw(window.screen)

        self.sound_slider_text.render_n_draw(window.screen)

    def reset(self, window):
        pass

    def play_sound(self, window):
        window.sfx.play_music('menu_music')

    def pause_sound(self, window):
        window.sfx.pause_music()
