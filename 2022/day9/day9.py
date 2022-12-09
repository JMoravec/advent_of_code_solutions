"""Day 9 of Davent of Code 2022"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Set, Tuple


class Direction(Enum):
    """Enum for direction to move"""

    UP = "U"
    DOWN = "D"
    RIGHT = "R"
    LEFT = "L"


@dataclass(frozen=True)
class Point:
    """A single point on the map"""

    x_coor: int
    y_coor: int

    def move(self, direction: Direction) -> "Point":
        """Get the point in the next direction"""
        if direction == Direction.UP:
            return Point(self.x_coor, self.y_coor + 1)
        if direction == Direction.DOWN:
            return Point(self.x_coor, self.y_coor - 1)
        if direction == Direction.LEFT:
            return Point(self.x_coor - 1, self.y_coor)
        if direction == Direction.RIGHT:
            return Point(self.x_coor + 1, self.y_coor)
        raise Exception("Direction not available to move")

    def move_to(self, point_to_move_to: "Point") -> "Point":
        """Move the point so its touching the other point"""

        # don't move if its already touching
        if self.x_coor in [
            point_to_move_to.x_coor - 1,
            point_to_move_to.x_coor,
            point_to_move_to.x_coor + 1,
        ] and self.y_coor in [
            point_to_move_to.y_coor - 1,
            point_to_move_to.y_coor,
            point_to_move_to.y_coor + 1,
        ]:
            return self

        # same column
        if self.x_coor == point_to_move_to.x_coor:
            return Point(
                self.x_coor,
                (
                    self.y_coor + 1
                    if self.y_coor < point_to_move_to.y_coor
                    else self.y_coor - 1
                ),
            )
        if self.y_coor == point_to_move_to.y_coor:
            return Point(
                (
                    self.x_coor + 1
                    if self.x_coor < point_to_move_to.x_coor
                    else self.x_coor - 1
                ),
                self.y_coor,
            )
        # diag
        return Point(
            (
                self.x_coor + 1
                if self.x_coor < point_to_move_to.x_coor
                else self.x_coor - 1
            ),
            (
                self.y_coor + 1
                if self.y_coor < point_to_move_to.y_coor
                else self.y_coor - 1
            ),
        )


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
        self.points_visited.add(self.current_position)

    def move(self, head_position: Point):
        """Move the tail to the correct position of the Head"""
        self.current_position = self.current_position.move_to(head_position)
        self.add_point_to_visited()


class Head:
    """Represents the head of the rope"""

    current_position: Point
    tail: Tail

    def __init__(self, rope_segmenets_to_create: int = 9) -> None:
        self.current_position = Point(0, 0)
        self.tail = Tail()

    def move(self, direction: Direction, how_far: int) -> "Head":
        """Move the head in a given direction and distance"""
        for _ in range(how_far):
            self.current_position = self.current_position.move(direction)
            self.tail.move(self.current_position)
        return self


def parse_directions(input_str: str) -> List[Tuple[Direction, int]]:
    """Parse a set of instructions"""
    all_instructions = []
    for line in input_str.splitlines():
        direction_str, length_str = line.strip().split(" ")
        all_instructions.append(
            (Direction(direction_str.strip()), int(length_str.strip()))
        )
    return all_instructions


def part_1() -> int:
    """Solve part 1 of day 9"""
    with open("input.txt", "r", encoding="utf-8") as file:
        all_lines = file.read()
    head = Head()
    for instruction in parse_directions(all_lines):
        head.move(*instruction)
    return len(head.tail.points_visited)


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    # print(f"Part 2: {part_2()}")
