"""Tests for day3 of 2023"""

from year_2023.python.day3.day3 import find_part_nums, find_part_nums_part2


TEST_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
/....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_find_part_nums():
    """Validate that the solution to part 1 works correctly"""
    assert find_part_nums(TEST_INPUT.splitlines()) == 4361


def test_find_part_nums2():
    """Validate that the solution to part 1 works correctly"""
    assert find_part_nums_part2(TEST_INPUT.splitlines()) == 467835


def test_find_part_nums_more():
    """Validate that the solution to part 1 works correctly"""
    test_input = """$..
.11
.11
$..
..$
11.
11.
..$"""
    assert find_part_nums(test_input.splitlines()) == 44


def test_find_part_nums_more_more():
    """Validate that the solution to part 1 works correctly"""
    test_input = """........
.24$-4..
......*."""
    assert find_part_nums(test_input.splitlines()) == 28


def test_find_part_nums_more_more_more():
    """Validate that the solution to part 1 works correctly"""
    test_input = """97..
...*
100."""
    assert find_part_nums(test_input.splitlines()) == 100


def test_find_part_nums_more_more_more_2():
    """Validate that the solution to part 1 works correctly"""
    test_input = """....................
..-52..52-..52..52..
..................-."""
    assert find_part_nums(test_input.splitlines()) == 156


def test_find_part_nums_more_more_more_3():
    """Validate that the solution to part 1 works correctly"""
    test_input = """.......5......
..7*..*.......
...*13*.......
.......15....."""
    assert find_part_nums(test_input.splitlines()) == 40


def test_find_part_nums_more_more_more_4():
    """Validate that the solution to part 1 works correctly"""
    test_input = """100
200"""
    assert find_part_nums(test_input.splitlines()) == 0


def test_find_part_nums_more_more_more_more_more():
    """Validate that the solution to part 1 works correctly"""
    test_input = """12.......*..
+.........34
.......-12..
..78........
..*....60...
78.........9
.5.....23..$
8...90*12...
............
2.2......12.
.*.........*
1.1..503+.56"""
    assert find_part_nums(test_input.splitlines()) == 925


def test_find_part_nums_more_more_more_more():
    """Validate that the solution to part 1 works correctly"""
    test_input = """12.......*..
+.........34
.......-12..
..78........
..*....60...
78..........
.......23...
....90*12...
............
2.2......12.
.*.........*
1.1.......56"""
    assert find_part_nums(test_input.splitlines()) == 413
