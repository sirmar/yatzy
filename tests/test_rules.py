from unittest import TestCase
from unittest.mock import MagicMock

from src.hand import Hand
from src.rules import (
    Ones,
    Twos,
    Threes,
    Fours,
    Fives,
    Sixes,
    Pair,
    ThreeEqual,
    FourEqual,
    SmallStraight,
    LargeStraight,
    Chance,
    Yatzy,
)


class TestRules(TestCase):
    def test_ones(self):
        self.give_points(Ones, "11123", 3)
        self.give_zero_points(Ones, "23456")
        self.has_name(Ones, "Ettor")

    def test_twos(self):
        self.give_points(Twos, "11223", 4)
        self.give_zero_points(Twos, "13456")
        self.has_name(Twos, "Tvåor")

    def test_threes(self):
        self.give_points(Threes, "33336", 12)
        self.give_zero_points(Threes, "12456")
        self.has_name(Threes, "Treor")

    def test_fours(self):
        self.give_points(Fours, "33446", 8)
        self.give_zero_points(Fours, "12356")
        self.has_name(Fours, "Fyror")

    def test_fives(self):
        self.give_points(Fives, "44556", 10)
        self.give_zero_points(Fives, "12346")
        self.has_name(Fives, "Femmor")

    def test_sixes(self):
        self.give_points(Sixes, "33446", 6)
        self.give_zero_points(Sixes, "12345")
        self.has_name(Sixes, "Sexor")

    def test_pair(self):
        self.give_points(Pair, "12366", 12)
        self.give_points(Pair, "33446", 8)
        self.give_zero_points(Pair, "12345")
        self.has_name(Pair, "Ett par")

    def test_tree_equal(self):
        self.give_points(ThreeEqual, "111666", 18)
        self.give_points(ThreeEqual, "33444", 12)
        self.give_points(ThreeEqual, "55555", 15)
        self.give_zero_points(ThreeEqual, "11445")
        self.has_name(ThreeEqual, "Tretal")

    def test_four_equal(self):
        self.give_points(FourEqual, "34444", 16)
        self.give_points(FourEqual, "11116666", 24)
        self.give_points(FourEqual, "55555", 20)
        self.give_zero_points(FourEqual, "11444")
        self.has_name(FourEqual, "Fyrtal")

    def test_small_straigt(self):
        self.give_points(SmallStraight, "12345", 15)
        self.give_points(SmallStraight, "1123445", 15)
        self.give_zero_points(SmallStraight, "23456")
        self.give_zero_points(SmallStraight, "11111")
        self.has_name(SmallStraight, "Liten straight")

    def test_large_straigt(self):
        self.give_points(LargeStraight, "23456", 20)
        self.give_points(LargeStraight, "2334456", 20)
        self.give_zero_points(LargeStraight, "12345")
        self.give_zero_points(LargeStraight, "66666")
        self.has_name(LargeStraight, "Stor straight")

    def test_chance(self):
        self.give_points(Chance, "11111", 5)
        self.give_points(Chance, "34456", 22)
        self.has_name(Chance, "Chans")

    def test_yatzy(self):
        self.give_points(Yatzy, "4444444", 50)
        self.give_points(Yatzy, "1111", 50)
        self.give_points(Yatzy, "55555", 50)
        self.give_zero_points(Yatzy, "133333")
        self.has_name(Yatzy, "Yatzy")

    def give_points(self, rule, dice, expected):
        hand = MagicMock(Hand)
        hand.dice = [int(die) for die in dice]
        hand.nb_of_dice = len(dice)
        points = rule().points(hand)
        self.assertEqual(points, expected)

    def give_zero_points(self, rule, dice):
        self.give_points(rule, dice, 0)

    def has_name(self, rule, expected):
        self.assertEqual(rule().name, expected)
