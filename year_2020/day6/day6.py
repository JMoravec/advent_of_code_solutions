"""
Day 6 of advent of code 2020
"""
from typing import Dict
import itertools


def count_group(input_str: str) -> int:
    """
    Count the amount of unique answers in a group
    """
    individuals = input_str.strip().split("\n")
    unique_choices = set()
    for individual in individuals:
        for char in individual:
            unique_choices.add(char)
    return len(unique_choices)


def count_all_group(input_str: str) -> int:
    """
    Count the amount of answers that are common to each person in a group
    """
    individuals = input_str.strip().split("\n")
    unique_choices: Dict[str, int] = {}
    for char in individuals[0]:
        unique_choices[char] = 1

    if len(individuals) == 1:
        return len(unique_choices)

    for individual in individuals[1:]:
        for char in individual:
            if char in unique_choices.keys():
                unique_choices[char] += 1

    total = 0
    for value in unique_choices.values():
        if value == len(individuals):
            total += 1
    return total


def solve_part_1(input_str: str) -> int:
    """
    Solve part 1 for a given input
    """
    all_groups = input_str.split("\n\n")
    total = 0
    for group in all_groups:
        total += count_group(group)
    return total


def solve_part_2(input_str: str) -> int:
    """
    Solve part 2 for a given input
    """
    all_groups = input_str.split("\n\n")
    total = 0
    for group in all_groups:
        total += count_all_group(group)
    return total


def main():
    """
    Main method to run the day's input
    """
    with open("day6_input.txt") as problem_file:
        all_inputs = problem_file.read()
    print(f"Part 1: {solve_part_1(all_inputs)}")
    print(f"Part 2: {solve_part_2(all_inputs)}")


if __name__ == "__main__":
    main()
