"""Tests for day 12"""
from day12.day12 import (
    parse_graph,
    Point,
    find_shortest_path,
    find_shortest_starting_path,
)

TEST_INPUT = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def test_parse_graph():
    """Test parsing the input works correctly"""
    starting_point, ending_point, all_points = parse_graph(TEST_INPUT)
    assert starting_point == Point(0, 0, 0, 0)
    assert ending_point == Point(5, 2, 25, 999999)
    assert all_points[0][0] == starting_point
    assert all_points[2][5] == ending_point
    assert all_points[4][7] == Point(7, 4, 8, 999999)


def test_find_shortest_path():
    """Test finding the shortest path"""
    assert find_shortest_path(*parse_graph(TEST_INPUT)) == 31


def test_find_shortest_starting_path():
    """Test finding the shortest path for any starting point"""
    assert find_shortest_starting_path(TEST_INPUT) == 29
