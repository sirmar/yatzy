from dataclasses import dataclass
from yatzy.hand import Hand
from yatzy.games import Game
from yatzy.rules import Rule


@dataclass
class Row:
    rule: Rule
    score: int
    used: bool

    # pylint: disable=assignment-from-no-return
    def set_score(self, hand: Hand) -> None:
        self.score = self.rule.points(hand)
        self.used = True


class Board:
    score: dict[int, Row]

    def __init__(self, game: Game) -> None:
        self.game = game
        self.score = {
            i: Row(rule, 0, False) for i, rule in enumerate(game.rules)
        }

    def set_score(self, rule_index: int, hand: Hand) -> None:
        row = self.score[rule_index]
        row.set_score(hand)

    def used(self, rule_index: int) -> bool:
        return self.score[rule_index].used

    def upper(self):
        return [(i, row) for i, row in self.score.items() if row.rule.upper]

    def lower(self):
        return [
            (i, row) for i, row in self.score.items() if not row.rule.upper
        ]

    def bonus(self) -> int:
        if self.upper_section_score() < self.game.bonus_threshold:
            return 0
        return self.game.bonus_amount

    def upper_section_score(self) -> int:
        return sum(
            [row.score for row in self.score.values() if row.rule.upper]
        )

    def total_score(self) -> int:
        return sum([row.score for row in self.score.values()]) + self.bonus()

    def rounds(self) -> int:
        return len(self.score)
