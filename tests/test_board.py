import unittest

from src.board import Board
from src.rules import Ones, Twos, Pair


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board([Ones(), Twos(), Pair()])

    def test_bonus_is_zero_at_start_of_game(self):
        pass
