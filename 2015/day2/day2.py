"""Solution to day 2 of 2015"""


from typing import List, Tuple


def calculate_surface_area(length: int, width: int, height: int) -> int:
    """Calculate the surface area of a box"""
    return (2 * length * width) + (2 * width * height) + (2 * height * length)


def calculate_volume(length: int, width: int, height: int) -> int:
    """Calculate the volume of a box"""
    return length * width * height


def calculate_shortest_distance(lwh: Tuple[int, int, int]) -> int:
    """Calculate the shortest distance for the sides"""
    sorted_lengths = sorted(lwh)
    return (2 * sorted_lengths[0]) + (2 * sorted_lengths[1])


def calculate_wrapping_paper(lwh: Tuple[int, int, int]) -> int:
    """Calculate the required amount of wrapping paper given a lwh box"""
    length, width, height = lwh[0], lwh[1], lwh[2]
    sides = (length * width), (width * height), (height * length)
    return 2 * sum(sides) + min(sides)


def calculate_ribbon_needed(lwh: Tuple[int, int, int]) -> int:
    """Calculate the required amount of ribbon needed for a box"""
    return calculate_volume(*lwh) + calculate_shortest_distance(lwh)


def parse_input() -> List[Tuple[int, int, int]]:
    """Parse the day's input from file"""
    output_list = []
    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            output_list.append(tuple(int(item.strip()) for item in line.split("x")))
    return output_list


def part_1() -> int:
    """Solve part 1 of day 2"""
    total = 0
    for item in parse_input():
        total += calculate_wrapping_paper(item)
    return total


def part_2() -> int:
    """Solve part 2 of day 2"""
    total = 0
    for item in parse_input():
        total += calculate_ribbon_needed(item)
    return total


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
