from typing import Tuple, List

from yatzy.hand import Hand
from yatzy.rules import Rule


class Board:
    score: List[Tuple[Rule, int, bool]]

    def __init__(self, rules: List[Rule]) -> None:
        self.score = [(rule, 0, False) for rule in rules]

    def set_score(self, rule_index: int, hand: Hand):
        rule = self.score[rule_index][0]
        self.score[rule_index] = (rule, rule.points(hand), True)

    def bonus(self):
        points = sum([points for rule, points, _ in self.score if rule.bonus])
        if points > 63:
            return 50
        return 0

    def __str__(self) -> str:
        return "\n".join(
            [
                f"{i+1:>2}. {rule.name}: {score}"
                for i, (rule, score, _) in enumerate(self.score)
            ]
        )
