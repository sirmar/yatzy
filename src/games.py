from typing import List

from .hand import Hand
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
    ThreeEqual,
    FourEqual,
    SmallStraight,
    LargeStraight,
    FullHouse,
    Chance,
    Yatzy as YatzyRule,
)
from .board import Board
from .input import choose_combination, choose_rerolls


class Game:
    hand: Hand
    rules: List[Rule]

    def __init__(self, rules: List[Rule], nb_of_dice: int) -> None:
        self.hand = Hand(nb_of_dice)
        self.rules = rules
        self.board = Board(rules)

    def play(self) -> None:
        print(self.board)
        for _ in range(len(self.rules)):
            self.turn()
            print(self.board)
        print("Slut!")

    def turn(self) -> None:
        self.hand.roll_all()
        print(f"{self.hand}")

        for _ in range(2):
            dice_to_reroll = choose_rerolls()
            if len(dice_to_reroll) == 0:
                break
            self.hand.roll(dice_to_reroll)
            print(f"{self.hand}")

        rule_index = choose_combination()
        self.board.set_score(rule_index, self.hand)


class Yatzy(Game):
    def __init__(self) -> None:
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
            FullHouse(),
            Chance(),
            YatzyRule(),
        ]
        super().__init__(rules, 5)


# Maxi Yatzy
# Uppifrån och ner
# 10000
