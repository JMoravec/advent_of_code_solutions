"""Tests for day 8"""

from year_2023.python.day8.day8 import (
    follow_instructions,
    follow_instructions_ghost,
    read_lines,
)


TEST_INPUT_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def test_steps_taken():
    """Validate part 1 instructions"""
    assert follow_instructions(*read_lines(TEST_INPUT_1)) == 2
    assert follow_instructions(*read_lines(TEST_INPUT_2)) == 6


def test_steps_taken_ghost():
    """Validate part 2 instructions"""
    assert follow_instructions_ghost(*read_lines(TEST_INPUT_3)) == 6
