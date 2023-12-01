"""Tests for day9"""

import pytest
from year_2022.day9.day9 import Point, Rope, Direction, parse_directions


@pytest.mark.parametrize(
    "initial_point,move_direction,expected_point",
    [
        (Point(3, 1), Direction.RIGHT, Point(4, 1)),
        (Point(3, 1), Direction.LEFT, Point(2, 1)),
        (Point(3, 1), Direction.UP, Point(3, 2)),
        (Point(3, 1), Direction.DOWN, Point(3, 0)),
    ],
)
def test_move_point(
    initial_point: Point, move_direction: Direction, expected_point: Point
):
    """Test that moving a point produces the expected point value"""
    assert initial_point.move(move_direction) == expected_point


@pytest.mark.parametrize(
    "tail_pos,head_position,expected_tail_pos",
    [
        (Point(1, 1), Point(2, 1), Point(1, 1)),
        (Point(1, 1), Point(1, 1), Point(1, 1)),
        (Point(1, 1), Point(3, 1), Point(2, 1)),
        (Point(1, 3), Point(1, 2), Point(1, 3)),
        (Point(1, 3), Point(1, 1), Point(1, 2)),
        (Point(1, 1), Point(2, 2), Point(1, 1)),
        (Point(1, 1), Point(2, 3), Point(2, 2)),
        (Point(1, 1), Point(3, 2), Point(2, 2)),
    ],
)
def test_move_point_to(tail_pos: Point, head_position: Point, expected_tail_pos: Point):
    """Test moving a point towards another point"""
    assert tail_pos.move_to(head_position) == expected_tail_pos


@pytest.mark.parametrize(
    "directions,rope_segments,expected_positions",
    [
        ("R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2", 1, 13),
        ("R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2", 9, 1),
        ("R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20", 9, 36),
    ],
)
def test_positions_visited_longer_tail(
    directions: str, rope_segments: int, expected_positions: int
):
    """Test the total amount of places visited for the tail"""
    head = Rope(rope_segments)
    for instruction in parse_directions(directions):
        head.move(*instruction)
    assert head.get_tail_points_visited() == expected_positions
