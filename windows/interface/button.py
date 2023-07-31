import pygame



# TODO use text class

class Button:
    def __init__(self, position, width, height, text, font, active_color, inactive_color, bg_color, sfx):
        self.rect = pygame.Rect(position[0], position[1], width, height)

        self.active_color = active_color
        self.inactive_color = inactive_color
        self.current_color = self.inactive_color

        self.text = text
        self.font = font
        self.text_rendered = self.font.render(self.text, True, bg_color)

        self.sfx = sfx
        self.sound = True

    def handle_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
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
        screen.blit(self.text_rendered, (self.rect.x + (self.rect.width / 2) -
                                         (self.text_rendered.get_width() / 2),
                                         self.rect.y + (self.rect.height / 2) -
                                         (self.text_rendered.get_height() / 2)))
