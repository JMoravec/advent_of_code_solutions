"""Tests for day8"""
from day8.day8 import (
    compute_is_visible,
    create_forest,
    get_down_viewing_distance,
    get_left_viewing_distance,
    get_number_of_visible_trees,
    compute_viewing_distance,
    get_right_viewing_distance,
    get_up_viewing_distance,
    get_largest_viewing_distance,
)


TEST_INPUT = """30373
25512
65332
33549
35390"""


def test_get_visible_trees():
    """Test getting the total number of visible trees"""
    forrest = create_forest(TEST_INPUT)
    compute_is_visible(forrest)
    assert get_number_of_visible_trees(forrest) == 21


def test_get_viewing_score():
    """Test getting the individual viewing directions for a few points"""
    forrest = create_forest(TEST_INPUT)
    x = 2
    y = 1
    assert forrest[y][x].value == 5
    assert get_up_viewing_distance(forrest, x, y) == 1
    assert get_left_viewing_distance(forrest, x, y) == 1
    assert get_down_viewing_distance(forrest, x, y) == 2
    assert get_right_viewing_distance(forrest, x, y) == 2

    x = 2
    y = 3
    assert forrest[y][x].value == 5
    assert get_up_viewing_distance(forrest, x, y) == 2
    assert get_left_viewing_distance(forrest, x, y) == 2
    assert get_down_viewing_distance(forrest, x, y) == 1
    assert get_right_viewing_distance(forrest, x, y) == 2


def test_get_computing_distance():
    """Test getting the total number of visible trees"""
    forrest = create_forest(TEST_INPUT)
    compute_viewing_distance(forrest)
    assert forrest[1][2].viewing_score == 4
    assert forrest[3][2].viewing_score == 8
    assert get_largest_viewing_distance(forrest) == 8
