from yatzy.gui import Gui
from yatzy.hand import Hand
from yatzy.board import Board


class Engine:
    def __init__(self, gui: Gui, hand: Hand, board: Board) -> None:
        self.hand = hand
        self.board = board
        self.gui = gui

    def play(self) -> None:
        for _ in range(self.board.rounds()):
            self.gui.display_score_board(self.board)
            self.turn()

    def turn(self) -> None:
        self.hand.roll_all()
        self.gui.display_hand(self.hand)

        for _ in range(2):
            reroll_again = self.choose_rerolls()
            if not reroll_again:
                break
            self.gui.display_hand(self.hand)

        self.choose_combination()

    def choose_rerolls(self) -> bool:
        rerolls = self.gui.choose_rerolls()
        if rerolls == 0:
            return False
        self.hand.roll(str(rerolls))
        return True

    def choose_combination(self) -> None:
        while True:
            combination = self.gui.choose_combination()
            if not self.board.used(combination):
                self.board.set_score(combination, self.hand)
                return
            self.gui.display_combination_used_error()
