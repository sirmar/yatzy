from string import ascii_lowercase
from typing import Dict, List

from .die import Die


class Hand:
    dice: Dict[str, Die]

    def __init__(self, dice: List[Die]) -> None:
        self.dice = {}
        for i, die in enumerate(dice):
            self.dice[ascii_lowercase[i]] = die

    def throw_all(self) -> None:
        for die in self.dice.values():
            die.throw()

    def throw(self, name_string: str) -> None:
        for character in name_string:
            if character in self.dice:
                self.dice[character].throw()

    def __str__(self) -> str:
        return ", ".join([f"{name}:{die}" for name, die in self.dice.items()])
