from typing import Optional

from yatzy.hand import Hand
from yatzy.games import Game
from yatzy.rules import Rule


class Board:
    score: list[tuple[Rule, Optional[int]]]

    def __init__(self, game: Game) -> None:
        self.game = game
        all_rules = game.upper_section + game.lower_section
        self.score = [(rule, None) for rule in all_rules]

    def set_score(self, rule_index: int, hand: Hand):
        rule = self.score[rule_index][0]
        self.score[rule_index] = (rule, rule.points(hand))

    def rounds(self):
        return len(self.score)

    def __str__(self) -> str:
        return "\n".join(
            [
                f"{i+1:>2}. {rule.name} {score if score is not None else ''}"
                for i, (rule, score) in enumerate(self.score)
            ]
        )
