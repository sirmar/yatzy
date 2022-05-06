from yatzy.gui import Gui
from yatzy.hand import Hand
from yatzy.board import Board
from yatzy.combination_strategy import CombinationStrategy
from yatzy.reroll_strategy import RerollStrategy


# pylint: disable=too-many-arguments
class Engine:
    def __init__(
        self,
        gui: Gui,
        hand: Hand,
        board: Board,
        reroll_strategy: RerollStrategy,
        combination_strategy: CombinationStrategy,
    ) -> None:
        self.hand = hand
        self.board = board
        self.gui = gui
        self.reroll_strategy = reroll_strategy
        self.combination_strategy = combination_strategy

    def play(self) -> None:
        self.gui.display_score_board()
        for _ in range(self.board.rounds()):
            self.turn()

    def turn(self) -> None:
        self.hand.roll_all()
        self.gui.display_hand()

        for _ in range(2):
            rerolls = self.reroll_strategy.choose_dice()
            if rerolls == 0:
                break
            self.hand.roll(str(rerolls))
            self.gui.display_hand()

        combination = self.combination_strategy.choose_combination()
        self.board.set_score(combination, self.hand)
        self.gui.display_score_board()
