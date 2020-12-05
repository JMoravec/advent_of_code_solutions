"""
Day 4 of advent of code 2020
"""
from typing import List


def is_passport_valid(input_str: str) -> bool:
    """
    Check if a passport is valid
    """
    strings_to_check = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    for test_string in strings_to_check:
        if test_string not in input_str:
            return False
    return True


def parse_full_input(input_strings: List[str]) -> List[str]:
    """
    Get the passports from the full import
    """
    parsed_input: List[str] = []
    current_input = ""
    for new_input in input_strings:
        if not new_input:
            parsed_input.append(current_input)
            current_input = ""
        elif current_input:
            current_input = f"{current_input}\n{new_input}"
        else:
            current_input = new_input
    parsed_input.append(current_input)
    return parsed_input


def get_day1_answer(input_str: str) -> int:
    """
    Get the day 1 answer from an input string
    """
    parsed_input = parse_full_input(input_str.split("\n"))
    total = 0
    for passport in parsed_input:
        if is_passport_valid(passport):
            total += 1
    return total


def main():
    """
    Main method to run the day's input
    """
    full_input: str
    with open("day4_input.txt") as f:
        full_input = f.read()
    print(f"Day 1: {get_day1_answer(full_input)}")


if __name__ == "__main__":
    main()
