from typing import Protocol

from yatzy.hand import Hand


class Gui(Protocol):
    def display_hand(self, hand: Hand) -> None:
        ...

    def display_score_board(self) -> None:
        ...

    def choose_combination(self) -> int:
        ...

    def choose_rerolls(self) -> str:
        ...
