"""Tests for day9"""

import pytest
from day9.day9 import Point, Head, Direction, parse_directions


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


def test_positions_visited():
    """Test the total amount of places visited for the tail"""
    directions = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    head = Head()
    for instruction in parse_directions(directions):
        head.move(*instruction)
    assert len(head.tail.points_visited) == 13
