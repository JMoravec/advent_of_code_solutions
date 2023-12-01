"""
Test module for day 8 2020
"""
from typing import List
import pytest
from year_2020.day9.day9 import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "preamble_length,inputs,expected",
    [
        (
            5,
            [
                35,
                20,
                15,
                25,
                47,
                40,
                62,
                55,
                65,
                95,
                102,
                117,
                150,
                182,
                127,
                219,
                299,
                277,
                309,
                576,
            ],
            127,
        )
    ],
)
def test_solve_part_1(preamble_length: int, inputs: List[int], expected: int):
    assert solve_part_1(preamble_length, inputs) == expected


@pytest.mark.parametrize(
    "preamble_length,inputs,expected",
    [
        (
            5,
            [
                35,
                20,
                15,
                25,
                47,
                40,
                62,
                55,
                65,
                95,
                102,
                117,
                150,
                182,
                127,
                219,
                299,
                277,
                309,
                576,
            ],
            62,
        )
    ],
)
def test_solve_part_2(preamble_length: int, inputs: List[int], expected: int):
    assert solve_part_2(127, inputs) == expected
