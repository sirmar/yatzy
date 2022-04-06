# pylint: disable=too-few-public-methods
from typing import Protocol, List
from collections import Counter

from .hand import Hand


class Rule(Protocol):
    name: str

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

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 1)


class Twos:
    name: str = "Tvåor"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 2)


class Threes:
    name: str = "Treor"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 3)


class Fours:
    name: str = "Fyror"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 4)


class Fives:
    name: str = "Femmor"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 5)


class Sixes:
    name: str = "Sexor"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_for_die_value(hand, 6)


class Pair:
    name: str = "Ett par"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2])


class TwoPair:
    name: str = "Två par"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 2])


class ThreeEqual:
    name: str = "Tretal"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [3])


class FourEqual:
    name: str = "Fyrtal"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [4])


class SmallStraight:
    name: str = "Liten straight"

    @staticmethod
    def points(hand: Hand) -> int:
        return straight_between(hand, 1, 5)


class LargeStraight:
    name: str = "Stor straight"

    @staticmethod
    def points(hand: Hand) -> int:
        return straight_between(hand, 2, 6)


class FullHouse:
    name: str = "Kåk"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_sets(hand, [2, 3])


class Chance:
    name: str = "Chans"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum(hand.dice)


class Yatzy:
    name: str = "Yatzy"

    @staticmethod
    def points(hand: Hand) -> int:
        if sum_sets(hand, [hand.nb_of_dice]) > 0:
            return 50
        return 0
