from dataclasses import dataclass

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
    Yatzy,
)


@dataclass
class Game:
    bonus_threshold: int
    bonus_amount: int
    nb_of_dice: int
    rules: list[Rule]

    def bonus(self, score: int) -> int:
        if score < self.bonus_threshold:
            return 0
        return self.bonus_amount


def create_yatzy() -> Game:
    return Game(
        bonus_threshold=63,
        bonus_amount=50,
        nb_of_dice=5,
        rules=[
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
            Yatzy(50),
        ],
    )


def create_maxi_yatzy() -> Game:
    return Game(
        bonus_threshold=84,
        bonus_amount=100,
        nb_of_dice=6,
        rules=[
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
            Yatzy(100),
        ],
    )


def create_game(game: str) -> Game:
    if game == "maxiyatzy":
        return create_maxi_yatzy()
    return create_yatzy()
