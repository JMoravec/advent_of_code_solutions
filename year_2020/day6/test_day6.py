"""
Test module for day 6 2020
"""
import pytest
from year_2020.day6.day6 import count_all_group, count_group, solve_part_1, solve_part_2


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
    "input_str,expected",
    [("abc\n", 3), ("a\nb\nc\n", 0), ("ab\nac\n", 1), ("a\na\na\na\n", 1), ("b\n", 1)],
)
def test_count_all_group(input_str: str, expected: int):
    """
    Validate that a single group is counted correctly
    """
    assert count_all_group(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected", [("abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb", 11)]
)
def test_solve_part_1(input_str: str, expected: int):
    """
    Validate that the exmple is correctly solved for part 1
    """
    assert solve_part_1(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected", [("abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb", 6)]
)
def test_solve_part_2(input_str: str, expected: int):
    """
    Validate that the exmple is correctly solved for part 2
    """
    assert solve_part_2(input_str) == expected
