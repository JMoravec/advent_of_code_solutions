"""Day 4 of 2022 Advent of Code"""


from typing import List, Set, Tuple


def convert_range_to_set(input_range: str) -> Set[int]:
    """Converts a string range to a set of numbers"""
    start, end = input_range.strip().split("-")
    return set(range(int(start), int(end) + 1))


def check_if_fully_contained(set_1: Set[int], set_2: Set[int]) -> bool:
    """Check if 1 set is a subset of another or vice versa"""
    return set_1 <= set_2 or set_2 <= set_1


def check_if_overlap(set_1: Set[int], set_2: Set[int]) -> bool:
    """Check if 1 set has any elements of set 2 or vice versa"""
    return not set_1.isdisjoint(set_2)


def parse_input() -> List[Tuple[str, str]]:
    """Parse the day's input"""
    full_list = []
    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            first_range, second_range = line.strip().split(",")
            full_list.append((first_range, second_range))
    return full_list


def part_1() -> int:
    """Solve part 1 of day 4"""
    all_ranges = parse_input()
    total = 0
    for first_range, second_range in all_ranges:
        if check_if_fully_contained(
            convert_range_to_set(first_range), convert_range_to_set(second_range)
        ):
            total += 1
    return total


def part_2() -> int:
    """Solve part 2 of day4"""
    all_ranges = parse_input()
    total = 0
    for first_range, second_range in all_ranges:
        if check_if_overlap(
            convert_range_to_set(first_range), convert_range_to_set(second_range)
        ):
            total += 1
    return total


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
