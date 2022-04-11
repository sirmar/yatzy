from typing import List

from yatzy.hand import Hand
from yatzy.rules import Rule


class Board:
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

    def rounds(self):
        return len(self.score)

    def __str__(self) -> str:
        return "\n".join(
            [
                f"{i+1:>2}. {rule.name}: {score if used else ''}"
                for i, (rule, score, used) in enumerate(self.score)
            ]
        )
