import pygame
from pygame import gfxdraw
import math

from windows.interface.text import Text


class Slider:
    def __init__(self, position, width, height, radius, bg_color, slider_inactive_color, slider_active_color, start_value, font):
        self.position = position
        self.width = width
        self.height = height

        self.bg_color = bg_color
        self.radius = radius

        self.slider_radius = radius * 0.8
        self.slider_y = position[1] + radius
        self.slider_left_limit = position[0] + radius
        self.slider_right_limit = position[0] + width - radius
        self.slider_inactive_color = slider_inactive_color
        self.slider_active_color = slider_active_color
        self.slider_color = slider_inactive_color
        self.slider_x = self.get_slider_x_from_value(start_value)

        self.font = font
        self.value_text = Text(self.get_value_text_position(), str(self.get_value()), font, slider_inactive_color)

        self.sliding = False

    def get_value_text_position(self):
        if self.get_value() >= 0.5:
            return self.position[0] + (self.radius * 2), self.position[1] + self.radius
        else:
            return self.position[0] + self.width - (self.radius * 2), self.position[1] + self.radius

    def distance_from_slider(self, pos):
        return math.sqrt((pos[0] - self.slider_x) ** 2 + (pos[1] - self.slider_y) ** 2)

    def get_value(self):
        slider_range = self.slider_right_limit - self.slider_left_limit
        offset = self.slider_x - self.slider_left_limit
        value = offset / slider_range
        return round(value * 100) / 100

    def get_slider_x_from_value(self, value):
        clamped_value = max(0.0, min(1.0, value))
        slider_range = self.slider_right_limit - self.slider_left_limit
        self.slider_x = self.slider_left_limit + clamped_value * slider_range
        return self.slider_x

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.distance_from_slider(pygame.mouse.get_pos()) < self.slider_radius:
                self.slider_color = self.slider_active_color
                self.sliding = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.slider_color = self.slider_inactive_color
            self.sliding = False

        if self.sliding:
            self.slider_x = pygame.mouse.get_pos()[0]
            if self.slider_x < self.slider_left_limit:
                self.slider_x = self.slider_left_limit
            if self.slider_x > self.slider_right_limit:
                self.slider_x = self.slider_right_limit

            self.value_text.set_text(str(self.get_value()))
            self.value_text.set_position(self.get_value_text_position())
            self.value_text.update_render()
            return True
        else:
            return False

    def draw_background(self, screen):
        pygame.draw.circle(screen, self.bg_color, (self.position[0] + self.radius, self.position[1] + self.radius), self.radius)
        pygame.draw.circle(screen, self.bg_color, (self.position[0] + self.width - self.radius, self.position[1] + self.radius), self.radius)

        pygame.draw.rect(screen, self.bg_color, (self.position[0] + self.radius, self.position[1], self.width - (self.radius * 2), self.height))

    def draw(self, screen):
        self.draw_background(screen)
        self.value_text.draw(screen)

        gfxdraw.aacircle(screen, int(self.slider_x), int(self.slider_y), int(self.slider_radius), self.slider_color)
        gfxdraw.filled_circle(screen, int(self.slider_x), int(self.slider_y), int(self.slider_radius), self.slider_color)
