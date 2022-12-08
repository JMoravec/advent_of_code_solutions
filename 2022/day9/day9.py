"""Day 9 of Davent of Code 2022"""

from dataclasses import dataclass
import dataclasses
from enum import Enum
from typing import Set


class Direction(Enum):
    """Enum for direction to move"""

    UP = "U"
    DOWN = "D"
    RIGHT = "R"
    LEFT = "L"


@dataclass
class Point:
    """A single point on the map"""

    x_coor: int
    y_coor: int

    def move(self, direction: Direction) -> "Point":
        """Get the point in the next direction"""
        if direction == Direction.UP:
            self.y_coor += 1
        if direction == Direction.DOWN:
            self.y_coor -= 1
        if direction == Direction.LEFT:
            self.x_coor -= 1
        if direction == Direction.RIGHT:
            self.x_coor += 1
        return self


class Head:
    """Represents the head of the rope"""

    current_position: Point
    tail: Tail

    def __init__(self) -> None:
        self.current_position = Point(0, 0)
        self.tail = Tail()

    def move(self, direction: Direction, how_far: int) -> "Head":
        """Move the head in a given direction and distance"""
        for _ in range(how_far):
            self.current_position.move(direction)
            self.tail.move(self)
        return self


class Tail:
    """Represents the tail of the rope"""

    current_position: Point
    points_visited: Set[Point]

    def __init__(self) -> None:
        self.current_position = Point(0, 0)
        self.points_visited = set()
        self.add_point_to_visited()

    def add_point_to_visited(self):
        """Adds a point to the visited set"""
        self.points_visited.add(dataclasses.replace(self.current_position))

    def move(self, head: Head):
        """Move the tail to the correct position of the Head"""
        pass


def part_1():
    """Solve part 1 of day 9"""
    pass


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    # print(f"Part 2: {part_2()}")
