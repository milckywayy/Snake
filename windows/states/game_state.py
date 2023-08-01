import math

import pygame

from windows.states.window_state import WindowState
from utils.config import get_color
from windows.interface.button import Button
from windows.interface.text import Text
from windows.interface.score_bar import ScoreBar

from entities.snake import Snake
from entities.apple import Apple
from entities.cell import Cell


class GameState(WindowState):
    def __init__(self, window):
        self.active_color = get_color(window.get_config(), 'input-active-color')
        self.inactive_color = get_color(window.get_config(), 'input-inactive-color')
        self.bg_color = get_color(window.get_config(), 'background-color')

        self.background_rect = pygame.Rect(0, 0, window.resolution[0], window.resolution[1] - int(window.get_config()['score-bar-height']))

        self.snake = Snake((12, 12), 3, 0,
                           get_color(window.get_config(), 'snake-body-color'),
                           get_color(window.get_config(), 'snake-head-color'),
                           int(window.get_config()['cell-size']), int(window.get_config()['outline']))

        self.apple = Apple(int(window.get_config()['cell-size']), int(window.get_config()['outline']),
                           get_color(window.get_config(), 'food-color'), window.get_cell_number())

        self.score_bar = ScoreBar(window.score, (0, window.get_cell_number() * int(window.get_config()['cell-size']) + (window.get_cell_number() + 1) * int(window.get_config()['outline'])),
                                  window.resolution[0], int(window.get_config()['score-bar-height']), self.inactive_color, window.font_medium, self.bg_color)

        self.SNAKE_MOVE = pygame.USEREVENT + 1
        self.snake_move = pygame.event.Event(self.SNAKE_MOVE)
        pygame.time.set_timer(self.snake_move, self.speed_fun(window.score.get_score()))

        self.direction = [0]

    def speed_fun(self, x):
        if x < 100:
            return round((-1/250) * math.pow(x, 2) + 100)
        else:
            return 60

    def handle_event(self, window, event):
        if event.type == pygame.QUIT:
            window.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                window.set_state(window.states['pause'])
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                if self.direction[-1] != 0 and self.direction[-1] != 2 and len(self.direction) < 3:
                    self.direction.append(0)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if self.direction[-1] != 1 and self.direction[-1] != 3 and len(self.direction) < 3:
                    self.direction.append(1)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if self.direction[-1] != 2 and self.direction[-1] != 0 and len(self.direction) < 3:
                    self.direction.append(2)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if self.direction[-1] != 3 and self.direction[-1] != 1 and len(self.direction) < 3:
                    self.direction.append(3)
        elif event.type == self.SNAKE_MOVE:
            self.snake.move(self.direction[0])
            if self.snake.get_head().get_position()[0] >= window.get_cell_number():
                self.snake.get_head().set_position([0, self.snake.get_head().get_position()[1]])
            elif self.snake.get_head().get_position()[0] < 0:
                self.snake.get_head().set_position(
                    [window.get_cell_number() - 1, self.snake.get_head().get_position()[1]])
            elif self.snake.get_head().get_position()[1] >= window.get_cell_number():
                self.snake.get_head().set_position([self.snake.get_head().get_position()[0], 0])
            elif self.snake.get_head().get_position()[1] < 0:
                self.snake.get_head().set_position(
                    [self.snake.get_head().get_position()[0], window.get_cell_number() - 1])

            if len(self.direction) > 1:
                self.direction.pop(0)
            if self.snake.get_head().get_position() == self.apple.get_position():
                window.sfx.play_sound('eat')
                window.score.add_point()
                self.apple.eaten()
                while self.apple in self.snake.get_whole_body():
                    self.apple.eaten()
                self.snake.grow()
                pygame.time.set_timer(self.snake_move, self.speed_fun(window.score.get_score()))
                self.draw_static_background(window)
            elif self.snake.get_head() in self.snake.get_body():
                self.reset(window)
                window.set_state(window.states['lost'])

    def draw(self, window):
        pygame.draw.rect(window.screen, get_color(window.config, 'background-color'), self.background_rect)
        self.snake.draw(window.screen)
        self.apple.draw(window.screen)

    def draw_static_background(self, window):
        self.score_bar.render_n_draw(window.screen)

    def reset(self, window):
        window.sfx.stop_music()
        self.snake.die()
        self.apple.eaten()
        self.direction = [0]
        window.score.reset()
        pygame.time.set_timer(self.snake_move, self.speed_fun(0))

        self.draw_static_background(window)

    def play_sound(self, window):
        if window.sfx.is_music_playing():
            window.sfx.play_music('game_music')
        else:
            window.sfx.play_music('game_music')

    def pause_sound(self, window):
        window.sfx.pause_music()
