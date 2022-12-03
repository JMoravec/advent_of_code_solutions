"""Tests for day 3"""

from typing import Tuple
import pytest
from day3.day3 import (
    get_rucksacks,
    get_common_letter,
    get_set_for_string,
    get_priority,
    get_common_badge,
)


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", ("vJrwpWtwJgWr", "hcsFMMfFFhFp")),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")),
        ("PmmdzqPrVvPwwTWBwg", ("PmmdzqPrV", "vPwwTWBwg")),
    ],
)
def test_get_rucksacks(input_str: str, expected: Tuple[str, str]):
    """Test the rucksack split"""
    assert get_rucksacks(input_str) == expected


@pytest.mark.parametrize(
    "ruck_1,ruck_2,expected",
    [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrV", "vPwwTWBwg", "P"),
    ],
)
def test_get_common_letter(ruck_1: str, ruck_2: str, expected: str):
    """Test getting the common letter"""
    assert (
        get_common_letter(get_set_for_string(ruck_1), get_set_for_string(ruck_2))
        == expected
    )


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrVvPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJQctTZtZT", "t"),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
    ],
)
def test_get_common_letter_from_str(input_str: str, expected: str):
    """Test getting the common letter from the full original string"""
    ruck_1, ruck_2 = get_rucksacks(input_str)
    assert (
        get_common_letter(get_set_for_string(ruck_1), get_set_for_string(ruck_2))
        == expected
    )


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", 16),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 38),
        ("PmmdzqPrVvPwwTWBwg", 42),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 22),
        ("ttgJtRGJQctTZtZT", 20),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", 19),
    ],
)
def test_get_priority_point_from_str(input_str: str, expected: int):
    """Test getting the priority value from the full original string"""
    ruck_1, ruck_2 = get_rucksacks(input_str)
    assert (
        get_priority(
            get_common_letter(get_set_for_string(ruck_1), get_set_for_string(ruck_2))
        )
        == expected
    )


@pytest.mark.parametrize(
    "ruck_1,ruck_2,ruck_3,expected",
    [
        (
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "r",
        ),
        (
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
            "Z",
        ),
    ],
)
def test_get_badge(ruck_1: str, ruck_2: str, ruck_3: str, expected: int):
    """Test getting the priority value from the full original string"""
    assert (
        get_common_badge(
            get_set_for_string(ruck_1),
            get_set_for_string(ruck_2),
            get_set_for_string(ruck_3),
        )
        == expected
    )
