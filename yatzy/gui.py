from typing import Protocol


class Gui(Protocol):
    def display_hand(self) -> None:
        ...

    def display_score_board(self) -> None:
        ...

    def display_no_such_combination_error(self) -> None:
        ...

    def display_combination_used_error(self) -> None:
        ...

    def choose_combination(self) -> int:
        ...

    def choose_rerolls(self) -> int:
        ...
