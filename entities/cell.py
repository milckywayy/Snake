import pygame


class Cell:
    def __init__(self, pos, color, cell_size, outline_size):
        self.pos = pos
        self.color = color

        self.cell_size = cell_size
        self.outline_size = outline_size

    def get_position(self):
        return self.pos

    def set_position(self, pos):
        self.pos = pos

    def set_color(self, color):
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (
            (self.cell_size * self.pos[0] + self.outline_size * (self.pos[0] + 1)),
            (self.cell_size * self.pos[1] + self.outline_size * (self.pos[1] + 1)),
            self.cell_size, self.cell_size))

    def __eq__(self, obj):
        if not isinstance(obj, Cell):
            return False
        if self.get_position() != obj.get_position():
            return False

        return True

    def __ne__(self, obj):
        return not self.__eq__(obj)
