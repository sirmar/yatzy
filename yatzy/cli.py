from yatzy.hand import Hand


# pylint: disable=no-self-use
class CLI:
    def display_hand(self, hand: Hand) -> None:
        print(f"{hand}")

    def display_score_board(self) -> None:
        ...

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