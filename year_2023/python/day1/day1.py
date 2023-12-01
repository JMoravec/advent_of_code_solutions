"""Day 1 solution code"""

NUMS = "1234567890"


def part1():
    """main function for day1 part1"""


def get_num_from_line(line: str) -> int:
    """Get the number (first value and last value) from a given line"""
    left = 0
    right = len(line) - 1
    left_num = ""
    right_num = ""
    while not left_num and not right_num:
        if not left_num and line[left] in NUMS:
            left_num = line[left]
        if not right_num and line[right] in NUMS:
            right_num = line[right]

        left += 1
        right -= 1

    return int(left + right)


if __name__ == "__main__":
    part1()
