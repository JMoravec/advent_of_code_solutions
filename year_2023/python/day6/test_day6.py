"""Tests for day 6 of 2023"""

import pytest
from year_2023.python.day6.day6 import (
    get_amount_of_solutions,
    solve_part_1,
    solve_part_2,
)


TEST_INPUT = """Time:      7  15   30
Distance:  9  40  200"""


@pytest.mark.parametrize(
    "time,distance,expected", [(7, 9, 4), (15, 40, 8), (30, 200, 9)]
)
def test_amount_of_solutions(time: int, distance: int, expected: int):
    """Test that the test inputs produce the correct output"""
    assert get_amount_of_solutions(time, distance) == expected


def test_part_1():
    """Validate the solution works for the test input"""
    assert solve_part_1(TEST_INPUT) == 288


def test_part_2():
    """Validate the solution works for the test input"""
    assert solve_part_2(TEST_INPUT) == 71503
