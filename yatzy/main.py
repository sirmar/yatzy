from yatzy.games import Yatzy, MaxiYatzy
from yatzy.engine import Engine
from yatzy.cli import CLI
from yatzy.hand import Hand
from yatzy.board import Board


def yatzy():
    engine = Engine(CLI(), Hand(5), Board(Yatzy()))
    engine.play()


def maxi_yatzy():
    engine = Engine(CLI(), Hand(5), Board(MaxiYatzy()))
    engine.play()


if __name__ == "__main__":
    yatzy()
