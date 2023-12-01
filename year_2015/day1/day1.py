"""
Solution to Day 1 of 2015 Advent of Code
"""


def get_total_up_floors(input_str: str) -> int:
    """Get the amount of times to go up"""
    return input_str.count("(")


def get_total_down_floors(input_str: str) -> int:
    """Get the amount of times to go down"""
    return input_str.count(")")


def get_end_floor(input_str: str) -> int:
    """Get the end floor after going up and down"""
    return get_total_up_floors(input_str) - get_total_down_floors(input_str)


def parse_input() -> str:
    """Get the input string from file"""
    with open("input.txt", "r", encoding="utf-8") as file:
        return file.readline()


def get_first_basement_char(input_str: str) -> int:
    """Get the position of the first time to go into the basement"""
    current_floor = 0
    current_pos = 0
    for char in input_str:
        current_pos += 1
        if char == "(":
            current_floor += 1
        else:
            current_floor -= 1

        if current_floor < 0:
            return current_pos
    raise Exception("Never goes to basement")


def part_1() -> int:
    """
    Solve part 1 of day 1
    """
    return get_end_floor(parse_input())


def part_2() -> int:
    """Solve part 2 of day 2"""
    return get_first_basement_char(parse_input())


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
