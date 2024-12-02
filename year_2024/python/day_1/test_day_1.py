"""tests for day 1"""

from day_1.day_1 import solve_part_1, solve_part_2


def test_solve_part_1():
    """test part 1"""
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    answer = solve_part_1(left_list, right_list)
    assert answer == 11


def test_solve_part_2():
    """test part 2"""
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    answer = solve_part_2(left_list, right_list)
    assert answer == 31
