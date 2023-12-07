"""Solution for day 7 of 2023"""

import collections
from dataclasses import dataclass
from enum import Enum
from functools import cache, cached_property, cmp_to_key
from typing import Dict, List


class HandType(Enum):
    """Enum for each type of hand"""

    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


@cache
def get_card_value(char: str, joker_wild: bool = False):
    """Get the card value for a given card"""
    if char == "A":
        return 14
    if char == "K":
        return 13
    if char == "Q":
        return 12
    if char == "J":
        if joker_wild:
            return 1
        return 11
    if char == "T":
        return 10
    return int(char)


@dataclass
class Hand:
    """Class representing a hand of cards"""

    hand: str
    bid: int
    joker_wild: bool

    @cached_property
    def hand_type(self) -> HandType:
        """Get the hand type of a hand"""
        cards: Dict[str, int] = collections.defaultdict(int)
        for card in self.hand:
            cards[card] += 1

        jokers = cards["J"]
        if not self.joker_wild or jokers == 0:
            values = list(cards.values())
            values.sort(reverse=True)
            if 5 in values:
                return HandType.FIVE_OF_A_KIND
            if 4 in values:
                return HandType.FOUR_OF_A_KIND
            if values[0] == 3:
                if values[1] == 2:
                    return HandType.FULL_HOUSE
                return HandType.THREE_OF_A_KIND
            if values[0] == 2:
                if values[1] == 2:
                    return HandType.TWO_PAIR
                return HandType.ONE_PAIR
            return HandType.HIGH_CARD

        if jokers in [4, 5]:
            return HandType.FIVE_OF_A_KIND

        values = []
        for key, value in cards.items():
            if key != "J":
                values.append(value)
        values.sort(reverse=True)
        values[0] += jokers
        if 5 in values:
            return HandType.FIVE_OF_A_KIND
        if 4 in values:
            return HandType.FOUR_OF_A_KIND
        if values[0] == 3:
            if values[1] == 2:
                return HandType.FULL_HOUSE
            return HandType.THREE_OF_A_KIND
        if values[0] == 2:
            if values[1] == 2:
                return HandType.TWO_PAIR
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    @staticmethod
    def from_string(input_str: str, joker_wild: bool = False) -> "Hand":
        """Create a hand object from a string"""
        hand, bid = input_str.strip().split()
        return Hand(hand, int(bid), joker_wild)

    @staticmethod
    def compare_hand_type(hand_1: "Hand", hand_2: "Hand") -> int:
        """Compare hand types (for sorting)"""
        if hand_1.hand_type.value < hand_2.hand_type.value:
            return -1
        if hand_1.hand_type.value > hand_2.hand_type.value:
            return 1
        return 0

    @staticmethod
    def compare_high_card(hand_1: "Hand", hand_2: "Hand") -> int:
        """Compare high cards (for sorting)"""
        for i, hand_1_char in enumerate(hand_1.hand):
            hand_1_value = get_card_value(hand_1_char, hand_1.joker_wild)
            hand_2_value = get_card_value(hand_2.hand[i], hand_2.joker_wild)

            if hand_1_value < hand_2_value:
                return -1
            if hand_1_value > hand_2_value:
                return 1
        return 0


def sort_cards(hands: List[Hand]):
    """Sort a list of hands"""
    hands.sort(key=cmp_to_key(Hand.compare_high_card))
    hands.sort(key=cmp_to_key(Hand.compare_hand_type))


def solve_answer(hands: List[Hand]) -> int:
    """Solve the answer for a given list of hands"""
    sort_cards(hands)
    answer = 0
    for i, hand in enumerate(hands):
        answer += (i + 1) * hand.bid
    return answer


if __name__ == "__main__":
    with open("year_2023/inputs/day7_input.txt", encoding="utf-8") as file:
        input_file = file.read()
    hands_no_jokers = [Hand.from_string(x) for x in input_file.splitlines()]
    print(f"Day 7 part 1: {solve_answer(hands_no_jokers)}")
    hands_joker_wild = [Hand.from_string(x, True) for x in input_file.splitlines()]
    print(f"Day 7 part 2: {solve_answer(hands_joker_wild)}")
