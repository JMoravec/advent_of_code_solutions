"""Day 1 solution code"""

NUMS = "1234567890"


def part1(input_str: str):
    """main function for day1 part1"""
    answer = get_total_from_lines(input_str)
    print(f"Day 1, part 1: {answer}")


def part2(input_str: str):
    """main function for day1 part2"""
    answer = get_total_from_lines(input_str, True)
    print(f"Day 1, part 2: {answer}")


def get_num_from_line(line: str, replace_text: bool = False) -> int:
    """Get the number (first value and last value) from a given line"""
    left = 0
    right = len(line) - 1
    left_num = ""
    right_num = ""
    while not left_num or not right_num:
        if not left_num and line[left] in NUMS:
            left_num = line[left]
        if (
            replace_text
            and not left_num
            and (num := replace_num_text_from_line(line, left))
        ):
            left_num = num
        if not right_num and line[right] in NUMS:
            right_num = line[right]
        if (
            replace_text
            and not right_num
            and (num := replace_num_text_from_line(line, right))
        ):
            right_num = num

        left += 1
        right -= 1

    return int(f"{left_num}{right_num}")


def get_total_from_lines(lines: str, replace_text: bool = False) -> int:
    """Get the total of the artsy lines"""
    total = 0
    for line in lines.splitlines():
        total += get_num_from_line(line, replace_text)
    return total


def replace_num_text_from_line(line: str, index) -> str:
    """convert all text nums to their digit replacement"""
    i = index
    if line[i] == "o" and i + 2 < len(line) and line[i : i + 3] == "one":
        return "1"
    if line[i] == "t":
        if i + 2 < len(line) and line[i : i + 3] == "two":
            return "2"
        if i + 4 < len(line) and line[i : i + 5] == "three":
            return "3"
    if line[i] == "f" and i + 3 < len(line):
        if line[i : i + 4] == "four":
            return "4"
        if line[i : i + 4] == "five":
            return "5"
    if line[i] == "s":
        if i + 2 < len(line) and line[i : i + 3] == "six":
            return "6"
        if i + 4 < len(line) and line[i : i + 5] == "seven":
            return "7"
    if line[i] == "e" and i + 4 < len(line) and line[i : i + 5] == "eight":
        return "8"
    if line[i] == "n" and i + 3 < len(line) and line[i : i + 4] == "nine":
        return "9"

    return ""


if __name__ == "__main__":
    with open("year_2023/inputs/day1_input.txt", encoding="utf-8") as file:
        input_file = file.read()
    part1(input_file)
    part2(input_file)
