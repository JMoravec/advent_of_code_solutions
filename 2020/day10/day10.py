"""
Day 10 of advent of code 2020
"""
from typing import List


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


def main():
    """
    Main method to run the day's input
    """
    with open("day10_input.txt") as problem_file:
        all_inputs = problem_file.readlines()

    all_inputs_int = [int(number) for number in all_inputs]
    part_1_answer = solve_part_1(all_inputs_int)
    print(f"Part 1: {part_1_answer}")
    # print(f"Part 2: {solve_part_2(part_1_answer, all_inputs_int)}")


if __name__ == "__main__":
    main()
