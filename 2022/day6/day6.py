"""Day 6 of Advent of Cod 2022"""


def find_signal(input_str: str, window_size: int) -> int:
    """Find the start of the signal given a string"""
    for i in range(len(input_str)):
        window = set(input_str[i : i + window_size])
        if len(window) == window_size:
            return i + window_size
    raise Exception("No signal")


def part_1() -> int:
    """Solve part 1 of day 6"""
    with open("input.txt", "r", encoding="utf-8") as file:
        line = file.read()
    return find_signal(line, 4)


def part_2() -> int:
    """Solve part 2 of day 6"""
    with open("input.txt", "r", encoding="utf-8") as file:
        line = file.read()
    return find_signal(line, 14)


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
