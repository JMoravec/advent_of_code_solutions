"""
Test module for day 6 2020
"""
import pytest
from day6.day6 import solve_part_1, count_group


@pytest.mark.parametrize(
    "input_str,expected",
    [("abc\n", 3), ("a\nb\nc\n", 3), ("ab\nac\n", 3), ("a\na\na\na\n", 1), ("b\n", 1)],
)
def test_count_group(input_str: str, expected: int):
    """
    Validate that a single group is counted correctly
    """
    assert count_group(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected", [("abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb", 11)]
)
def test_solve_part_1(input_str: str, expected: int):
    """
    Validate that the exmple is correctly solved for part 1
    """
    assert solve_part_1(input_str) == expected
