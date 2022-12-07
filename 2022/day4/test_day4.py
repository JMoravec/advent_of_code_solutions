"""Tests for day 4"""
from typing import Set
import pytest
from day4.day4 import convert_range_to_set, check_if_fully_contained, check_if_overlap


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("2-4", {2, 3, 4}),
        ("6-8", {6, 7, 8}),
        ("2-3", {2, 3}),
        ("4-5", {4, 5}),
        ("5-7", {5, 6, 7}),
        ("7-9", {7, 8, 9}),
        ("2-8", {2, 3, 4, 5, 6, 7, 8}),
        ("3-7", {3, 4, 5, 6, 7}),
        ("6-6", {6}),
        ("4-6", {4, 5, 6}),
        ("2-6", {2, 3, 4, 5, 6}),
        ("4-8", {4, 5, 6, 7, 8}),
    ],
)
def test_convert_range_to_set(input_str: str, expected: Set[int]):
    """Test converting range to set"""
    assert convert_range_to_set(input_str) == expected


@pytest.mark.parametrize(
    "str_1,str_2,expected",
    [
        ("2-4", "6-8", False),
        ("2-3", "4-5", False),
        ("5-7", "7-9", False),
        ("2-8", "3-7", True),
        ("6-6", "4-6", True),
        ("2-6", "4-8", False),
    ],
)
def test_is_subset(str_1: str, str_2: str, expected: bool):
    """Test if the subset check works"""
    assert (
        check_if_fully_contained(
            convert_range_to_set(str_1), convert_range_to_set(str_2)
        )
        == expected
    )


@pytest.mark.parametrize(
    "str_1,str_2,expected",
    [
        ("2-4", "6-8", False),
        ("2-3", "4-5", False),
        ("5-7", "7-9", True),
        ("2-8", "3-7", True),
        ("6-6", "4-6", True),
        ("2-6", "4-8", True),
    ],
)
def test_is_overlap(str_1: str, str_2: str, expected: bool):
    """Test if the subset check works"""
    assert (
        check_if_overlap(convert_range_to_set(str_1), convert_range_to_set(str_2))
        == expected
    )
