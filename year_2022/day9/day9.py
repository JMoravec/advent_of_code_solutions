"""Day 9 of Davent of Code 2022"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Set, Tuple


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


class Rope:
    """Represents the head of the rope"""

    current_position: Point
    tail: Optional["Rope"]
    points_visited: Set[Point]

    def __init__(self, rope_segmenets_to_create) -> None:
        self.current_position = Point(0, 0)
        if rope_segmenets_to_create > 0:
            self.tail = Rope(rope_segmenets_to_create - 1)
        else:
            self.tail = None
        self.points_visited = set()
        self.add_point_to_visited()

    def move(self, direction: Direction, how_far: int) -> "Rope":
        """Move the head in a given direction and distance"""
        for _ in range(how_far):
            self.current_position = self.current_position.move(direction)
            if self.tail:
                self.tail.move_to(self.current_position)
        return self

    def add_point_to_visited(self):
        """Adds a point to the visited set"""
        self.points_visited.add(self.current_position)

    def move_to(self, head_position: Point):
        """Move the tail to the correct position of the Head"""
        self.current_position = self.current_position.move_to(head_position)
        self.add_point_to_visited()
        if self.tail:
            self.tail.move_to(self.current_position)

    def get_tail_points_visited(self) -> int:
        """Get the final tail's points visited"""
        if not self.tail:
            return len(self.points_visited)
        return self.tail.get_tail_points_visited()


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
    head = Rope(1)
    for instruction in parse_directions(all_lines):
        head.move(*instruction)
    return head.get_tail_points_visited()


def part_2() -> int:
    """Solve part 1 of day 9"""
    with open("input.txt", "r", encoding="utf-8") as file:
        all_lines = file.read()
    head = Rope(9)
    for instruction in parse_directions(all_lines):
        head.move(*instruction)
    return head.get_tail_points_visited()


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
