from typing import List

from .gui import Gui
from .hand import Hand
from .board import Board
from .rules import (
    Rule,
    Ones,
    Twos,
    Threes,
    Fours,
    Fives,
    Sixes,
    Pair,
    TwoPair,
    ThreePair,
    ThreeEqual,
    FourEqual,
    FiveEqual,
    SmallStraight,
    LargeStraight,
    FullStraight,
    Cabin,
    House,
    Tower,
    Chance,
    Yatzy as YatzyRule,
)


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


class Yatzy(Game):
    def __init__(self, gui: Gui) -> None:
        rules: List[Rule] = [
            Ones(),
            Twos(),
            Threes(),
            Fours(),
            Fives(),
            Sixes(),
            Pair(),
            TwoPair(),
            ThreeEqual(),
            FourEqual(),
            SmallStraight(),
            LargeStraight(),
            Cabin(),
            Chance(),
            YatzyRule(50),
        ]
        super().__init__(gui, rules, 5)


class MaxiYatzy(Game):
    def __init__(self, gui: Gui) -> None:
        rules: List[Rule] = [
            Ones(),
            Twos(),
            Threes(),
            Fours(),
            Fives(),
            Sixes(),
            Pair(),
            TwoPair(),
            ThreePair(),
            ThreeEqual(),
            FourEqual(),
            FiveEqual(),
            SmallStraight(),
            LargeStraight(),
            FullStraight(),
            Cabin(),
            House(),
            Tower(),
            Chance(),
            YatzyRule(100),
        ]
        super().__init__(gui, rules, 6)


# Uppifrån och ner
# 10000
