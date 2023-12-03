"""Solution for day 3 of 2023"""
from collections import defaultdict
from typing import Dict, List, Set


def find_part_nums(input_map: List[str]) -> int:
    """Find the part nums in a given input map"""
    nums = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    all_part_nums = []
    symbols = defaultdict(set)
    for y, row in enumerate(input_map):
        current_num = ""
        stripped_row = row.strip()
        for x, cell in enumerate(stripped_row):
            if cell in nums:
                current_num = f"{current_num}{cell}"
            elif current_num:
                all_part_nums.append((current_num, x, y))
                current_num = ""
            if cell != "." and cell not in nums:
                symbols[y].add(x)
        if current_num:
            all_part_nums.append((current_num, len(stripped_row), y))
    part_nums = []
    for test_num, x, y in all_part_nums:
        x_s = set(range(x - len(test_num) - 1, x + 1))
        y_s = list(range(y - 1, y + 2))
        for test_y in y_s:
            if len(symbols[test_y].intersection(x_s)) != 0:
                part_nums.append(int(test_num))
                break

    return sum(part_nums)


def find_part_nums_part2(input_map: List[str]) -> int:
    """Find the part nums in a given input map"""
    nums = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    all_part_nums = []
    symbols: Dict[int, Dict[int, Set[int]]] = {}
    for y, row in enumerate(input_map):
        current_num = ""
        stripped_row = row.strip()
        for x, cell in enumerate(stripped_row):
            if cell in nums:
                current_num = f"{current_num}{cell}"
            elif current_num:
                all_part_nums.append((current_num, x, y))
                current_num = ""
            if cell == "*":
                if y in symbols:
                    symbols[y][x] = set()
                else:
                    symbols[y] = {x: set()}
        if current_num:
            all_part_nums.append((current_num, len(stripped_row), y))
    for test_num, x, y in all_part_nums:
        x_s = set(range(x - len(test_num) - 1, x + 1))
        y_s = list(range(y - 1, y + 2))
        for test_y in y_s:
            for test_x in x_s:
                if test_y in symbols and test_x in symbols[test_y]:
                    symbols[test_y][test_x].add(int(test_num))

    total = 0
    for test_symbol in symbols.values():
        for test_x_symbole in test_symbol.values():
            if len(test_x_symbole) == 2:
                total += test_x_symbole.pop() * test_x_symbole.pop()

    return total


if __name__ == "__main__":
    with open("year_2023/inputs/day3_input.txt", encoding="utf-8") as file:
        lines = file.readlines()
    print(f"Day 3 part 1: {find_part_nums(lines)}")
    print(f"Day 3 part 2: {find_part_nums_part2(lines)}")
