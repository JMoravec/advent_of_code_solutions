"""
Day 12 of advent of code 2020
"""
from typing import List
from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    WEST = "W"
    EAST = "E"

    @staticmethod
    def get_reverse(direction: "Direction") -> "Direction":
        """
        Get the reverse direction
        """
        if direction == Direction.NORTH:
            return Direction.SOUTH
        if direction == Direction.SOUTH:
            return Direction.NORTH
        if direction == Direction.EAST:
            return Direction.WEST
        if direction == Direction.WEST:
            return Direction.EAST
        return Direction.EAST

    @staticmethod
    def turn_left(direction: "Direction") -> "Direction":
        """
        Turn left
        """
        if direction == Direction.NORTH:
            return Direction.WEST
        if direction == Direction.SOUTH:
            return Direction.EAST
        if direction == Direction.EAST:
            return Direction.NORTH
        if direction == Direction.WEST:
            return Direction.SOUTH
        return Direction.EAST

    @staticmethod
    def turn_right(direction: "Direction") -> "Direction":
        """
        Turn right
        """
        if direction == Direction.NORTH:
            return Direction.EAST
        if direction == Direction.SOUTH:
            return Direction.WEST
        if direction == Direction.EAST:
            return Direction.SOUTH
        if direction == Direction.WEST:
            return Direction.NORTH
        return Direction.EAST


@dataclass
class Boat:
    east_pos: int = 0
    nort_pos: int = 0
    direction: Direction = Direction.EAST

    def turn_boat(self, direction: str, degrees: int):
        final_direction = self.direction
        for _ in range(degrees, 0, -90):
            final_direction = (
                Direction.turn_left(final_direction)
                if direction == "L"
                else Direction.turn_right(final_direction)
            )
        self.direction = final_direction

    def move_boat(self, input_str: str):
        direction_input = input_str[0]
        direction_to_move: Direction

        if direction_input in ["L", "R"]:
            self.turn_boat(direction_input, int(input_str[1:]))
            return
        if direction_input == "F":
            direction_to_move = self.direction
        elif direction_input == "R":
            direction_to_move = Direction.get_reverse(self.direction)
        else:
            direction_to_move = Direction(direction_input)

        amount_to_move = int(input_str[1:])
        if direction_to_move in [Direction.WEST, Direction.SOUTH]:
            amount_to_move = -amount_to_move

        if direction_to_move in [Direction.WEST, Direction.EAST]:
            self.east_pos += amount_to_move
        else:
            self.nort_pos += amount_to_move


def solve_part_1(input_lines: List[str]) -> int:
    boat = Boat()
    for movement in input_lines:
        boat.move_boat(movement)
    return abs(boat.east_pos) + abs(boat.nort_pos)


def main():
    """
    Main method to run the day's input
    """
    with open("day12_input.txt") as problem_file:
        all_inputs = problem_file.readlines()

    print(f"Part 1: {solve_part_1(all_inputs)}")
    # print(f"Part 2: {solve_part_2(all_inputs)}")


if __name__ == "__main__":
    main()
