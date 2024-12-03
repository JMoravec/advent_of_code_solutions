"""tests for day 3"""

from day_3.day_3 import solve_part_1, solve_part_2


def test_solve_part_1():
    """tests the solution"""
    input_str = [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    ]
    assert solve_part_1(input_str) == 161


def test_solve_part_2():
    """tests the solution"""
    input_str = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ]
    assert solve_part_2(input_str) == 48
