from typing import List

from yatzy.gui import Gui
from yatzy.hand import Hand
from yatzy.board import Board
from yatzy.rules import Rule


class Game:
    def __init__(self, gui: Gui, rules: List[Rule], nb_of_dice: int) -> None:
        self.hand = Hand(nb_of_dice)
        self.rules = rules
        self.board = Board(rules)
        self.gui = gui

    def play(self) -> None:
        print(self.board)
        for _ in range(len(self.rules)):
            self.turn()
            print(self.board)

    def turn(self) -> None:
        self.hand.roll_all()
        self.gui.display_hand(self.hand)

        for _ in range(2):
            dice_to_reroll = self.gui.choose_rerolls()
            if len(dice_to_reroll) == 0:
                break
            self.hand.roll(dice_to_reroll)
            self.gui.display_hand(self.hand)

        rule_index = self.gui.choose_combination()
        self.board.set_score(rule_index, self.hand)


# Uppifrån och ner
# 10000
