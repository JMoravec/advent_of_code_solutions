"""
Day 9 of advent of code 2020
"""
import itertools
from typing import Dict, Tuple, List


def generate_list_of_combos(inputs: List[int]) -> Dict[int, Tuple[int, int]]:
    """
    Generate the full list of combinations and sums for a given input
    """
    return_dict: Dict[int, Tuple[int, int]] = {}
    all_combinations = itertools.combinations(inputs, 2)
    for combo in all_combinations:
        return_dict[sum(combo)] = combo
    return return_dict


def solve_part_1(preamble_length: int, inputs: List[int]) -> int:
    """
    Solve part 1 of day 9
    """
    current_set = inputs[0:preamble_length].copy()
    for current_input in inputs[preamble_length:]:
        combos = generate_list_of_combos(current_set)
        if not current_input in combos.keys():
            return current_input

        current_set = current_set[1:]
        current_set.append(current_input)
    return -1


class DefinitlyNotAnswerException(Exception):
    """ Helper exception """


def _check_inner_loop(inputs: List[int], start_index: int, part_1_answer: int) -> int:
    for end_delta in range(1, len(inputs[start_index:])):
        test_answer = sum(inputs[start_index : start_index + end_delta])
        if test_answer == part_1_answer:
            return min(inputs[start_index : start_index + end_delta]) + max(
                inputs[start_index : start_index + end_delta]
            )
        if test_answer > part_1_answer:
            raise DefinitlyNotAnswerException()
    return -1


def solve_part_2(part_1_answer: int, inputs: List[int]) -> int:
    """
    Solve part 1 of day 9
    """
    for start_index, _ in enumerate(inputs):
        try:
            answer = _check_inner_loop(inputs, start_index, part_1_answer)
            if answer != -1:
                return answer
        except DefinitlyNotAnswerException:
            pass
    return -1


def main():
    """
    Main method to run the day's input
    """
    with open("day9_input.txt") as problem_file:
        all_inputs = problem_file.readlines()

    all_inputs_int = [int(number) for number in all_inputs]
    part_1_answer = solve_part_1(25, all_inputs_int)
    print(f"Part 1: {part_1_answer}")
    print(f"Part 2: {solve_part_2(part_1_answer, all_inputs_int)}")


if __name__ == "__main__":
    main()
