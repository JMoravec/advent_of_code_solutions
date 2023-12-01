"""Day 3 of Advent of Code 2022"""


from typing import Set, Tuple


def get_rucksacks(full_string: str) -> Tuple[str, str]:
    """Get the two rucksack strings from the main string"""
    middle = len(full_string) // 2
    return (full_string[:middle], full_string[middle:])


def get_set_for_string(rucksack: str) -> Set[str]:
    """Convert a rucksack to a set"""
    return set(list(rucksack))


def get_common_letter(rucksack_1: Set[str], rucksack_2: Set[str]) -> str:
    """Get the common letter between the two rucksacks"""
    for letter in rucksack_1:
        if letter in rucksack_2:
            return letter
    return ""


def get_common_badge(ruck_1: Set[str], ruck_2: Set[str], ruck_3: Set[str]) -> str:
    """Get the common badge letter for 3 rucksacks"""
    return ruck_1.intersection(ruck_2, ruck_3).pop()


def get_priority(letter: str) -> int:
    """Get the priority points of the letter"""
    current_point = "abcdefghijklmnopqrstuvwxyz".index(letter.lower()) + 1
    if letter.isupper():
        return current_point + 26
    return current_point


def part_1() -> int:
    """Solve part 1 of day 3"""
    total_points = 0
    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            ruck_1, ruck_2 = get_rucksacks(line)
            total_points += get_priority(
                get_common_letter(
                    get_set_for_string(ruck_1), get_set_for_string(ruck_2)
                )
            )
    return total_points


def part_2() -> int:
    """Solve part 2 of day 3"""
    total_points = 0
    with open("input.txt", "r", encoding="utf-8") as file:
        while True:
            first_line = file.readline().strip()
            if first_line == "":
                break
            second_line = file.readline().strip()
            third_line = file.readline().strip()
            total_points += get_priority(
                get_common_badge(
                    get_set_for_string(first_line),
                    get_set_for_string(second_line),
                    get_set_for_string(third_line),
                )
            )
    return total_points


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
