from src.games import Yatzy
from src.cli import CLI


def main():
    game = Yatzy(CLI())
    game.play()


if __name__ == "__main__":
    main()
