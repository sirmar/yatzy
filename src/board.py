from typing import Tuple, List, Optional

from .hand import Hand
from .rules import Rule


class Board:
    score: List[Tuple[int, Rule, Optional[int]]]

    def __init__(self, rules: List[Rule]) -> None:
        self.score = [(i, rule, None) for i, rule in enumerate(rules)]

    def set_score(self, rule_index: int, hand: Hand):
        i, rule, _ = self.score[rule_index]
        self.score[rule_index] = (i, rule, rule.points(hand))

    def __str__(self) -> str:
        return "\n".join(
            [f"{i+1}. {rule.name}: {score}" for i, rule, score in self.score]
        )
