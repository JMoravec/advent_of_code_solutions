"""Tests for day 9"""


import pytest
from year_2023.python.day9.day9 import Nums, calculate_totals


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("0 3 6 9 12 15", 18),
        ("1 3 6 10 15 21", 28),
        ("10 13 16 21 30 45", 68),
    ],
)
def test_get_next_num(input_str: str, expected: int):
    """Validate getting the next number in a sequence"""
    nums = Nums([int(num) for num in input_str.split()])
    assert nums.get_next_num(0) == expected


def test_part_1():
    """Validate part 1"""
    input_lines = [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45",
    ]
    assert calculate_totals(input_lines) == 114


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("0 3 6 9 12 15", -3),
        ("1 3 6 10 15 21", 0),
        ("10 13 16 21 30 45", 5),
    ],
)
def test_use_left(input_str: str, expected: int):
    """Validate getting the next number in a sequence from the left"""
    nums = Nums([int(num) for num in input_str.split()])
    assert nums.get_next_num(0, True) == expected


def test_part_2():
    """Validate part 2"""
    input_lines = [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45",
    ]
    assert calculate_totals(input_lines, True) == 2
