"""Tests for day 7 of 2023"""

import pytest
from year_2023.python.day7.day7 import (
    Hand,
    HandType,
    solve_answer,
    sort_cards,
)

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


@pytest.mark.parametrize(
    "hand,expected",
    [
        (Hand("AAAAA", 0, False), HandType.FIVE_OF_A_KIND),
        (Hand("AA8AA", 0, False), HandType.FOUR_OF_A_KIND),
        (Hand("23332", 0, False), HandType.FULL_HOUSE),
        (Hand("TTT98", 0, False), HandType.THREE_OF_A_KIND),
        (Hand("23432", 0, False), HandType.TWO_PAIR),
        (Hand("A23A4", 0, False), HandType.ONE_PAIR),
        (Hand("23456", 0, False), HandType.HIGH_CARD),
        (Hand("32T3K", 0, False), HandType.ONE_PAIR),
        (Hand("32T3K", 0, True), HandType.ONE_PAIR),
        (Hand("KK677", 0, False), HandType.TWO_PAIR),
        (Hand("KK677", 0, True), HandType.TWO_PAIR),
        (Hand("KTJJT", 0, False), HandType.TWO_PAIR),
        (Hand("KTJJT", 0, True), HandType.FOUR_OF_A_KIND),
        (Hand("T55J5", 0, False), HandType.THREE_OF_A_KIND),
        (Hand("T55J5", 0, True), HandType.FOUR_OF_A_KIND),
        (Hand("QQQJA", 0, False), HandType.THREE_OF_A_KIND),
        (Hand("QQQJA", 0, True), HandType.FOUR_OF_A_KIND),
        (Hand("QQJAA", 0, True), HandType.FULL_HOUSE),
        (Hand("QQJA9", 0, True), HandType.THREE_OF_A_KIND),
        (Hand("QQJJJ", 0, True), HandType.FIVE_OF_A_KIND),
        (Hand("QJJJJ", 0, True), HandType.FIVE_OF_A_KIND),
        (Hand("1234J", 0, True), HandType.ONE_PAIR),
        (Hand("123JJ", 0, True), HandType.THREE_OF_A_KIND),
    ],
)
def test_hand_type(hand: Hand, expected: HandType):
    assert hand.hand_type == expected


def test_sort_no_jokers():
    hands = [Hand.from_string(x) for x in TEST_INPUT.splitlines()]
    sort_cards(hands)
    assert hands[0].hand == "32T3K"
    assert hands[1].hand == "KTJJT"
    assert hands[2].hand == "KK677"
    assert hands[3].hand == "T55J5"
    assert hands[4].hand == "QQQJA"


def test_sort_jokers_wild():
    hands = [Hand.from_string(x, True) for x in TEST_INPUT.splitlines()]
    sort_cards(hands)
    assert hands[0].hand == "32T3K"
    assert hands[1].hand == "KK677"
    assert hands[2].hand == "T55J5"
    assert hands[3].hand == "QQQJA"
    assert hands[4].hand == "KTJJT"


def test_part_1():
    hands = [Hand.from_string(x) for x in TEST_INPUT.splitlines()]
    assert solve_answer(hands) == 6440


def test_part_2():
    hands = [Hand.from_string(x, True) for x in TEST_INPUT.splitlines()]
    assert solve_answer(hands) == 5905
