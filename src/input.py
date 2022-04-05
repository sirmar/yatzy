def choose_combination() -> int:
    while True:
        try:
            return int(input("Välj kombination: ")) - 1
        except ValueError as error:
            print(error)


def choose_rerolls() -> str:
    while True:
        try:
            return input("Omslag: ")
        except ValueError as error:
            print(error)
