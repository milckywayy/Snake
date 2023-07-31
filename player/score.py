import datetime

from utils.highscore_reader import write_highscore, read_highscore, reset_highscore


class Score:
    def __init__(self):
        self.points = 0
        self.previous_score = 0

    def get_score(self):
        return self.points

    def get_highscore(self):
        return read_highscore()

    def get_previous_score(self):
        return self.previous_score

    def set_highscore(self):
        if self.points > self.get_highscore():
            write_highscore(self.points, datetime.datetime.now().strftime("%d-%m-%Y"))

    def add_point(self):
        self.points += 1

    def reset(self):
        self.previous_score = self.points
        self.points = 0

    def highscore_reset(self):
        reset_highscore()
