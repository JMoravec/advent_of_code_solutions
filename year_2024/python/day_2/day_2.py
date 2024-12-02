"""solution for day 2"""

from enum import Enum, auto

import functools
from typing import List, Tuple


class IncDec(Enum):
    """helper class for type of change"""

    INC = auto()
    DEC = auto()
    EQUAL = auto()

    @staticmethod
    # @functools.cache
    def get_from_diff(diff: int) -> "IncDec":
        """get from a diff"""
        if diff == 0:
            return IncDec.EQUAL
        if diff > 0:
            return IncDec.DEC
        return IncDec.INC


def get_input() -> List[List[int]]:
    """get the days input file"""
    output = []
    with open("input_day2.txt", encoding="utf-8") as file:
        for line in file:
            output.append([int(x) for x in line.strip().split()])
    return output


def main():
    """Main function for solution"""
    all_lines = get_input()
    part_1_sol = solve_part_1(all_lines)
    print(part_1_sol)
    part_2_sol = solve_part_2(all_lines)
    print(part_2_sol)


def solve_part_1(lines: List[List[int]]) -> int:
    """solves part 1"""
    total = 0
    for line in lines:
        if is_line_safe(line):
            total += 1
    return total


def solve_part_2(lines: List[List[int]]) -> int:
    """solves part 2"""
    total = 0
    for line in lines:
        if is_line_safe_v2(line):
            total += 1
    return total


def is_line_safe(line: List[int]) -> bool:
    """checks if the line is safe"""
    increase = IncDec.get_from_diff(line[0] - line[1])
    for i in range(len(line) - 1):
        diff, inc_dec = check_nums(line[i], line[i + 1])
        if diff or (increase != inc_dec):
            return False
    return True


def is_line_safe_v2(line: List[int]) -> bool:
    """check a line with dampening"""

    @functools.cache
    def dp(i: int, inc_dec: IncDec, has_taken: bool) -> bool:
        if i == 0:
            return True

        diff, inc_dec_test = check_nums(line[i], line[i - 1])
        if not diff and inc_dec_test == inc_dec:
            main_result = dp(i - 1, inc_dec, has_taken)
        else:
            main_result = False
        if not has_taken:
            if i < 2:
                return True
            diff, inc_dec_test = check_nums(line[i], line[i - 2])
            take_result = (
                not diff and inc_dec_test == inc_dec and dp(i - 2, inc_dec, True)
            )
        else:
            take_result = False
        return main_result or take_result

    return (
        dp(len(line) - 1, IncDec.INC, False)
        or dp(len(line) - 1, IncDec.DEC, False)
        or dp(len(line) - 2, IncDec.INC, True)
        or dp(len(line) - 2, IncDec.DEC, True)
    )


@functools.cache
def check_nums(num1: int, num2: int) -> Tuple[bool, IncDec]:
    """Check if the diff between two nums is greater than 3"""
    diff = num1 - num2
    return (abs(diff) > 3), IncDec.get_from_diff(diff)


if __name__ == "__main__":
    main()
