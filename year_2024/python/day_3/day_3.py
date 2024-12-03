"""solution for day3"""

import re
from typing import List


def main():
    """solves day 3"""
    input_str = get_input()
    print(f"Part 1: {solve_part_1(input_str)}")
    print(f"Part 2: {solve_part_2(input_str)}")


def get_input() -> List[str]:
    """get the days input file"""
    with open("input_day3.txt", encoding="utf-8") as file:
        return file.readlines()


def solve_part_1(input_str: List[str]) -> int:
    """solves part 1"""
    regex = re.compile(r"mul\(\d+,\d+\)")
    num_reg = re.compile(r"\d+")
    all_matches = []
    total = 0
    for line in input_str:
        all_matches += regex.findall(line)
    for match in all_matches:
        nums = num_reg.findall(match)
        total += int(nums[0]) * int(nums[1])
    return total


def solve_part_2(input_str: List[str]) -> int:
    """solves part 2"""
    regex = re.compile(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)")
    num_reg = re.compile(r"\d+")
    all_matches = []
    total = 0
    mul_on = True
    full_input = "".join(input_str)
    all_matches += regex.findall(full_input)
    for match in all_matches:
        if match[0:3] == "do(":
            mul_on = True
        elif match[0:3] == "don":
            mul_on = False
        elif mul_on:
            nums = num_reg.findall(match)
            total += int(nums[0]) * int(nums[1])
        continue
    return total


if __name__ == "__main__":
    main()
