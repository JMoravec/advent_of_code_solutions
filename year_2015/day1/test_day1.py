""" Tests for day 1"""
import pytest
from year_2015.day1.day1 import get_end_floor, get_first_basement_char


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_final_floor(input_str: str, expected: int):
    """Test the logic for getting the final floor number"""
    assert get_end_floor(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [(")", 1), ("()())", 5)])
def test_basement_pos(input_str: str, expected: int):
    """Test finding the first basement char"""
    assert get_first_basement_char(input_str) == expected
