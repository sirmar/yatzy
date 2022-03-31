from unittest import TestCase
from unittest.mock import Mock

from src.die import Die


class TestDie(TestCase):
    def setUp(self):
        self.random_fn = Mock()
        self.die = Die(self.random_fn)

    def test_throwing_should_set_die_value(self):
        self.given_next_die_roll_is(1)
        self.when_die_is_thrown()
        self.then_value_is(1)

    def test_value_should_be_result_of_latest_throw(self):
        self.given_next_die_roll_is(1)
        self.when_die_is_thrown()
        self.given_next_die_roll_is(6)
        self.when_die_is_thrown()
        self.then_value_is(6)

    def given_next_die_roll_is(self, value):
        self.random_fn.return_value = value

    def when_die_is_thrown(self):
        self.die.throw()

    def then_value_is(self, expected):
        self.assertEqual(self.die.value(), expected)
