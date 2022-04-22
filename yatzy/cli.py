from yatzy.hand import Hand
from yatzy.board import Board


# pylint: disable=no-self-use
class CLI:
    def display_hand(self, hand: Hand) -> None:
        hand_str = "".join([str(die) for die in hand.dice])
        print(f"Current hand: {hand_str}")

    def display_score_board(self, board: Board) -> None:
        for i, row in board.score.items():
            print(f"{i+1:>2} {row.rule.name} {row.score if row.used else ''}")

    def choose_combination(self) -> int:
        while True:
            try:
                return int(input("Välj kombination: ")) - 1
            except ValueError as error:
                print(error)

    def choose_rerolls(self) -> str:
        while True:
            try:
                return input("Omslag: ")
            except ValueError as error:
                print(error)
