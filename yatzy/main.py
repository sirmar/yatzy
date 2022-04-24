from yatzy.games import Game, Yatzy, MaxiYatzy
from yatzy.engine import Choose, TopDown
from yatzy.cli import CLI
from yatzy.hand import Hand
from yatzy.board import Board


def play(game: Game, mode) -> None:
    engine = mode(CLI(), Hand(game.nb_of_dice), Board(game))
    engine.play()


def yatzy():
    play(Yatzy(), Choose)


def yatzy_top_down():
    play(Yatzy(), TopDown)


def maxi_yatzy():
    play(MaxiYatzy(), Choose)


def maxi_yatzy_top_down():
    play(MaxiYatzy(), TopDown)
