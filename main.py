from utils.config import create_config
from utils.setup import create_game_directory
from windows.game_window import GameWindow


if __name__ == '__main__':
    create_game_directory()
    create_config()

    game = GameWindow()
    game.run()
