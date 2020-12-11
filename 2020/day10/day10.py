"""
Day 10 of advent of code 2020
"""
from typing import List, Dict


def solve_part_1(input_nums: List[int]) -> int:
    """
    Solve part 1 of the day
    """
    input_nums.sort()
    one_jumps = 0
    three_jumps = 0
    for i, value in enumerate(input_nums, start=1):
        if i == 1:
            if value == 1:
                one_jumps += 1
            else:
                three_jumps += 1
        if i == len(input_nums):
            three_jumps += 1
            break

        diff = input_nums[i] - value
        if diff == 1:
            one_jumps += 1
        elif diff == 3:
            three_jumps += 1
        else:
            return -1

    return one_jumps * three_jumps


def solve_part_2(input_nums: List[int]) -> int:
    """
    Solve part 2 of the day
    """
    input_nums.sort()
    input_nums.insert(0, 0)
    paths_to_end: Dict[int, int] = {max(input_nums): 1}
    for value in reversed(input_nums[:-1]):
        total_paths_for_value = 0
        total_paths_for_value += paths_to_end.get(value + 1, 0)
        total_paths_for_value += paths_to_end.get(value + 2, 0)
        total_paths_for_value += paths_to_end.get(value + 3, 0)
        paths_to_end[value] = total_paths_for_value

    return paths_to_end[0]


def main():
    """
    Main method to run the day's input
    """
    with open("day10_input.txt") as problem_file:
        all_inputs = problem_file.readlines()

    all_inputs_int = [int(number) for number in all_inputs]
    part_1_answer = solve_part_1(all_inputs_int)
    print(f"Part 1: {part_1_answer}")
    print(f"Part 2: {solve_part_2(all_inputs_int)}")


if __name__ == "__main__":
    main()
