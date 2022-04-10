# pylint: disable=too-few-public-methods
from typing import Protocol, List
from collections import Counter

from yatzy.hand import Hand


class Rule(Protocol):
    name: str
    bonus: bool

    def points(self, hand: Hand) -> int:
        ...


def sum_for_die_value(hand: Hand, value: int) -> int:
    return sum(filter(lambda x: x == value, hand.dice))


def sum_sets(hand: Hand, lengths: List[int]) -> int:
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


class Ones:
    name: str = "Ettor"
    bonus: bool = True

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 1)


class Twos:
    name: str = "Tvåor"
    bonus: bool = True

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 2)


class Threes:
    name: str = "Treor"
    bonus: bool = True

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 3)


class Fours:
    name: str = "Fyror"
    bonus: bool = True

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 4)


class Fives:
    name: str = "Femmor"
    bonus: bool = True

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 5)


class Sixes:
    name: str = "Sexor"
    bonus: bool = True

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 6)


class Pair:
    name: str = "Ett par"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2])


class TwoPair:
    name: str = "Två par"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 2])


class ThreePair:
    name: str = "Tre par"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 2, 2])


class ThreeEqual:
    name: str = "Tretal"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [3])


class FourEqual:
    name: str = "Fyrtal"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [4])


class FiveEqual:
    name: str = "Femtal"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [5])


class SmallStraight:
    name: str = "Liten straight"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return straight_between(hand, 1, 5)


class LargeStraight:
    name: str = "Stor straight"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return straight_between(hand, 2, 6)


class FullStraight:
    name: str = "Full straight"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return straight_between(hand, 1, 6)


class Cabin:
    name: str = "Kåk"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 3])


class House:
    name: str = "Hus"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [3, 3])


class Tower:
    name: str = "Torn"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 4])


class Chance:
    name: str = "Chans"
    bonus: bool = False

    @staticmethod
    def points(hand: Hand) -> int:
        return sum(hand.dice)


class Yatzy:
    name: str = "Yatzy"
    bonus: bool = False

    def __init__(self, points: int) -> None:
        self._points = points

    def points(self, hand: Hand) -> int:
        if sum_sets(hand, [hand.nb_of_dice]) > 0:
            return self._points
        return 0
