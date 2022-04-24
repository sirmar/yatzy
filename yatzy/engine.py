from abc import ABC

from yatzy.gui import Gui
from yatzy.hand import Hand
from yatzy.board import Board


class Engine(ABC):
    def __init__(self, gui: Gui, hand: Hand, board: Board) -> None:
        self.hand = hand
        self.board = board
        self.gui = gui

    def play(self) -> None:
        for turn_nb in range(self.board.rounds()):
            self.gui.display_score_board(self.board)
            self.turn(turn_nb + 1)

    def turn(self, turn_nb: int) -> None:
        self.hand.roll_all()
        self.gui.display_hand(self.hand)

        for _ in range(2):
            reroll_again = self.choose_rerolls()
            if not reroll_again:
                break
            self.gui.display_hand(self.hand)

        self.update_combination(turn_nb)

    def choose_rerolls(self) -> bool:
        rerolls = self.gui.choose_rerolls()
        if rerolls == 0:
            return False
        self.hand.roll(str(rerolls))
        return True

    def update_combination(self, turn_nb) -> None:
        raise NotImplementedError


class Choose(Engine):
    def update_combination(self, _: int) -> None:
        while True:
            combination = self.gui.choose_combination()
            if not self.board.used(combination):
                self.board.set_score(combination, self.hand)
                return
            self.gui.display_combination_used_error()


class TopDown(Engine):
    def update_combination(self, turn_nb: int) -> None:
        self.board.set_score(turn_nb, self.hand)
