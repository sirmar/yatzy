# pylint: disable=too-few-public-methods
from dataclasses import dataclass, field
from abc import ABC

from yatzy.rules import (
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


class Game(ABC):
    bonus_threshold: int
    bonus_amount: int
    nb_of_dice: int
    rules: list[Rule]

    def bonus(self, score: int) -> int:
        if score < self.bonus_threshold:
            return 0
        return self.bonus_amount


@dataclass
class Yatzy(Game):
    bonus_threshold: int = 63
    bonus_amount: int = 50
    nb_of_dice: int = 5
    rules: list[Rule] = field(
        default_factory=lambda: [
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
    )


@dataclass
class MaxiYatzy(Game):
    bonus_threshold: int = 84
    bonus_amount: int = 100
    nb_of_dice: int = 6
    rules: list[Rule] = field(
        default_factory=lambda: [
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
    )
