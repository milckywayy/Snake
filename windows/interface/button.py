import pygame

from windows.interface.text import Text

# TODO use text class


class Button:
    def __init__(self, position, width, height, text, font, active_color, inactive_color, bg_color, sfx):
        self.rect = pygame.Rect(position[0], position[1], width, height)

        self.active_color = active_color
        self.inactive_color = inactive_color
        self.current_color = self.inactive_color

        self.text = Text((position[0] + (width / 2), position[1] + (height / 2)), text, font, bg_color)

        self.sfx = sfx
        self.sound = True

    def handle_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.sfx.play_sound('click')
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.sfx.play_sound('click')
                return True
            self.current_color = self.active_color
            return False
        else:
            self.current_color = self.inactive_color
            return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect)
        self.text.draw(screen)
