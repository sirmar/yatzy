from yatzy.games import create_game
from yatzy.engine import Engine
from yatzy.combination_strategy import create_combination_strategy
from yatzy.reroll_strategy import UserInputRerollStrategy
from yatzy.cli import CLI
from yatzy.hand import Hand
from yatzy.board import Board
from yatzy.cli_parser import parse_arguments


def main():
    result = parse_arguments()
    game = create_game(result.game)
    hand = Hand(game.nb_of_dice)
    board = Board(game)
    gui = CLI(board, hand)
    reroll_strategy = UserInputRerollStrategy(gui)
    combination_strategy = create_combination_strategy(
        result.variant, board, gui
    )
    engine = Engine(
        gui,
        hand,
        board,
        reroll_strategy,
        combination_strategy,
    )
    engine.play()
