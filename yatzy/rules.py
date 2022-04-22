# pylint: disable=too-few-public-methods
from typing import Protocol
from collections import Counter

from yatzy.hand import Hand


class Rule(Protocol):
    name: str
    upper: bool

    def points(self, hand: Hand) -> int:
        ...


def sum_for_die_value(hand: Hand, value: int) -> int:
    return sum(filter(lambda x: x == value, hand.dice))


def sum_sets(hand: Hand, lengths: list[int]) -> int:
    freq = Counter(hand.dice)

    result = 0
    for length in sorted(lengths, reverse=True):
        value = max([v for v, f in freq.items() if f >= length], default=0)
        if value == 0:
            return 0
        result += value * length
        del freq[value]
    return result


def straight_between(hand: Hand, start: int, end: int) -> int:
    straight = range(start, end + 1)
    for value in straight:
        if value not in hand.dice:
            return 0
    return sum(straight)


class UpperRule:
    upper: bool = True


class LowerRule:
    upper: bool = False


class Ones(UpperRule):
    name: str = "Ettor"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 1)


class Twos(UpperRule):
    name: str = "Tvåor"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 2)


class Threes(UpperRule):
    name: str = "Treor"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 3)


class Fours(UpperRule):
    name: str = "Fyror"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 4)


class Fives(UpperRule):
    name: str = "Femmor"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 5)


class Sixes(UpperRule):
    name: str = "Sexor"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 6)


class Pair(LowerRule):
    name: str = "Ett par"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2])


class TwoPair(LowerRule):
    name: str = "Två par"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 2])


class ThreePair(LowerRule):
    name: str = "Tre par"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 2, 2])


class ThreeEqual(LowerRule):
    name: str = "Tretal"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [3])


class FourEqual(LowerRule):
    name: str = "Fyrtal"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [4])


class FiveEqual(LowerRule):
    name: str = "Femtal"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [5])


class SmallStraight(LowerRule):
    name: str = "Liten straight"

    @staticmethod
    def points(hand: Hand) -> int:
        return straight_between(hand, 1, 5)


class LargeStraight(LowerRule):
    name: str = "Stor straight"

    @staticmethod
    def points(hand: Hand) -> int:
        return straight_between(hand, 2, 6)


class FullStraight(LowerRule):
    name: str = "Full straight"

    @staticmethod
    def points(hand: Hand) -> int:
        return straight_between(hand, 1, 6)


class Cabin(LowerRule):
    name: str = "Kåk"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 3])


class House(LowerRule):
    name: str = "Hus"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [3, 3])


class Tower(LowerRule):
    name: str = "Torn"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 4])


class Chance(LowerRule):
    name: str = "Chans"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum(hand.dice)


class Yatzy(LowerRule):
    name: str = "Yatzy"

    def __init__(self, points: int) -> None:
        self._points = points

    def points(self, hand: Hand) -> int:
        if sum_sets(hand, [hand.nb_of_dice]) > 0:
            return self._points
        return 0
