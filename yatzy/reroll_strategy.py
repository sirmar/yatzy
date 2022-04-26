# pylint: disable=too-few-public-methods
from typing import Protocol

from yatzy.gui import Gui


class RerollStrategy(Protocol):
    def choose_dice(self) -> int:
        ...


class UserInputRerollStrategy:
    def __init__(self, gui: Gui):
        self.gui = gui

    def choose_dice(self) -> int:
        return self.gui.choose_rerolls()
