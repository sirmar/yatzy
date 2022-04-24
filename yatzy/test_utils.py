import unittest

from yatzy.utils import input_int, roll_die, clear_screen


class TestBoard(unittest.TestCase):
    def test_input_int_converts_answer_to_int_and_retries_on_errors(self):
        mock = unittest.mock.Mock(side_effect=["not an int", "1234"])
        result = input_int("text", mock)
        mock.assert_called_with("text")
        self.assertEqual(1234, result)

    def test_roll_die(self):
        self.assertTrue(1 <= roll_die() <= 6)

    # pylint: disable=no-self-use
    def test_clear_screen(self):
        mock = unittest.mock.Mock()
        clear_screen(mock)
        mock.assert_called_with("clear")
