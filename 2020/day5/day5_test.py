"""
Test module for day 5 2020
"""
from typing import Tuple
import pytest
from day5.day5 import get_row, get_seat, get_row_and_seat, get_seat_id_from_input


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("FBFBBFF", 44),
        ("BFFFBBF", 70),
        ("FFFBBBF", 14),
        ("BBFFBBF", 102),
    ],
)
def test_get_row(input_str: str, expected: int):
    """
    Validate that getting the row number works as expected
    """
    assert get_row(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("RLR", 5),
        ("RRR", 7),
        ("RRR", 7),
        ("RLL", 4),
    ],
)
def test_get_seat(input_str: str, expected: int):
    """
    Validate that getting the row number works as expected
    """
    assert get_seat(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("FBFBBFFRLR", (44, 5)),
        ("BFFFBBFRRR", (70, 7)),
        ("FFFBBBFRRR", (14, 7)),
        ("BBFFBBFRLL", (102, 4)),
    ],
)
def test_get_row_and_seat(input_str: str, expected: Tuple[int, int]):
    """
    Validate that getting the row number works as expected
    """
    assert get_row_and_seat(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_get_seat_id(input_str: str, expected: int):
    """
    Validate that getting the seatid number works as expected
    """
    assert get_seat_id_from_input(input_str) == expected
