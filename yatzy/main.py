from yatzy.games import Yatzy, MaxiYatzy
from yatzy.cli import CLI


def yatzy():
    game = Yatzy(CLI())
    game.play()


def maxi_yatzy():
    game = MaxiYatzy(CLI())
    game.play()


if __name__ == "__main__":
    yatzy()
