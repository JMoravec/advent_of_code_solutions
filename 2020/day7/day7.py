"""
Day 7 of advent of code 2020
"""
from typing import NamedTuple, List, Tuple, Dict
import re


class BagAmount(NamedTuple):  # pylint: disable=inherit-non-class
    """
    Helper tuple to hold an amount of bags
    """

    amount: int
    color: str


def parse_str_to_bag_amount(input_str: str) -> List["BagAmount"]:
    """
    Parse a string to the amount
    """
    if "contain no other bags" in input_str:
        return []
    regex = re.compile("(\\d) (\\w+ \\w+) bag[s]?")
    all_matched = regex.findall(input_str)
    if not all_matched:
        return []

    return_list = []
    for amount, bag_color in all_matched:
        return_list.append(BagAmount(amount, bag_color))
    return return_list


def process_rule(input_str: str) -> Tuple[str, List[BagAmount]]:
    """
    Process a single rule to color and a list of amounts of other bags
    """
    regex = re.compile("(\\w+ \\w+) bags")
    main_color = regex.findall(input_str)[0]
    return main_color, parse_str_to_bag_amount(input_str)


def check_color(
    all_colors: Dict[str, List[BagAmount]], top_level_color: str, color_to_find: str
) -> int:
    """
    Check to see if a color has a certain bag
    """
    contains = all_colors[top_level_color]
    if not contains:
        return 0
    if color_to_find in [x.color for x in contains]:
        return 1
    for new_color in contains:
        if check_color(all_colors, new_color.color, color_to_find) == 1:
            return 1
    return 0


def how_many_bags_it_contains(
    all_colors: Dict[str, List[BagAmount]], bag_to_search: str
) -> int:
    """
    Count how many options a bag has to be in
    """
    total = 0
    for test_color in all_colors.keys():
        if check_color(all_colors, test_color, bag_to_search) == 1:
            total += 1
    return total


def solve_part_1(input_text: List[str]) -> int:
    """
    Solve part 1 of the day's input
    """
    all_colors: Dict[str, List[BagAmount]] = {}
    for rule in input_text:
        color, bags = process_rule(rule)
        if color not in all_colors.keys():
            all_colors[color] = bags
        else:
            all_colors[color].extend(bags)
    return how_many_bags_it_contains(all_colors, "shiny gold")


def main():
    """
    Main method to run the day's input
    """
    with open("day7_input.txt") as problem_file:
        all_inputs = problem_file.readlines()
    print(f"Part 1: {solve_part_1(all_inputs)}")
    # print(f"Part 2: {solve_part_2(all_inputs)}")


if __name__ == "__main__":
    main()
