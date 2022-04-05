# pylint: disable=too-few-public-methods
from typing import Protocol
from collections import Counter

from .hand import Hand


class Rule(Protocol):
    name: str

    def points(self, hand: Hand) -> int:
        ...


def sum_for_die_value(hand: Hand, value: int) -> int:
    return sum(filter(lambda x: x == value, hand.dice))


def sum_equals(hand: Hand, length: int) -> int:
    counter = Counter(hand.dice)
    pairs = filter(lambda x: x[1] >= length, counter.items())
    return max(dict(pairs).keys(), default=0) * length


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
        return sum_equals(hand, 2)


class ThreeEqual:
    name: str = "Tretal"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_equals(hand, 3)


class FourEqual:
    name: str = "Fyrtal"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum_equals(hand, 4)


class Yatzy:
    name: str = "Yatzy"

    @staticmethod
    def points(hand: Hand) -> int:
        if sum_equals(hand, hand.nb_of_dice) > 0:
            return 50
        return 0


class Chance:
    name: str = "Chans"

    @staticmethod
    def points(hand: Hand) -> int:
        return sum(hand.dice)
