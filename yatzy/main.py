from yatzy.games import Game, create_yatzy, create_maxi_yatzy
from yatzy.engine import Choose, TopDown
from yatzy.cli import CLI
from yatzy.hand import Hand
from yatzy.board import Board


def play(game: Game, mode) -> None:
    engine = mode(CLI(), Hand(game.nb_of_dice), Board(game))
    engine.play()


def yatzy():
    play(create_yatzy(), Choose)


def yatzy_top_down():
    play(create_yatzy(), TopDown)


def maxi_yatzy():
    play(create_maxi_yatzy(), Choose)


def maxi_yatzy_top_down():
    play(create_maxi_yatzy(), TopDown)
