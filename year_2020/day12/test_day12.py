"""
Test module for day 12 2020
"""
from typing import List
import pytest
from year_2020.day12.day12 import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "input_str,expected", [(["F10", "N3", "F7", "R90", "F11"], 25)]
)
def test_solve_part_1(input_str: List[str], expected: int):
    assert solve_part_1(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected", [(["F10", "N3", "F7", "R90", "F11"], 286)]
)
def test_solve_part_2(input_str: List[str], expected: int):
    assert solve_part_2(input_str) == expected
