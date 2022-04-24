import unittest

from yatzy.board import Board
from yatzy.games import Yatzy
from yatzy.hand import Hand


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.game = Yatzy()
        self.board = Board(self.game)
        self.hand = Hand(self.game.nb_of_dice)

    def test_score_is_zero_at_start_of_game(self):
        self.when_calculating_total_score()
        self.then_score_is(0)

        self.when_calculating_upper_section_score()
        self.then_score_is(0)

        self.when_calculating_bonus()
        self.then_score_is(0)

    def test_lower_sections_scores_do_not_effect_upper_section(self):
        self.given_rule_with_dice(7, "12366")  # Pair 12
        self.given_rule_with_dice(11, "12345")  # Small Straight 15
        self.when_calculating_total_score()
        self.then_score_is(27)

        self.when_calculating_upper_section_score()
        self.then_score_is(0)

    def test_bonus_is_zero_until_above_threshold(self):
        self.given_rule_with_dice(1, "11222")
        self.given_rule_with_dice(2, "22211")
        self.given_rule_with_dice(3, "33311")
        self.given_rule_with_dice(4, "44411")
        self.given_rule_with_dice(5, "55511")
        self.given_rule_with_dice(6, "66611")

        self.when_calculating_upper_section_score()
        self.then_score_is(62)

        self.when_calculating_bonus()
        self.then_score_is(0)

        self.given_rule_with_dice(1, "11122")
        self.when_calculating_upper_section_score()
        self.then_score_is(63)

        self.when_calculating_bonus()
        self.then_score_is(50)

    def test_rounds(self):
        self.assertEqual(self.board.rounds(), 15)

    def test_used(self):
        self.assertFalse(self.board.used(1))
        self.given_rule_with_dice(1, "11222")
        self.assertTrue(self.board.used(1))

    def given_rule_with_dice(self, rule_index, dice):
        self.hand.set_dice(dice)
        self.board.set_score(rule_index, self.hand)

    def when_calculating_total_score(self):
        self.score = self.board.total_score()

    def when_calculating_bonus(self):
        self.score = self.board.bonus()

    def when_calculating_upper_section_score(self):
        self.score = self.board.upper_section_score()

    def then_score_is(self, expected):
        self.assertEqual(self.score, expected)
