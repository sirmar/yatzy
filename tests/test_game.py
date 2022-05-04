import unittest

from yatzy.games import create_game


class TestGames(unittest.TestCase):
    def test_yatzy(self):
        yatzy = create_game("yatzy")
        self.assertEqual(yatzy.nb_of_dice, 5)
        self.assertEqual(yatzy.bonus(62), 0)
        self.assertEqual(yatzy.bonus(63), 50)

    def test_maxi_yatzy(self):
        yatzy = create_game("maxiyatzy")
        self.assertEqual(yatzy.nb_of_dice, 6)
        self.assertEqual(yatzy.bonus(83), 0)
        self.assertEqual(yatzy.bonus(84), 100)

    def test_non_existing_game(self):
        with self.assertRaises(ValueError):
            create_game("non existing game")
