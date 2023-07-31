import pygame

from windows.interface.text import Text


class ScoreBar:
    def __init__(self, score_obj, position, width, height, bg_color, font, text_color):
        self.score_obj = score_obj
        self.position = position
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.font = font
        self.text_color = text_color
        self.text = 'Score: '

        self.score_text = Text((self.width / 2, self.position[1] + height / 2), self.text, self.font, self.text_color, self.width)
        self.background_rect = pygame.Rect(position[0], position[1], width, height)

    def update_render(self):
        self.score_text.set_text(self.text + str(self.score_obj.get_points()))
        self.score_text.update_render()

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.background_rect)
        self.score_text.draw(screen)

    def render_n_draw(self, screen):
        self.update_render()
        self.draw(screen)
