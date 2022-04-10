from yatzy.games import Game
from yatzy.cli import CLI
from yatzy.rules import (
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


def yatzy():
    rules = [
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
    ]
    game = Game(CLI(), rules, 5)
    game.play()


def maxi_yatzy():
    rules = [
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
    ]
    game = Game(CLI(), rules, 6)
    game.play()


if __name__ == "__main__":
    yatzy()
