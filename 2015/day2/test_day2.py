"""Tests for day 2"""
from typing import Tuple
import pytest

from day2.day2 import calculate_ribbon_needed, calculate_wrapping_paper


@pytest.mark.parametrize(
    "input_box,expected",
    [((2, 3, 4), 58), ((1, 1, 10), 43)],
)
def test_final_floor(input_box: Tuple[int, int, int], expected: int):
    """Test the logic for getting the amount of wrapping paper needed"""
    assert calculate_wrapping_paper(input_box) == expected


@pytest.mark.parametrize(
    "input_box,expected",
    [((2, 3, 4), 34), ((1, 1, 10), 14)],
)
def test_calculate_ribbon_needed(input_box: Tuple[int, int, int], expected):
    """Test the logic for getting the ribbon needed"""
    assert calculate_ribbon_needed(input_box) == expected
