"""
Solution for day 1
"""

from typing import Counter, List, Tuple


def main():
    """Main function for solution"""
    left_input, right_input = get_input()
    part_1_sol = solve_part_1(left_input, right_input)
    print(part_1_sol)
    part_2_sol = solve_part_2(left_input, right_input)
    print(part_2_sol)


def get_input() -> Tuple[List[int], List[int]]:
    """gets the input for the day"""
    left, right = [], []

    with open("input_day1.txt", "r", encoding="utf-8") as input_file:
        for line in input_file:
            left_int, right_int = line.strip().split("   ")
            left.append(int(left_int))
            right.append(int(right_int))

    return left, right


def solve_part_1(left_list: List[int], right_list: List[int]) -> int:
    """solve part one of the day"""
    left_list.sort()
    right_list.sort()
    zipped_list = list(zip(left_list, right_list))
    total = 0
    for left, right in zipped_list:
        total += abs(left - right)
    return total


def solve_part_2(left_list: List[int], right_list: List[int]) -> int:
    """Sovle part 2 of the day"""
    right_counter = Counter(right_list)
    total = 0
    for item in left_list:
        total += item * right_counter[item]
    return total


if __name__ == "__main__":
    main()
