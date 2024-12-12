"""tests for day 7"""

from typing import List, Tuple

import pytest

from day_7.day_7 import check_line, check_line_v2, get_line_from_str, solve_part_1

line_test_data = [
    (190, [10, 19], True),
    (3267, [81, 40, 27], True),
    (83, [17, 5], False),
    (156, [15, 6], False),
    (7290, [6, 8, 6, 15], False),
    (161011, [16, 10, 13], False),
    (192, [17, 8, 14], False),
    (21037, [9, 7, 18, 13], False),
    (292, [11, 6, 16, 20], True),
]


@pytest.mark.parametrize("num,line,expected", line_test_data)
def test_check_line(num: int, line: List[int], expected: bool):
    """test a single line"""
    assert check_line(num, line) == expected


@pytest.mark.parametrize("num,line,expected", line_test_data)
def test_check_line_v2(num: int, line: List[int], expected: bool):
    """test a single line"""
    assert check_line_v2(num, line[0], line[1:]) == expected


line_test_data_part_2 = [
    (190, [10, 19], True),
    (3267, [81, 40, 27], True),
    (83, [17, 5], False),
    (156, [15, 6], True),
    (7290, [6, 8, 6, 15], True),
    (161011, [16, 10, 13], False),
    (192, [17, 8, 14], True),
    (21037, [9, 7, 18, 13], False),
    (292, [11, 6, 16, 20], True),
]


@pytest.mark.parametrize("num,line,expected", line_test_data_part_2)
def test_check_line_part_2(num: int, line: List[int], expected: bool):
    """test a single line"""
    assert check_line_v2(num, line[0], line[1:], True) == expected


process_test_data = [
    ("190: 10 19", (190, [10, 19])),
    ("3267: 81 40 27", (3267, [81, 40, 27])),
    ("83: 17 5", (83, [17, 5])),
    ("156: 15 6", (156, [15, 6])),
    ("7290: 6 8 6 15", (7290, [6, 8, 6, 15])),
    ("161011: 16 10 13", (161011, [16, 10, 13])),
    ("192: 17 8 14", (192, [17, 8, 14])),
    ("21037: 9 7 18 13", (21037, [9, 7, 18, 13])),
    ("292: 11 6 16 20", (292, [11, 6, 16, 20])),
]


@pytest.mark.parametrize("input_str,expected", process_test_data)
def test_process_line(input_str: str, expected: Tuple[int, List[int]]):
    """test the input getter"""
    assert get_line_from_str(input_str) == expected


def test_solve_part_1():
    """test part 1 with example input"""
    input_str = [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20",
    ]
    assert solve_part_1(input_str) == 3749
