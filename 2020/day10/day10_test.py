"""
Test module for day 10 2020
"""
from typing import List
import pytest
from day10.day10 import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "input_values,expected",
    [
        (
            [
                16,
                10,
                15,
                5,
                1,
                11,
                7,
                19,
                6,
                12,
                4,
            ],
            35,
        ),
        (
            [
                28,
                33,
                18,
                42,
                31,
                14,
                46,
                20,
                48,
                47,
                24,
                23,
                49,
                45,
                19,
                38,
                39,
                11,
                1,
                32,
                25,
                35,
                8,
                17,
                7,
                9,
                4,
                2,
                34,
                10,
                3,
            ],
            220,
        ),
    ],
)
def test_solve_part_1(input_values: List[int], expected: int):
    """
    Validate part 1 of the day
    """
    assert solve_part_1(input_values) == expected


@pytest.mark.parametrize(
    "input_values,expected",
    [
        (
            [
                16,
                10,
                15,
                5,
                1,
                11,
                7,
                19,
                6,
                12,
                4,
            ],
            8,
        ),
        (
            [
                28,
                33,
                18,
                42,
                31,
                14,
                46,
                20,
                48,
                47,
                24,
                23,
                49,
                45,
                19,
                38,
                39,
                11,
                1,
                32,
                25,
                35,
                8,
                17,
                7,
                9,
                4,
                2,
                34,
                10,
                3,
            ],
            19208,
        ),
    ],
)
def test_solve_part_2(input_values: List[int], expected: int):
    """
    Validate part 1 of the day
    """
    assert solve_part_2(input_values) == expected
