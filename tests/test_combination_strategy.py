import unittest

from yatzy.combination_strategy import (
    UserInputCombinationStrategy,
    TopDownCombinationStrategy,
    create_combination_strategy,
)
from yatzy.gui import Gui
from yatzy.board import Board


class TestUserInputCombinationStrategy(unittest.TestCase):
    def setUp(self):
        self.gui = unittest.mock.Mock(Gui)
        self.board = unittest.mock.Mock(Board)
        self.strategy = UserInputCombinationStrategy(self.board, self.gui)

    def test_user_input_combination_strategy(self):
        self.given_user_input([1])
        self.given_combination_is_avaialable([False])
        self.when_choosing_combination()
        self.then_combination_is(1)

    def test_user_cannot_choose_used_combination(self):
        self.given_user_input([1, 2])
        self.given_combination_is_avaialable([True, False])
        self.when_choosing_combination()
        self.then_combination_is(2)
        self.then_combination_used_error_is_shown()

    def given_user_input(self, combinations):
        self.gui.choose_combination.side_effect = combinations

    def given_combination_is_avaialable(self, is_used_list):
        self.board.used.side_effect = is_used_list

    def when_choosing_combination(self):
        self.combination = self.strategy.choose_combination()

    def then_combination_is(self, expected):
        self.assertEqual(expected, self.combination)

    def then_combination_used_error_is_shown(self):
        self.gui.display_combination_used_error.assert_called_once()


class TestTopDownCombinationStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = TopDownCombinationStrategy()

    def test_combinations_is_chosen_in_sequence(self):
        self.assertEqual(1, self.strategy.choose_combination())
        self.assertEqual(2, self.strategy.choose_combination())
        self.assertEqual(3, self.strategy.choose_combination())


class TestCombinationStrategyInstantation(unittest.TestCase):
    def setUp(self):
        self.gui = unittest.mock.Mock(Gui)
        self.board = unittest.mock.Mock(Board)

    def test_return_correct_strategy_instance(self):
        self.assert_return_cls("standard", UserInputCombinationStrategy)
        self.assert_return_cls("topdown", TopDownCombinationStrategy)
        self.assert_raises_value_error("non existing")

    def assert_return_cls(self, variant, cls):
        obj = create_combination_strategy(variant, self.board, self.gui)
        self.assertIsInstance(obj, cls)

    def assert_raises_value_error(self, variant):
        with self.assertRaises(ValueError):
            create_combination_strategy(variant, self.board, self.gui)
