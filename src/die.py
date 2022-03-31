from typing import Callable


class Die:
    def __init__(self, random_fn: Callable[[int, int], int]) -> None:
        self._random_fn = random_fn
        self._value = 1

    def throw(self) -> None:
        self._value = self._random_fn(1, 6)

    def value(self) -> int:
        return self._value

    def __str__(self) -> str:
        return f"{self.value()}"
