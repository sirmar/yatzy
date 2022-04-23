from typing import Protocol, Optional

from yatzy.hand import Hand
from yatzy.board import Board


class Gui(Protocol):
    def display_hand(self, hand: Hand) -> None:
        ...

    def display_score_board(self, board: Board) -> None:
        ...

    def choose_combination(self, board: Board) -> int:
        ...

    def choose_rerolls(self) -> Optional[str]:
        ...
