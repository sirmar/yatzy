import os
from typing import Optional

from yatzy.hand import Hand
from yatzy.board import Board


# pylint: disable=no-self-use
class CLI:
    def print_section(self, rows) -> None:
        for i, row in rows:
            score = row.score if row.used else ""
            print(f"{i+1:>2} | {row.rule.name:<20} | {score}")

    def display_hand(self, hand: Hand) -> None:
        hand_str = "".join([str(die) for die in hand.dice])
        print(f"Nuvarande hand: {hand_str}")

    def display_score_board(self, board: Board) -> None:
        os.system("clear")
        print(35 * "-")
        self.print_section(board.upper())
        print(35 * "-")
        print(f"Summa: {board.upper_section_score()}")
        print(35 * "-")
        print(f"Bonus: {board.bonus()}")
        print(35 * "-")
        self.print_section(board.lower())
        print(35 * "-")
        print(f"Summa: {board.total_score()}")
        print(35 * "-")

    def choose_combination(self, board: Board) -> int:
        while True:
            try:
                combination = int(input("Välj kombination: ")) - 1
                if board.used(combination):
                    print("Upptagen. Välj en annan.")
                else:
                    return combination
            except ValueError:
                print("Fel: Endast siffror tillåtna. Försök igen.")

    def choose_rerolls(self) -> Optional[str]:
        while True:
            try:
                answer = input("Slå om: ")
                if len(answer) == 0:
                    return None
                int(answer)
                return answer
            except ValueError:
                print("Fel: Endast siffror tillåtna. Försök igen.")
