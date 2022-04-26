# pylint: disable=too-few-public-methods
from typing import Protocol

from yatzy.gui import Gui
from yatzy.board import Board


class CombinationStrategy(Protocol):
    def choose_combination(self) -> int:
        ...


class UserInputCombinationStrategy:
    def __init__(self, board: Board, gui: Gui) -> None:
        self.board = board
        self.gui = gui

    def choose_combination(self) -> int:
        while True:
            combination = self.gui.choose_combination()
            if not self.board.used(combination):
                return combination
            self.gui.display_combination_used_error()


class TopDownCombinationStrategy:
    def __init__(self) -> None:
        self.current_round = 0

    def choose_combination(self) -> int:
        self.current_round += 1
        return self.current_round


def create_combination_strategy(
    variant: str, board: Board, gui: Gui
) -> CombinationStrategy:
    if variant == "topdown":
        return TopDownCombinationStrategy()
    return UserInputCombinationStrategy(board, gui)
