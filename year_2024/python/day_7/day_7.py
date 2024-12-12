"""sovle day 7 of 2024"""

from typing import List, Tuple


def concat(num1: int, num2: int) -> int:
    """concat 2 nums"""
    return int(f"{num1}{num2}")


def check_line(num: int, tests: List[int], part_2: bool = False) -> bool:
    """check a single line"""
    if len(tests) == 1:
        return (num - tests[0] == 0) or (num // tests[0] == 1 and num % tests[0] == 0)

    if len(tests) == 0:
        return False

    new_nums = [(num - tests[-1], tests[:-1])]
    if num % tests[-1] == 0:
        new_nums.append((num // tests[-1], tests[:-1]))

    if part_2:
        new_concat = concat(tests[-2], tests[-1])
        new_nums.append((num - new_concat, tests[:-2]))

        if num % new_concat == 0:
            divis_num = num // new_concat
            new_nums.append((divis_num, tests[:-2]))
            if len(tests[:-2]) == 0 and divis_num == 1:
                return True

    for new_num, new_tests in new_nums:
        if sum(new_tests) == new_num:
            return True
        if len(new_tests) == 0 and new_num == 0:
            return True
        if check_line(new_num, new_tests, part_2):
            return True

    return False


def check_line_v2(
    final_num: int, current_num: int, tests: List[int], part_2: bool = False
) -> bool:
    """check a single line"""
    if len(tests) == 0:
        return final_num == current_num
    next_num = tests[0]
    next_tests = tests[1:]

    add_current_num = current_num + next_num
    mult_current_num = current_num * next_num
    concat_current_num = concat(current_num, next_num)

    run_add = True
    run_mult = True
    run_concat = part_2

    if add_current_num > final_num:
        run_add = False
    if mult_current_num > final_num:
        run_mult = False
    if concat_current_num > final_num:
        run_concat = False

    return (
        (run_add and check_line_v2(final_num, add_current_num, next_tests, part_2))
        or (run_mult and check_line_v2(final_num, mult_current_num, next_tests, part_2))
        or (
            run_concat
            and check_line_v2(final_num, concat_current_num, next_tests, part_2)
        )
    )


def get_line_from_str(input_line: str) -> Tuple[int, List[int]]:
    """process a single line str"""
    num_str, line_str = input_line.strip().split(":")
    output_line = [int(x.strip()) for x in line_str.strip().split()]
    return int(num_str), output_line


def solve_part_1(input_strs: List[str]) -> int:
    """solve part 1"""
    total = 0
    for line in input_strs:
        num, tests = get_line_from_str(line)
        if check_line_v2(num, tests[0], tests[1:]):
            total += num
    return total


def solve_part_2(input_strs: List[str]) -> int:
    """solve part 2"""
    total = 0
    for line in input_strs:
        num, tests = get_line_from_str(line)
        if check_line_v2(num, tests[0], tests[1:], True):
            total += num
    return total


def main():
    """main func"""
    with open("input_day7.txt", encoding="utf-8") as file:
        lines = file.readlines()
    print(f"part 1: {solve_part_1(lines)}")
    print(f"part 2: {solve_part_2(lines)}")


if __name__ == "__main__":
    main()
