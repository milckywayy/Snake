import datetime

from utils.data_bank import Paths


def read_highscore():
    with open(str(Paths.HIGHSCORE_DIRECTORY.value), 'r') as f:
        return f.read().split('\n')


def write_highscore(points, date):
    with open(str(Paths.HIGHSCORE_DIRECTORY.value), 'w') as f:
        f.write(str(points) + '\n' + date)


def reset_highscore():
    with open(str(Paths.HIGHSCORE_DIRECTORY.value), 'w') as f:
        f.write("0\n" + datetime.datetime.now().strftime("%d-%m-%Y"))
