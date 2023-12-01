"""
Day 5 of advent of code 2020
"""

from typing import Tuple, List
import bisect


def _convert_to_binary(input_str: str) -> int:
    """
    Convert a given input str to binary and return the base 10 value
    """
    new_string = "0b"
    for char in input_str:
        if char in ["F", "L"]:
            new_string += "0"
        else:
            new_string += "1"
    return int(new_string, 2)


def get_row(input_str: str) -> int:
    """
    Get the row from an input string of 7 chars
    """
    assert len(input_str) == 7
    return _convert_to_binary(input_str)


def get_seat(input_str: str) -> int:
    """
    Get the seat from an input string of 3 chars
    """
    assert len(input_str) == 3
    return _convert_to_binary(input_str)


def get_row_and_seat(input_str: str) -> Tuple[int, int]:
    """
    Get the row and seat from a full 10 char input
    """
    assert len(input_str) == 10
    return get_row(input_str[:7]), get_seat(input_str[7:])


def get_seat_id(row: int, seat: int) -> int:
    """
    Get the seat id value for a given row and seat
    """
    return row * 8 + seat


def get_seat_id_from_input(input_str: str) -> int:
    """
    Solve the part 1 problem for a given input
    """
    return get_seat_id(*get_row_and_seat(input_str))


def solve_part_1(inputs: List[str]) -> int:
    """
    Solve the problem in part 1
    """
    max_seat_id = 0
    for test_input in inputs:
        new_id = get_seat_id_from_input(test_input.strip())
        if new_id > max_seat_id:
            max_seat_id = new_id
    return max_seat_id


def solve_part_2(inputs: List[str]) -> int:
    """
    Solve the problem in part 2
    """
    seats = []
    for test_input in inputs:
        seat_id = get_seat_id_from_input(test_input.strip())
        bisect.insort(seats, seat_id)
    last_seat = seats[0] - 1
    for seat in seats:
        if last_seat + 1 != seat:
            return last_seat + 1
        last_seat = seat
    return 0


def main():
    """
    Main method to run the day's input
    """
    with open("day5_input.txt") as problem_file:
        all_inputs = problem_file.readlines()
    print(f"Part 1: {solve_part_1(all_inputs)}")
    print(f"Part 2: {solve_part_2(all_inputs)}")


if __name__ == "__main__":
    main()
