"""
Day 1 of 2020 Advent of Code
"""
from typing import List
import itertools


def check_2020(values: tuple) -> bool:
    """
    A generic version of the check_2020 method
    """
    sum_of_all = 0
    for value in values:
        sum_of_all += value
    return sum_of_all == 2020


def get_sums_from_list(values: List[int], values_to_add: int) -> tuple:
    """
    Get the two numbers from a list that add up to 2020
    """
    all_combos = itertools.combinations(values, values_to_add)
    for combo in all_combos:
        if check_2020(combo):
            return combo
    return 0, 0


def get_day_1_answer(values: List[int]) -> int:
    """
    Generate the first day's answer
    """
    answer_first, answer_second = get_sums_from_list(values, 2)
    return answer_first * answer_second


def get_day_2_answer(values: List[int]) -> int:
    """
    Generate the first day's answer
    """
    answer_first, answer_second, answer_third = get_sums_from_list(values, 3)
    return answer_first * answer_second * answer_third


def convert_input_str_to_int(input_values: str) -> List[int]:
    return [int(x) for x in input_values.split("\n")]


def main():
    with open("day_1_input.txt") as f:
        values = f.read().strip()
    list_of_values = convert_input_str_to_int(values)
    print("Part 1: " + str(get_day_1_answer(list_of_values)))
    print("Part 2: " + str(get_day_2_answer(list_of_values)))


if __name__ == "__main__":
    main()
