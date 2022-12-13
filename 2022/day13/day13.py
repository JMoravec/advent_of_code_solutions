"""Day 13 of Advent of Code 2022"""

from enum import Enum, auto
from functools import cmp_to_key
from itertools import zip_longest
import json
from typing import Any, List, Tuple, Union


class CompareValues(Enum):
    """Enum representing 3 states of comparing two values"""

    TRUE = auto()
    FALSE = auto()
    CONTINUE = auto()


def compare_two_values(left: Any, right: Any) -> CompareValues:
    """Check if two lines are in the correct order"""
    if left is None and right is None:
        return CompareValues.CONTINUE
    if left is None and right is not None:
        return CompareValues.TRUE
    if left is not None and right is None:
        return CompareValues.FALSE

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return CompareValues.TRUE
        if left > right:
            return CompareValues.FALSE
        return CompareValues.CONTINUE

    new_list = None
    if isinstance(left, list) and isinstance(right, list):
        new_list = zip_longest(left, right, fillvalue=None)
    if isinstance(left, list) and isinstance(right, int):
        new_list = zip_longest(left, [right], fillvalue=None)
    if isinstance(left, int) and isinstance(right, list):
        new_list = zip_longest([left], right, fillvalue=None)

    if new_list:
        for new_left, new_right in new_list:
            result = compare_two_values(new_left, new_right)
            if result != CompareValues.CONTINUE:
                return result
    return CompareValues.CONTINUE


def sort_inputs(input_list: list) -> list:
    """Get the sorted list of inputs"""

    def _cmp_values(left, right):
        result = compare_two_values(left, right)
        if result == CompareValues.TRUE:
            return -1
        elif result == CompareValues.FALSE:
            return 1
        return 0

    input_list.append([[2]])
    input_list.append([[6]])

    return sorted(input_list, key=cmp_to_key(_cmp_values))


def parse_list_from_str(
    input_str: str,
) -> List[Tuple[List[Union[int, list]], List[Union[int, list]]]]:
    """Parse an input string into a list of inptus"""
    final_list = []
    all_lines = iter(input_str.splitlines())
    while True:
        try:
            left_line = json.loads(next(all_lines))
            right_line = json.loads(next(all_lines))
            final_list.append((left_line, right_line))
            # blank line
            next(all_lines)
        except StopIteration:
            break

    return final_list


def parse_list_from_str_flat(input_str: str) -> list:
    """Parse the input into a flat list"""
    final_list = []
    all_lines = iter(input_str.splitlines())
    while True:
        try:
            left_line = json.loads(next(all_lines))
            final_list.append(left_line)
            right_line = json.loads(next(all_lines))
            final_list.append(right_line)
            # blank line
            next(all_lines)
        except StopIteration:
            break
    return final_list


def get_indexes_of_correct_order(
    input_list: List[Tuple[List[Union[int, list]], List[Union[int, list]]]]
) -> List[int]:
    """Get all the indexes of the correct order"""
    correct_indexes = []
    for index, test_input in enumerate(input_list):
        if compare_two_values(*test_input) == CompareValues.TRUE:
            correct_indexes.append(index + 1)
    return correct_indexes


def get_sum_of_indexes(input_indexes: List[int]) -> int:
    """Get the sum of the indexes"""
    return sum(input_indexes)


def get_decoder_value(sorted_list: list) -> int:
    """Get the decoder value of a sorted list"""
    return (sorted_list.index([[2]]) + 1) * (sorted_list.index([[6]]) + 1)


def part_1() -> int:
    """Solve part 1 of day 13"""
    with open("input.txt", "r", encoding="utf-8") as file:
        all_lines = file.read()
    all_input = parse_list_from_str(all_lines)
    return get_sum_of_indexes(get_indexes_of_correct_order(all_input))


def part_2() -> int:
    """Solve part 2 of day 13"""
    with open("input.txt", "r", encoding="utf-8") as file:
        all_lines = file.read()
    all_input = parse_list_from_str_flat(all_lines)
    return get_decoder_value(sort_inputs(all_input))


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
