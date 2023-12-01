"""
Day 1 of advent of code 2022
"""
from typing import List


def get_calories_for_elf(elf: List[int]) -> int:
    """
    Returns the number of calories for a single elf
    """
    return sum(elf)


def get_largest_calorie(elves: List[List[int]]) -> int:
    """
    Returns the Largest sum calorie for a list of elves
    """
    return max(get_calories_for_elves(elves))


def parse_input() -> List[List[int]]:
    """
    Parses the day's input
    """
    output = []
    with open("input.txt", "r", encoding="utf-8") as file:
        next_elf: List[int] = []
        for line in file.readlines():
            if not line or line == "\n":
                output.append(next_elf)
                next_elf = []
                continue
            next_elf.append(int(line))
    return output


def get_three_largest_cals(total_cals: List[int]) -> int:
    """
    Returns the sum of the largest 3 cals in a list of elves' total cals
    """
    list.sort(total_cals)
    return sum(total_cals[-3:])


def get_three_largest_cals_for_elves(elves: List[List[int]]) -> int:
    """
    Returns the sum of the largest 3 cals in a list of elves
    """
    return get_three_largest_cals(get_calories_for_elves(elves))


def get_calories_for_elves(elves: List[List[int]]) -> List[int]:
    """
    Returns a list of the sum calories for each elf in a list of elves
    """
    return [get_calories_for_elf(elf) for elf in elves]


def part_1() -> int:
    """
    Solve part 1's problem
    """
    return get_largest_calorie(parse_input())


def part_2() -> int:
    """
    Solve part 2's problem
    """
    return get_three_largest_cals_for_elves(parse_input())


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
