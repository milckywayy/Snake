from entities.cell import Cell


class Snake:
    def __init__(self, position, length, direction, body_color, head_color, cell_size, outline_size):
        self.position_default = position
        self.length_default = length
        self.direction_default = direction

        self.body_color = body_color
        self.head_color = head_color

        self.cell_size = cell_size
        self.outline_size = outline_size

        self.direction = self.direction_default

        self.body = [Cell(self.position_default, self.body_color, cell_size, outline_size) for _ in range(self.length_default)]
        self.body[0].set_color(self.head_color)

    def get_head(self):
        return self.body[0]

    def get_whole_body(self):
        return self.body

    def get_body(self):
        return self.body[1:]

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def move(self, direction):
        self.set_direction(direction)

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].set_position(self.body[i - 1].get_position())

        head_pos = self.body[0].get_position()
        if self.direction == 0:
            self.body[0].set_position([head_pos[0], head_pos[1] - 1])
        elif self.direction == 1:
            self.body[0].set_position([head_pos[0] + 1, head_pos[1]])
        elif self.direction == 2:
            self.body[0].set_position([head_pos[0], head_pos[1] + 1])
        elif self.direction == 3:
            self.body[0].set_position([head_pos[0] - 1, head_pos[1]])

    def grow(self):
        self.body.append(Cell(self.body[-1].get_position(), self.body_color, self.cell_size, self.outline_size))

    def die(self):
        self.direction = self.direction_default

        self.body = [Cell(self.position_default, self.body_color, self.cell_size, self.outline_size) for _ in range(self.length_default)]
        self.body[0].set_color(self.head_color)

    def draw(self, screen):
        self.body[0].draw(screen)
        for cell in self.body[1:]:
            cell.draw(screen)
