"""Tests for day 1"""
import pytest

from year_2023.python.day1.day1 import (
    get_num_from_line,
    get_total_from_lines,
)


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
    """Test geting a single number from a single line"""
    assert get_num_from_line(input_line) == expected


@pytest.mark.parametrize(
    "input_line,use_replace_text,expected",
    [
        ("1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet", False, 142),
        (
            "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n"
            "4nineeightseven2\nzoneight234\n7pqrstsixteen",
            True,
            281,
        ),
    ],
)
def test_get_total_from_lines(input_line: str, use_replace_text: bool, expected: int):
    """Test getting the total value from multiple lines"""
    assert get_total_from_lines(input_line, use_replace_text) == expected
