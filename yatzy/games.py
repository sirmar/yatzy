# pylint: disable=too-few-public-methods
from typing import Protocol
from dataclasses import dataclass, field


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


class Game(Protocol):
    bonus_threshold: int
    bonus_amount: int
    nb_of_dice: int
    rules: list[Rule]


@dataclass
class Yatzy:
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
class MaxiYatzy:
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
