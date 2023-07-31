from utils.data_bank import Paths


def read_highscore():
    with open(str(Paths.HIGHSCORE_DIRECTORY), 'r') as f:
        return f.read().split('\n')


def write_highscore(points, date):
    with open(str(Paths.HIGHSCORE_DIRECTORY), 'r') as f:
        f.write(points + '\n' + date)
