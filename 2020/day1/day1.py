"""
Day 1 of 2020 Advent of Code
"""
from typing import List, Tuple
import itertools

def check_2020(value_1: int, value_2: int) -> bool:
    """
    See if two values add to 2020

    :param value_1: The first value
    :param value_2: The second value
    :return: True if adding them equals 2020
    """
    return value_1 + value_2 == 2020

def get_sums_from_list(values: List[int]) -> Tuple[int, int]:
    """
    Get the two numbers from a list that add up to 2020
    """
    for combo in itertools.combinations(values,2):
        if check_2020(combo[0], combo[1]):
            return combo
    return 0, 0

def get_day_1_answer(values: str) -> int:
    """
    Generate the first day's answer
    """
    list_of_values = [int(x) for x in values.split('\n')]
    answer_first, answer_second = get_sums_from_list(list_of_values)
    return answer_first * answer_second


def main():
    with open('day_1_input.txt') as f:
        values = f.read().strip()
    print(get_day_1_answer(values))

if __name__ == '__main__':
    main()
