"""tests for day 2"""

from typing import List

import pytest

from day_2.day_2 import is_line_safe, is_line_safe_v2, solve_part_1, solve_part_2


def test_solve_part_1():
    """test for part 1"""
    test_data = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert solve_part_1(test_data) == 2


def test_solve_part_2():
    """test for part 2"""
    test_data = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert solve_part_2(test_data) == 4


line_test_data = [
    ([7, 6, 4, 2, 1], True),
    ([1, 2, 7, 8, 9], False),
    ([9, 7, 6, 2, 1], False),
    ([1, 3, 2, 4, 5], False),
    ([8, 6, 4, 4, 1], False),
    ([1, 3, 6, 7, 9], True),
]


@pytest.mark.parametrize("line,expected", line_test_data)
def test_is_line_safe(line: List[int], expected: bool):
    """test line safety"""
    actual = is_line_safe(line)
    assert expected == actual


line_test_data_v2 = [
    ([7, 6, 4, 2, 1], True),
    ([1, 2, 7, 8, 9], False),
    ([9, 7, 6, 2, 1], False),
    ([1, 3, 2, 4, 5], True),
    ([8, 6, 4, 4, 1], True),
    ([1, 3, 6, 7, 9], True),
    ([9, 3, 6, 7, 9], True),
    ([-50, 3, 6, 7, 9], True),
    ([1, 3, 6, 7, 5], True),
    ([9, 3, 6, 7, 5], False),
    ([57, 56, 57, 59, 60, 63, 64, 65], True),
    ([91, 92, 95, 93, 94], True),
    ([16, 13, 15, 13, 12, 11, 9, 6], True),
    ([40, 41, 43, 44, 47, 46, 47, 49], True),
    ([1, 1, 4, 5, 7, 8], True),
    ([1, 1, 1, 1, 1, 8], False),
    ([1, 6, 2], True),
    ([2, 0, 4, 5, 6], True),
    ([14, 15, 14, 16, 17], True),
]


@pytest.mark.parametrize("line,expected", line_test_data_v2)
def test_is_line_safe_v2(line: List[int], expected: bool):
    """test line safety"""
    actual = is_line_safe_v2(line)
    assert expected == actual
