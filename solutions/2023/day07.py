import re

from dataclasses import dataclass
from typing import List


CARD_VALUES = values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}


@dataclass
class Hand:
    cards: str
    score: int
    bid: int
    card_values: str
    jokers: int
    matches: List[str]

    @classmethod
    def from_line(cls, line: str, use_joker: bool = False):
        matcher = re.compile(r'(\w)\1*')

        cards, bid = line.split()
        sorted_cards = ''.join(sorted(cards))
        matches = sorted(
            [match.group() for match in matcher.finditer(sorted_cards)],
            key=len,
            reverse=True
        )
        jokers = sorted_cards.count('J')

        if use_joker:
            # Pop out match with jokers
            matches = [
                match for match in matches
                if "J" not in match or "JJJJJ" in match
            ]
            # Add jokers to first match
            if matches[0] != 'JJJJJ':
                matches[0] += "J" * jokers

        card_values = []

        for card in cards:
            value = CARD_VALUES.get(card)
            card_values.append(
                value if value else int(card)
            )

        return Hand(
            bid=int(bid),
            score=len(matches[0]) / len(matches),
            card_values=card_values,
            cards=cards,
            matches=matches,
            jokers=jokers
        )


def part_one(lines, *args):
    answer = 0
    hands = []
    for line in lines:
        hands.append(Hand.from_line(line))

    sorted_hands = sorted(
        hands,
        key=lambda x: (x.score, x.card_values)
    )

    for i, hand in enumerate(sorted_hands, 1):
        answer += hand.bid * i

    return answer


def part_two(lines, *args):
    answer = 0
    CARD_VALUES["J"] = 1
    hands = []
    for line in lines:
        hands.append(Hand.from_line(line, use_joker=True))

    sorted_hands = sorted(
        hands,
        key=lambda x: (x.score, x.card_values)
    )

    for i, hand in enumerate(sorted_hands, 1):
        answer += hand.bid * i

    return answer
