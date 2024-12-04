"""Solution for day 4"""

from enum import Enum, auto
from typing import List


class Direction(Enum):
    """helper class for direction"""

    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    UP_LEFT = auto()
    UP_RIGHT = auto()
    DOWN_LEFT = auto()
    DOWN_RIGHT = auto()


def main():
    """solves day 4"""
    input_str = get_input()
    print(f"Part 1: {solve_part_1(input_str)}")
    print(f"Part 2: {solve_part_2(input_str)}")


def solve_part_1(input_str: List[str]) -> int:
    """Solves part 1"""
    total = 0
    for line_i, line in enumerate(input_str):
        for letter_j, _letter in enumerate(line):
            total += (
                1 if is_xmas_word(input_str, line_i, letter_j, "X", Direction.UP) else 0
            )
            total += (
                1
                if is_xmas_word(input_str, line_i, letter_j, "X", Direction.DOWN)
                else 0
            )
            total += (
                1
                if is_xmas_word(input_str, line_i, letter_j, "X", Direction.LEFT)
                else 0
            )
            total += (
                1
                if is_xmas_word(input_str, line_i, letter_j, "X", Direction.RIGHT)
                else 0
            )
            total += (
                1
                if is_xmas_word(input_str, line_i, letter_j, "X", Direction.UP_LEFT)
                else 0
            )
            total += (
                1
                if is_xmas_word(input_str, line_i, letter_j, "X", Direction.UP_RIGHT)
                else 0
            )
            total += (
                1
                if is_xmas_word(input_str, line_i, letter_j, "X", Direction.DOWN_LEFT)
                else 0
            )
            total += (
                1
                if is_xmas_word(input_str, line_i, letter_j, "X", Direction.DOWN_RIGHT)
                else 0
            )

    return total


def solve_part_2(input_str: List[str]) -> int:
    """solves part 2"""
    total = 0
    for line_i, line in enumerate(input_str):
        for letter_j, letter in enumerate(line):
            if letter == "A":
                total += 1 if is_x_mas_cross(input_str, line_i, letter_j) else 0
    return total


def is_x_mas_cross(input_str: List[str], line_loc: int, letter_loc: int) -> bool:
    """checks if the current 'A' is part of an X-MAS word"""
    if letter_loc <= 0 or line_loc <= 0:
        return False

    try:
        up_left_good = (
            input_str[line_loc - 1][letter_loc - 1] == "M"
            and input_str[line_loc + 1][letter_loc + 1] == "S"
        ) or (
            input_str[line_loc - 1][letter_loc - 1] == "S"
            and input_str[line_loc + 1][letter_loc + 1] == "M"
        )
        up_right_good = (
            input_str[line_loc + 1][letter_loc - 1] == "M"
            and input_str[line_loc - 1][letter_loc + 1] == "S"
        ) or (
            input_str[line_loc + 1][letter_loc - 1] == "S"
            and input_str[line_loc - 1][letter_loc + 1] == "M"
        )

        return up_left_good and up_right_good

    except IndexError:
        return False


def is_xmas_word(
    input_str: List[str],
    line_loc: int,
    letter_loc: int,
    letter_to_check: str,
    direction: Direction,
) -> bool:
    """checks if the loc at the current line is a word"""
    if letter_loc < 0 or line_loc < 0:
        return False
    try:
        if input_str[line_loc][letter_loc] != letter_to_check:
            return False
    except IndexError:
        return False

    match letter_to_check:
        case "S":
            return True
        case "X":
            next_letter = "M"
        case "M":
            next_letter = "A"
        case "A":
            next_letter = "S"
        case _:
            raise ValueError("not valid letter")

    match direction:
        case Direction.UP:
            line_loc -= 1
        case Direction.DOWN:
            line_loc += 1
        case Direction.LEFT:
            letter_loc -= 1
        case Direction.RIGHT:
            letter_loc += 1
        case Direction.UP_LEFT:
            line_loc -= 1
            letter_loc -= 1
        case Direction.UP_RIGHT:
            line_loc -= 1
            letter_loc += 1
        case Direction.DOWN_LEFT:
            line_loc += 1
            letter_loc -= 1
        case Direction.DOWN_RIGHT:
            line_loc += 1
            letter_loc += 1
        case _:
            raise ValueError("not valid")
    return is_xmas_word(input_str, line_loc, letter_loc, next_letter, direction)


def get_input() -> List[str]:
    """get the days input file"""
    with open("input_day4.txt", encoding="utf-8") as file:
        return file.readlines()


if __name__ == "__main__":
    main()
