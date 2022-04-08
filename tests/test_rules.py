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


class TestRules(TestCase):
    def test_ones(self):
        self.given_rule(Ones())
        self.give_points("11123", 3)
        self.give_zero_points("23456")
        self.has_name("Ettor")

    def test_twos(self):
        self.given_rule(Twos())
        self.give_points("11223", 4)
        self.give_zero_points("13456")
        self.has_name("Tvåor")

    def test_threes(self):
        self.given_rule(Threes())
        self.give_points("33336", 12)
        self.give_zero_points("12456")
        self.has_name("Treor")

    def test_fours(self):
        self.given_rule(Fours())
        self.give_points("33446", 8)
        self.give_zero_points("12356")
        self.has_name("Fyror")

    def test_fives(self):
        self.given_rule(Fives())
        self.give_points("44556", 10)
        self.give_zero_points("12346")
        self.has_name("Femmor")

    def test_sixes(self):
        self.given_rule(Sixes())
        self.give_points("33446", 6)
        self.give_zero_points("12345")
        self.has_name("Sexor")

    def test_pair(self):
        self.given_rule(Pair())
        self.give_points("12366", 12)
        self.give_points("33446", 8)
        self.give_zero_points("12345")
        self.has_name("Ett par")

    def test_two_pair(self):
        self.given_rule(TwoPair())
        self.give_points("13366", 18)
        self.give_points("11666", 14)
        self.give_points("114466", 20)
        self.give_zero_points("11112")
        self.give_zero_points("11234")
        self.has_name("Två par")

    def test_three_pair(self):
        self.given_rule(ThreePair())
        self.give_points("113366", 20)
        self.give_zero_points("114456")
        self.has_name("Tre par")

    def test_tree_equal(self):
        self.given_rule(ThreeEqual())
        self.give_points("111666", 18)
        self.give_points("33444", 12)
        self.give_points("55555", 15)
        self.give_zero_points("11445")
        self.has_name("Tretal")

    def test_four_equal(self):
        self.given_rule(FourEqual())
        self.give_points("34444", 16)
        self.give_points("11116666", 24)
        self.give_points("55555", 20)
        self.give_zero_points("11444")
        self.has_name("Fyrtal")

    def test_five_equal(self):
        self.given_rule(FiveEqual())
        self.give_points("344444", 20)
        self.give_points("55555", 25)
        self.give_zero_points("114444")
        self.has_name("Femtal")

    def test_small_straigt(self):
        self.given_rule(SmallStraight())
        self.give_points("12345", 15)
        self.give_points("1123445", 15)
        self.give_zero_points("23456")
        self.give_zero_points("11111")
        self.has_name("Liten straight")

    def test_large_straigt(self):
        self.given_rule(LargeStraight())
        self.give_points("23456", 20)
        self.give_points("2334456", 20)
        self.give_zero_points("12345")
        self.give_zero_points("66666")
        self.has_name("Stor straight")

    def test_full_straigt(self):
        self.given_rule(FullStraight())
        self.give_points("123456", 21)
        self.give_zero_points("112345")
        self.has_name("Full straight")

    def test_cabin(self):
        self.given_rule(Cabin())
        self.give_points("33366", 21)
        self.give_points("11666", 20)
        self.give_points("155666", 28)
        self.give_points("11116666", 20)
        self.give_zero_points("11223")
        self.give_zero_points("33333")
        self.has_name("Kåk")

    def test_house(self):
        self.given_rule(House())
        self.give_points("333666", 27)
        self.give_zero_points("133555")
        self.give_zero_points("226666")
        self.has_name("Hus")

    def test_tower(self):
        self.given_rule(Tower())
        self.give_points("336666", 30)
        self.give_zero_points("335556")
        self.give_zero_points("222666")
        self.has_name("Torn")

    def test_chance(self):
        self.given_rule(Chance())
        self.give_points("11111", 5)
        self.give_points("34456", 22)
        self.has_name("Chans")

    def test_yatzy(self):
        self.given_rule(Yatzy(100))
        self.give_points("444444", 100)
        self.has_name("Yatzy")

        self.given_rule(Yatzy(50))
        self.give_points("1111", 50)
        self.give_points("55555", 50)
        self.give_zero_points("133333")

    def given_rule(self, rule):
        self.rule = rule

    def give_points(self, dice, expected):
        hand = MagicMock(Hand)
        hand.dice = [int(die) for die in dice]
        hand.nb_of_dice = len(dice)
        points = self.rule.points(hand)
        self.assertEqual(points, expected)

    def give_zero_points(self, dice):
        self.give_points(dice, 0)

    def has_name(self, expected):
        self.assertEqual(self.rule.name, expected)
