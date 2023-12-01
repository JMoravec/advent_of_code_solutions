"""Day 8 of Advent of Code 2022"""


from dataclasses import dataclass
from typing import List


@dataclass
class Tree:
    """Single tree representative"""

    value: int
    is_visible: bool = False
    viewing_score: int = 0


def create_forest(input_str: str) -> List[List[Tree]]:
    """Create a forest from an input string"""
    forrest = []
    for row in input_str.split("\n"):
        row_values = []
        for tree in row.strip():
            row_values.append(Tree(int(tree)))
        forrest.append(row_values)

    return forrest


def check_right_values(
    forrest: List[List[Tree]], x_to_check: int, y_to_check: int
) -> bool:
    """Check if the tree is visible from the right"""
    value_to_check = forrest[y_to_check][x_to_check].value
    for x in range(x_to_check + 1, len(forrest[y_to_check])):
        if forrest[y_to_check][x].value >= value_to_check:
            return False
    return True


def check_up_values(
    forrest: List[List[Tree]], x_to_check: int, y_to_check: int
) -> bool:
    """Check if the tree is visible from the top"""
    value_to_check = forrest[y_to_check][x_to_check].value
    for y in range(y_to_check):
        if forrest[y][x_to_check].value >= value_to_check:
            return False
    return True


def check_down_values(
    forrest: List[List[Tree]], x_to_check: int, y_to_check: int
) -> bool:
    """Check if the tree is visible from the bottom"""
    value_to_check = forrest[y_to_check][x_to_check].value
    for y in range(y_to_check + 1, len(forrest)):
        if forrest[y][x_to_check].value >= value_to_check:
            return False
    return True


def get_left_viewing_distance(
    forrest: List[List[Tree]], x_to_check: int, y_to_check: int
) -> int:
    """Get the viewing distance to the left of the point"""
    if x_to_check == 0:
        return 0
    value_to_check = forrest[y_to_check][x_to_check].value
    distance = 0
    for x in range(x_to_check - 1, -1, -1):
        distance += 1
        if forrest[y_to_check][x].value >= value_to_check:
            return distance
    return distance


def get_right_viewing_distance(
    forrest: List[List[Tree]], x_to_check: int, y_to_check: int
) -> int:
    """Get the viewing distance to the right of the point"""
    if x_to_check == len(forrest[y_to_check]):
        return 0
    value_to_check = forrest[y_to_check][x_to_check].value
    distance = 0
    for x in range(x_to_check + 1, len(forrest[y_to_check])):
        distance += 1
        if forrest[y_to_check][x].value >= value_to_check:
            return distance
    return distance


def get_up_viewing_distance(
    forrest: List[List[Tree]], x_to_check: int, y_to_check: int
) -> int:
    """Get the viewing distance above the point"""
    if y_to_check == 0:
        return 0
    value_to_check = forrest[y_to_check][x_to_check].value
    distance = 0
    for y in range(y_to_check - 1, -1, -1):
        distance += 1
        if forrest[y][x_to_check].value >= value_to_check:
            return distance
    return distance


def get_down_viewing_distance(
    forrest: List[List[Tree]], x_to_check: int, y_to_check: int
) -> int:
    """Get the viewing distance above the point"""
    if y_to_check == len(forrest):
        return 0
    value_to_check = forrest[y_to_check][x_to_check].value
    distance = 0
    for y in range(y_to_check + 1, len(forrest)):
        distance += 1
        if forrest[y][x_to_check].value >= value_to_check:
            return distance
    return distance


def compute_is_visible(forrest: List[List[Tree]]):
    """Cmopute the is visible values for all trees"""
    for y, row in enumerate(forrest):
        largest_left_value = -1
        for x, tree in enumerate(row):
            if x in [0, len(row) - 1]:
                tree.is_visible = True
                largest_left_value = tree.value
            if y in [0, len(forrest) - 1]:
                tree.is_visible = True
            if tree.value > largest_left_value:
                largest_left_value = tree.value
                tree.is_visible = True
            elif (
                check_down_values(forrest, x, y)
                or check_up_values(forrest, x, y)
                or check_right_values(forrest, x, y)
            ):
                tree.is_visible = True


def compute_viewing_distance(forrest: List[List[Tree]]):
    """Compute all the viewing distance values"""
    for y, row in enumerate(forrest):
        for x, tree in enumerate(row):
            tree.viewing_score = (
                get_down_viewing_distance(forrest, x, y)
                * get_up_viewing_distance(forrest, x, y)
                * get_left_viewing_distance(forrest, x, y)
                * get_right_viewing_distance(forrest, x, y)
            )


def get_number_of_visible_trees(forrest: List[List[Tree]]) -> int:
    """Get the total number of visible trees"""
    total = 0
    for row in forrest:
        for tree in row:
            if tree.is_visible:
                total += 1
    return total


def get_largest_viewing_distance(forrest: List[List[Tree]]) -> int:
    """Get the larget viewing distance for a forrest"""
    largest = 0
    for row in forrest:
        for tree in row:
            if tree.viewing_score > largest:
                largest = tree.viewing_score
    return largest


def part_1() -> int:
    """Solve part 1 of day 8"""
    with open("input.txt", "r", encoding="utf-8") as file:
        input_str = file.read()
    forrest = create_forest(input_str)
    compute_is_visible(forrest)
    return get_number_of_visible_trees(forrest)


def part_2() -> int:
    """Solve part 2 of day 8"""
    with open("input.txt", "r", encoding="utf-8") as file:
        input_str = file.read()
    forrest = create_forest(input_str)
    compute_viewing_distance(forrest)
    return get_largest_viewing_distance(forrest)


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
