"""Solution for day6 of year 2023"""

# distance = x (time - x)
# want ->
# distance < x (time - x)
# 0 < x (time - x) - distance
# 0 < -x^2 + x*time - distance
# for 0 = bla:
# x = (-time +- sqrt(time^2 - 4*distance))/-2
# eg.:
# -7 + sqrt(49 + 36)

import math
from typing import Tuple


def get_limits(time: int, distance: int) -> Tuple[float, float]:
    """Get the limits where the forumla works"""
    first = (-time + math.sqrt(time**2 - 4 * distance)) / -2
    second = (-time - math.sqrt(time**2 - 4 * distance)) / -2
    return (min(first, second), max(first, second))


def get_amount_of_solutions(time: int, distance: int) -> int:
    """Get the amount of solutions for a given time/distance"""
    lower, higher = get_limits(time, distance)
    if lower.is_integer():
        lower += 1
    if higher.is_integer():
        higher -= 1
    return math.floor(higher) - math.ceil(lower) + 1


def solve_part_1(input_str: str) -> int:
    """Solve part 1 of day 6"""
    lines = input_str.splitlines()
    times = lines[0].split("Time:")[1].strip().split()
    distances = lines[1].split("Distance:")[1].strip().split()
    assert len(times) == len(distances)
    answer = 1

    for i, time in enumerate(times):
        answer *= get_amount_of_solutions(int(time), int(distances[i]))
    return answer


def solve_part_2(input_str: str) -> int:
    """Solve part 2 of day 6"""
    lines = input_str.splitlines()
    time = "".join(lines[0].split("Time:")[1].strip().split())
    distance = "".join(lines[1].split("Distance:")[1].strip().split())
    return get_amount_of_solutions(int(time), int(distance))


if __name__ == "__main__":
    with open("year_2023/inputs/day6_input.txt", encoding="utf-8") as file:
        test_input = file.read()

    print(f"Day 6 part 1: {solve_part_1(test_input)}")
    print(f"Day 6 part 2: {solve_part_2(test_input)}")
