from yatzy.games import Game, Yatzy, MaxiYatzy
from yatzy.engine import Engine
from yatzy.cli import CLI
from yatzy.hand import Hand
from yatzy.board import Board


def play(game: Game) -> None:
    engine = Engine(CLI(), Hand(game.nb_of_dice), Board(game))
    engine.play()


def yatzy():
    play(Yatzy())


def maxi_yatzy():
    play(MaxiYatzy())
