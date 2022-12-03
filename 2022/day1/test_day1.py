"""
Test module for day1
"""
from typing import List
import pytest
from day1.day1 import (
    get_calories_for_elf,
    get_largest_calorie,
    get_three_largest_cals_for_elves,
)


@pytest.fixture(name="test_elves")
def test_elves_fixture() -> List[List[int]]:
    """
    Fixture to get the test elves
    """
    return [
        [
            1000,
            2000,
            3000,
        ],
        [4000],
        [5000, 6000],
        [
            7000,
            8000,
            9000,
        ],
        [10000],
    ]


@pytest.mark.parametrize(
    "test_elf,expected",
    [
        ([1000, 2000, 3000], 6000),
        ([4000], 4000),
        ([5000, 6000], 11000),
        ([7000, 8000, 9000], 24000),
        ([10000], 10000),
    ],
)
def test_get_calories_for_elf(test_elf: List[int], expected: int):
    """
    Validates that the calculated calories for an elf are correct
    """
    assert get_calories_for_elf(test_elf) == expected


def test_get_largest_calorie(test_elves: List[List[int]]):
    """
    Validates that getting the largest calorie amount for a list of elves
    is correct
    """
    expected = 24000
    assert get_largest_calorie(test_elves) == expected


def test_get_three_largest_cals(test_elves: List[List[int]]):
    """
    Validates that getting the sum of the 3 largest calorie amounts for a list
    of elves is correct
    """
    expected = 45000
    assert get_three_largest_cals_for_elves(test_elves) == expected
