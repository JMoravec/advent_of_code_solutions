"""Tests for day 6 of 2023"""

import pytest
from year_2023.python.day6.day6 import (
    get_amount_of_solutions,
    solve_part_1,
    solve_part_2,
)


TEST_INPUT = """Time:      7  15   30
Distance:  9  40  200"""

# distance = x (time - x)
# want ->
# distance < x (time - x)
# 0 < x (time - x) - distance
# 0 < -x^2 + x*time - distance
# for 0 = bla:
# x = (-time +- sqrt(time^2 - 4*distance))/-2
# eg.:
# -7 + sqrt(49 + 36)


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
