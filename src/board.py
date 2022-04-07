from typing import Tuple, List, Optional

from .hand import Hand
from .rules import Rule


class Board:
    score: List[Tuple[Rule, Optional[int]]]

    def __init__(self, rules: List[Rule]) -> None:
        self.score = [(rule, None) for rule in rules]

    def set_score(self, rule_index: int, hand: Hand):
        rule, _ = self.score[rule_index]
        self.score[rule_index] = (rule, rule.points(hand))

    def __str__(self) -> str:
        return "\n".join(
            [
                f"{i+1:>2}. {rule.name}: {score}"
                for i, (rule, score) in enumerate(self.score)
            ]
        )
