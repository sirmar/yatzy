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
            dice_to_reroll = self.gui.choose_rerolls()
            if dice_to_reroll is None:
                break
            self.hand.roll(dice_to_reroll)
            self.gui.display_hand(self.hand)

        rule_index = self.gui.choose_combination(self.board)
        self.board.set_score(rule_index, self.hand)
