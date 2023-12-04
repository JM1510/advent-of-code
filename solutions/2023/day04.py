import re

from dataclasses import dataclass


@dataclass
class ScratchingCard:
    """Class for keeping track of scratching cards"""
    number: int
    score: int

    @classmethod
    def from_line(cls, line: str):
        card_data = re.match(
            r'[\w]+[\s]+(?P<number>[\d]+):(?P<winning_numbers>[\s+\d+]+)\|(?P<playing_numbers>[\s+\d+]+)',  # noqa
            line
        )

        winning_numbers = set(card_data.group('winning_numbers').split())
        playing_numbers = set(card_data.group('playing_numbers').split())

        score = len(winning_numbers & playing_numbers)

        return ScratchingCard(
            number=int(card_data.group('number')),
            score=score
        )


def part_one(lines):
    answer = 0

    for line in lines:
        scratching_card = ScratchingCard.from_line(line)

        matching_number_count = scratching_card.score

        if matching_number_count:
            answer += 2**(matching_number_count - 1)

    return answer


def part_two(lines):
    scratching_cards = {}

    for line in lines:
        scratching_card = ScratchingCard.from_line(line)
        scratching_cards[scratching_card.number] = scratching_card

    all_cards = list(scratching_cards.values())

    i = 0
    while i < len(all_cards):
        card = all_cards[i]

        card_copies = []
        if card.score:
            for j in range(card.number + 1, card.number+card.score+1):
                card_copies.append(scratching_cards[j])
        all_cards.extend(card_copies)
        i += 1

    return len(all_cards)
