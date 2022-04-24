import random
import os


def roll_die() -> int:
    return random.randint(1, 6)


def clear_screen(system_fn=os.system) -> None:
    system_fn("clear")


def input_int(text: str, input_fn=input) -> int:
    while True:
        try:
            return int(input_fn(text))
        except ValueError:
            pass
