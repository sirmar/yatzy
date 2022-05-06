from yatzy.hand import Hand
from yatzy.board import Board
from yatzy.utils import clear_screen, input_int


# pylint: disable=no-self-use
class CLI:
    def __init__(self, board: Board, hand: Hand) -> None:
        self.board = board
        self.hand = hand

    def print_section(self, rows) -> None:
        for i, row in rows:
            score = row.score if row.used else ""
            print(f"{i:>2} | {row.rule.name:<20} | {score}")

    def display_hand(self) -> None:
        hand_str = "".join([str(die) for die in self.hand.dice])
        print(f"Nuvarande hand: {hand_str}")

    def display_score_board(self) -> None:
        clear_screen()
        print(35 * "-")
        self.print_section(self.board.upper())
        print(35 * "-")
        print(f"Summa: {self.board.upper_section_score()}")
        print(35 * "-")
        print(f"Bonus: {self.board.bonus()}")
        print(35 * "-")
        self.print_section(self.board.lower())
        print(35 * "-")
        print(f"Summa: {self.board.total_score()}")
        print(35 * "-")

    def display_combination_used_error(self) -> None:
        print("Upptagen. Välj en annan.")

    def display_no_such_combination_error(self) -> None:
        print("Finns ingen sådan kombination. Välj en annan.")

    def choose_combination(self) -> int:
        return input_int("Välj kombination: ")

    def choose_rerolls(self) -> int:
        return input_int("Slå om: ")
