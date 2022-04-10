from typing import List
from yatzy.utils import roll_die


class Hand:
    dice: List[int]

    def __init__(self, nb_of_dice: int, rand_fn=roll_die) -> None:
        self.rand_fn = rand_fn
        self.nb_of_dice = nb_of_dice
        self.roll_all()

    def set_dice(self, dice: str) -> None:
        self.dice = sorted([int(c) for c in dice])

    def roll_all(self) -> None:
        self.dice = sorted([self.rand_fn() for i in range(self.nb_of_dice)])

    def roll(self, dice_to_reroll: str) -> None:
        new_dice = []
        for die in self.dice:
            if str(die) in dice_to_reroll:
                new_dice.append(self.rand_fn())
                dice_to_reroll = dice_to_reroll.replace(str(die), "", 1)
            else:
                new_dice.append(die)
        self.dice = sorted(new_dice)

    def __str__(self) -> str:
        return "".join([str(die) for die in self.dice])
