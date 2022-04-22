import unittest

from yatzy.hand import Hand


class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand(nb_of_dice=5, rand_fn=lambda: 1)

    def test_dice_are_sorted(self):
        self.given_rolls("54321")
        self.then_dice("12345")

    def test_rerolling_nothing_should_keep_all_dice(self):
        self.given_rolls("23456")
        self.when_rerolling_nothing()
        self.then_dice("23456")

    def test_rerolling_non_existing_values_should_keep_all_dice(self):
        self.given_rolls("12366")
        self.when_rerolling("45")
        self.then_dice("12366")

    def test_rerolling_existing_values_should_trigger_rolls(self):
        self.given_rolls("12366")
        self.when_rerolling("66")
        self.then_dice("11123")

    def given_rolls(self, dice):
        self.hand.set_dice(dice)

    def when_rerolling(self, dice_to_reroll):
        self.hand.roll(dice_to_reroll)

    def when_rerolling_nothing(self):
        self.when_rerolling("")

    def then_dice(self, expected):
        dice_str = "".join([str(die) for die in self.hand.dice])
        self.assertEqual(dice_str, expected)
