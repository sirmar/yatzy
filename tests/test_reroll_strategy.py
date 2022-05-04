import unittest

from yatzy.reroll_strategy import UserInputRerollStrategy
from yatzy.gui import Gui


class TestUserInputRerollStrategy(unittest.TestCase):
    def setUp(self):
        self.gui = unittest.mock.Mock(Gui)
        self.strategy = UserInputRerollStrategy(self.gui)

    def test_user_input_reroll_strategy(self):
        self.strategy.choose_dice()
        self.gui.choose_rerolls.assert_called_once()
