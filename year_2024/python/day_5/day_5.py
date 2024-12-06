"""Solution for day 5"""

from functools import cmp_to_key
from typing import Dict, List, Tuple


class PageRule:
    """helper class to represent a single page rule"""

    num: int
    pages_before: List[int]
    pages_after: List[int]

    def __init__(self, num: int):
        self.num = num
        self.pages_before = []
        self.pages_after = []

    def __eq__(self, another):
        return self.num == another.num

    def __hash__(self):
        return hash(self.num)


def main():
    """solves day 5"""
    rules, lines = get_input()
    print(f"Part 1: {solve_part_1(rules, lines)}")
    print(f"Part 2: {solve_part_2(rules, lines)}")


def solve_part_1(rules: Dict[int, PageRule], lines: List[List[int]]) -> int:
    """solves part 1"""
    total = 0
    for line in lines:
        total += process_line(rules, line)
    return total


def process_bad_line(rules: Dict[int, PageRule], line: List[int]) -> int:
    """fix a bad line to a correctly sorted one"""

    def compare_rule(first: int, second: int) -> int:
        """compare two rules"""
        rule = rules[first]
        if second in rule.pages_before:
            return 1
        return -1

    new_line = sorted(line, key=cmp_to_key(compare_rule))
    return new_line[(len(new_line) - 1) // 2]


def solve_part_2(rules: Dict[int, PageRule], lines: List[List[int]]) -> int:
    """solves part 2"""
    total = 0
    for line in lines:
        if process_line(rules, line) == 0:
            total += process_bad_line(rules, line)
    return total


def process_line(rules: Dict[int, PageRule], line: List[int]) -> int:
    """processes a single line for the middle num"""
    for i, test_num in enumerate(line):
        rule = rules[test_num]
        for j, second_test in enumerate(line):
            if i == j:
                continue
            if i < j and second_test in rule.pages_before:
                return 0
            if i > j and second_test in rule.pages_after:
                return 0
    return line[(len(line) - 1) // 2]


def process_rule_line(current_line: str, page_dict: Dict[int, PageRule]):
    """add a rule from a line"""
    first_num_str, second_num_str = current_line.strip().split("|")
    first_num = int(first_num_str)
    second_num = int(second_num_str)
    if first_num not in page_dict:
        rule = PageRule(first_num)
        page_dict[first_num] = rule
    page_dict[first_num].pages_after.append(second_num)

    if second_num not in page_dict:
        rule = PageRule(second_num)
        page_dict[second_num] = rule
    page_dict[second_num].pages_before.append(first_num)


def get_input() -> Tuple[Dict[int, PageRule], List[List[int]]]:
    """get the days input file"""
    page_dict: Dict[int, PageRule] = {}
    produce_lines: List[List[int]] = []
    with open("input_day5.txt", encoding="utf-8") as file:
        for current_line in file:
            if "|" in current_line:
                process_rule_line(current_line, page_dict)
            if "," in current_line:
                produce_lines.append([int(x) for x in current_line.strip().split(",")])

    return page_dict, produce_lines


if __name__ == "__main__":
    main()
