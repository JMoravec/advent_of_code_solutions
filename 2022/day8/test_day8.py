"""Tests for day8"""
from day8.day8 import (
    compute_is_visible,
    create_forest,
    get_number_of_visible_trees,
    compute_viewing_distance,
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


def test_get_computing_distance():
    """Test getting the total number of visible trees"""
    forrest = create_forest(TEST_INPUT)
    compute_viewing_distance(forrest)
    assert forrest[0][2].viewing_score == 4
    assert forrest[3][2].viewing_score == 8
