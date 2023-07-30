import random

from entities.cell import Cell


class Apple(Cell):
    def __init__(self, cell_size, outline_size, color, cell_number):
        self.cell_number = cell_number

        super().__init__(self.generate_new_position(), color, cell_size, outline_size)

    def generate_new_position(self):
        x = random.randrange(0, self.cell_number)
        y = random.randrange(0, self.cell_number)

        return [x, y]

    def eaten(self):
        super().set_position(self.generate_new_position())
