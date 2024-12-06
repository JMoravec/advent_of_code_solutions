"""Solution for day 6"""

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Set, Tuple


class Direction(Enum):
    """helper enum for direction"""

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def turn(self) -> "Direction":
        match self:
            case Direction.UP:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP
            case _:
                raise ValueError()


@dataclass
class Gaurd:
    location_x: int
    location_y: int
    direction: Direction
    traveled_locations: Dict[int, Set[Tuple[int, Direction]]]
    in_loop: bool = False

    def copy(self) -> "Gaurd":
        traveled_locations: Dict[int, Set[Tuple[int, Direction]]] = defaultdict(set)
        traveled_locations[self.location_x].add((self.location_y, Direction.UP))
        return Gaurd(self.location_x, self.location_y, Direction.UP, traveled_locations)

    def move(self, full_map: List[str]) -> bool:
        dir_x, dir_y = self.direction.value
        new_test_x = dir_x + self.location_x
        new_test_y = dir_y + self.location_y
        if (
            new_test_x < 0
            or new_test_x > len(full_map[0]) - 1
            or new_test_y < 0
            or new_test_y > len(full_map) - 1
        ):
            return False

        if full_map[new_test_y][new_test_x] == "#":
            self.direction = self.direction.turn()
            return True

        if (new_test_y, self.direction) in self.traveled_locations[new_test_x]:
            self.in_loop = True
            return False

        self.location_x = new_test_x
        self.location_y = new_test_y
        self.traveled_locations[self.location_x].add((self.location_y, self.direction))
        return True


def main():
    """solves day 6"""
    lines, guard = get_input()
    guard_1 = guard.copy()
    guard_2 = guard.copy()
    print(f"Part 1: {solve_part_1(lines, guard_1)}")
    print(f"Part 2: {solve_part_2(lines, guard_2)}")


def solve_part_1(lines: List[str], guard: Gaurd) -> int:
    """solves part 1"""
    traveled_locations: Dict[int, Set[int]] = defaultdict(set)
    traveled_locations[guard.location_x].add(guard.location_y)
    while guard.move(lines):
        traveled_locations[guard.location_x].add(guard.location_y)

    total = 0
    for _, y_values in traveled_locations.items():
        total += len(y_values)

    return total


def solve_part_2(lines: List[str], guard: Gaurd) -> int:
    """solves part 2"""
    original_guard = guard.copy()
    original_lines = lines.copy()
    potential_locations: Dict[int, Set[int]] = defaultdict(set)
    potential_locations[guard.location_x].add(guard.location_y)
    while guard.move(lines):
        potential_locations[guard.location_x].add(guard.location_y)

    potential_locations[original_guard.location_x].remove(original_guard.location_y)

    loops = 0
    for x, y_values in potential_locations.items():
        for y in y_values:
            new_guard = original_guard.copy()
            new_map = original_lines.copy()
            line_list = list(new_map[y])
            line_list[x] = "#"
            new_map[y] = "".join(line_list)
            while new_guard.move(new_map):
                pass
            if new_guard.in_loop:
                loops += 1

    return loops


def get_input() -> Tuple[List[str], Gaurd]:
    """get the days input file"""
    lines = []
    with open("input_day6.txt", encoding="utf-8") as file:
        for line in file:
            lines.append(line)

    gaurd = get_initial_guard(lines)

    return lines, gaurd


def get_initial_guard(lines: List[str]) -> Gaurd:
    """get the initial position of the guard"""
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "^":
                traveled_locations: Dict[int, Set[Tuple[int, Direction]]] = defaultdict(
                    set
                )
                traveled_locations[x].add((y, Direction.UP))
                return Gaurd(x, y, Direction.UP, traveled_locations)
    raise ValueError("Gaurd not found")


if __name__ == "__main__":
    main()
