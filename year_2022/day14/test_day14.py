"""Tests for day 14"""
from year_2022.day14.day14 import (
    parse_all_lines,
    Point,
    Particle,
    simulate_single_sand,
    get_total_units_of_sand,
)

TEST_INPUT = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def test_parse_input():
    """Test that creating the state works as expected"""
    current_state = parse_all_lines(TEST_INPUT)
    assert len(current_state.state.keys()) == 20
    assert current_state.get(Point(498, 5)) == Particle.ROCK
    assert current_state.get(Point(498, 9)) == Particle.ROCK


def test_lowest_point():
    """Test that getting the lowest possible rock works as expected"""
    current_state = parse_all_lines(TEST_INPUT)
    assert current_state.lowest_rock == 9


def test_single_sand():
    """Tests running a single sand simulation"""
    current_state = parse_all_lines(TEST_INPUT)
    start_point = Point(500, 0)
    assert simulate_single_sand(current_state, start_point)
    assert current_state[Point(500, 8)] == Particle.SAND

    assert simulate_single_sand(current_state, start_point)
    assert current_state[Point(500, 8)] == Particle.SAND
    assert current_state[Point(499, 8)] == Particle.SAND

    for _ in range(3):
        assert simulate_single_sand(current_state, start_point)

    assert current_state[Point(500, 8)] == Particle.SAND
    assert current_state[Point(499, 8)] == Particle.SAND
    assert current_state[Point(498, 8)] == Particle.SAND
    assert current_state[Point(501, 8)] == Particle.SAND
    assert current_state[Point(500, 7)] == Particle.SAND


def test_single_sand_full_test():
    """Tests running a single sand simulation"""
    current_state = parse_all_lines(TEST_INPUT)
    start_point = Point(500, 0)
    for _ in range(22):
        assert simulate_single_sand(current_state, start_point)
    assert current_state[Point(500, 2)] == Particle.SAND
    assert current_state[Point(499, 3)] == Particle.SAND
    assert current_state[Point(501, 3)] == Particle.SAND

    assert simulate_single_sand(current_state, start_point)
    assert simulate_single_sand(current_state, start_point)
    assert simulate_single_sand(current_state, start_point) is False


def test_total_units_of_sand():
    """Test that getting the total units of sand falling is correct"""
    current_state = parse_all_lines(TEST_INPUT)
    start_point = Point(500, 0)
    assert get_total_units_of_sand(current_state, start_point) == 24


def test_total_units_of_sand_no_void():
    """Test that getting the total units of sand falling is correct"""
    current_state = parse_all_lines(TEST_INPUT, False)
    start_point = Point(500, 0)
    assert get_total_units_of_sand(current_state, start_point) + 1 == 93
