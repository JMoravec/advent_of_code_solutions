"""Tests for day 1"""
import pytest

from year_2023.python.day1.day1 import get_num_from_line


@pytest.mark.parametrize(
    "input_line,expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_get_num_from_line(input_line: str, expected: int):
    assert get_num_from_line(input_line) == expected
