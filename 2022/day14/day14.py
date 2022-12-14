"""Day 14 of Advent of Code 2022"""


from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List


class Particle(Enum):
    """Enum that represents what's currently at a point"""

    SAND = auto()
    ROCK = auto()
    VOID = auto()


class CurrentState:
    """Represents the current state of the sand"""

    state: Dict["Point", Particle]
    has_void: bool
    lowest_rock: int

    def __init__(self, initial_state: Dict["Point", Particle], has_void: bool):
        self.state = initial_state
        self.has_void = has_void
        self.lowest_rock = self._get_lowest_rock(self.state)

    def __setitem__(self, point: "Point", particle: Particle):
        self.state[point] = particle

    def __getitem__(self, point: "Point") -> Particle:
        return self.state[point]

    def get(self, point: "Point") -> Particle:
        """Get the particle at a given point"""
        if not self.has_void and point.y_coor == self.lowest_rock + 2:
            return Particle.ROCK

        return self.state.get(point, Particle.VOID)

    @staticmethod
    def _get_lowest_rock(current_state: Dict["Point", Particle]) -> int:
        """Get the lowest possible rock position"""
        lowest_point = 0
        for point in current_state.keys():
            if point.y_coor > lowest_point:
                lowest_point = point.y_coor
        return lowest_point


@dataclass(frozen=True)
class Point:
    """Represents a single point"""

    x_coor: int
    y_coor: int

    @staticmethod
    def create_from_str(input_str: str) -> "Point":
        """Create a point from an input value"""
        split_input = input_str.split(",")
        if len(split_input) != 2:
            raise Exception("Incorrect input for Point")
        return Point(int(split_input[0].strip()), int(split_input[1].strip()))

    def simulate_sand_move_single(self, current_state: CurrentState) -> "Point":
        """Simulate a single movement of sand at the current point"""
        below_point = Point(self.x_coor, self.y_coor + 1)
        test_point = current_state.get(below_point)
        # if below is void, move to that point
        if test_point == Particle.VOID:
            return below_point
        if test_point in [Particle.ROCK, Particle.SAND]:
            # if below and to the left is void, move to that poitn
            below_left = Point(self.x_coor - 1, self.y_coor + 1)
            if current_state.get(below_left) == Particle.VOID:
                return below_left
            # if blow and to the right, move to that point
            below_right = Point(self.x_coor + 1, self.y_coor + 1)
            if current_state.get(below_right) == Particle.VOID:
                return Point(self.x_coor + 1, self.y_coor + 1)

        # doesn't move
        return self


def parse_single_line_str(input_line: str, current_state: Dict[Point, Particle]):
    """Parse a single line of input and add to the current state"""
    points: List[Point] = []
    for point_str in input_line.split(" -> "):
        points.append(Point.create_from_str(point_str.strip()))

    last_point = None
    for point in points:
        if last_point is None:
            last_point = point
            continue
        # vertical line
        if point.x_coor == last_point.x_coor:
            max_item = max(last_point.y_coor, point.y_coor)
            min_item = min(last_point.y_coor, point.y_coor)
            for y_index in range(min_item, max_item + 1):
                current_state[Point(point.x_coor, y_index)] = Particle.ROCK
        # horizontal line
        if point.y_coor == last_point.y_coor:
            max_item = max(last_point.x_coor, point.x_coor)
            min_item = min(last_point.x_coor, point.x_coor)
            for x_index in range(min_item, max_item + 1):
                current_state[Point(x_index, point.y_coor)] = Particle.ROCK
        last_point = point


def parse_all_lines(input_str: str, has_void: bool = True) -> CurrentState:
    """Parse all of the input lines and return a dict of the current state"""
    current_state_dict: Dict[Point, Particle] = {}
    for line in input_str.splitlines():
        parse_single_line_str(line, current_state_dict)
    current_state = CurrentState(current_state_dict, has_void)
    return current_state


def simulate_single_sand(current_state: CurrentState, start_point: Point) -> bool:
    """Simulates a single point of sand, returns False if it falls forever or
    hits the starting point"""
    current_point = start_point
    while True:
        next_point = current_point.simulate_sand_move_single(current_state)
        if current_state.has_void and next_point.y_coor > current_state.lowest_rock:
            return False
        if next_point == current_point:
            current_state[next_point] = Particle.SAND
            return current_point != start_point
        current_point = next_point


def get_total_units_of_sand(current_state: CurrentState, start_point: Point) -> int:
    """Get the total units of sand coming to rest before one falls forever"""
    total_units = 0
    while simulate_single_sand(current_state, start_point):
        total_units += 1
    return total_units


def part_1() -> int:
    """Solve part 1 of day 14"""
    with open("input.txt", "r", encoding="utf-8") as file:
        input_str = file.read()
    current_state = parse_all_lines(input_str)
    return get_total_units_of_sand(current_state, Point(500, 0))


def part_2() -> int:
    """Solve part 1 of day 14"""
    with open("input.txt", "r", encoding="utf-8") as file:
        input_str = file.read()
    current_state = parse_all_lines(input_str, False)
    return get_total_units_of_sand(current_state, Point(500, 0)) + 1


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
