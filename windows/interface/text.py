class Text:
    def __init__(self, position, text, font, color):
        self.position = position
        self.text = text
        self.font = font
        self.color = color

        self.text_rendered = self.render()

    def set_text(self, text):
        self.text = text

    def render(self):
        return self.font.render(self.text, True, self.color)

    def update_render(self):
        self.text_rendered = self.render()

    def draw(self, screen):
        screen.blit(self.text_rendered, (self.position[0] - self.text_rendered.get_width() / 2,
                                         self.position[1] - self.text_rendered.get_height() / 2))

    def render_n_draw(self, screen):
        self.update_render()
        self.draw(screen)
