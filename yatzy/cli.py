from typing import Optional

from yatzy.hand import Hand
from yatzy.board import Board


# pylint: disable=no-self-use
class CLI:
    def display_hand(self, hand: Hand) -> None:
        hand_str = "".join([str(die) for die in hand.dice])
        print(f"Nuvarande hand: {hand_str}")

    def display_score_board(self, board: Board) -> None:
        print(40 * "-")
        for i, row in board.score.items():
            if row.rule.upper:
                print(
                    f"{i+1:>2} | {row.rule.name:<20} | {row.score if row.used else ''}"
                )
        print(40 * "-")
        print(f"Summa: {board.upper_section_score()}")
        print(40 * "-")
        print(f"Bonus: {board.bonus()}")
        print(40 * "-")
        for i, row in board.score.items():
            if not row.rule.upper:
                print(
                    f"{i+1:>2} | {row.rule.name:<20} | {row.score if row.used else ''}"
                )
        print(40 * "-")
        print(f"Summa: {board.total_score()}")
        print(40 * "-")

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
