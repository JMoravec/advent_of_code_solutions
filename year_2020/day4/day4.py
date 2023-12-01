"""
Day 4 of advent of code 2020
"""
from typing import List


def is_passport_valid(
    input_str: str, validate_fields: bool, debug: bool = False
) -> bool:
    """
    Check if a passport is valid
    """
    valid = True
    strings_to_check = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    for test_string in strings_to_check:
        if test_string not in input_str:
            valid = False
            break

    if not valid or not validate_fields:
        return valid

    input_str = input_str.replace("\n", " ")
    fields = input_str.split(" ")
    for field in fields:
        if not field:
            continue
        if not validate_field(field):
            if debug:
                print(f"Field: {field}")
            return False

    return True


def validate_byr(value: str) -> bool:
    """
    Validate the byr field
    """
    return int(value) >= 1920 and int(value) <= 2002


def validate_iyr(value: str) -> bool:
    """
    Validate the iyr field
    """
    return int(value) >= 2010 and int(value) <= 2020


def validate_eyr(value: str) -> bool:
    """
    Validate the eyr field
    """
    return int(value) >= 2020 and int(value) <= 2030


def validate_hgt(value: str) -> bool:
    """
    Validate the hgt field
    """
    if "cm" in value:
        return int(value[0:-2]) >= 150 and int(value[0:-2]) <= 193
    if "in" in value:
        return int(value[0:-2]) >= 59 and int(value[0:-2]) <= 76
    return False


def validate_hcl(value: str) -> bool:
    """
    Validate the hcl field
    """
    if len(value) != 7 or value[0] != "#":
        return False

    try:
        int(value[1:], 16)
        return True
    except ValueError:
        return False


def validate_ecl(value: str) -> bool:
    """
    Validate the ecl field
    """
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(value: str) -> bool:
    """
    Validate the pid field
    """
    if len(value) != 9:
        return False
    try:
        int(value)
        return True
    except ValueError:
        return False


def validate_field(field: str) -> bool:
    """
    Validate a field
    """
    field_split = field.split(":")
    key = field_split[0]
    value = field_split[1]

    if key == "byr":
        return validate_byr(value)
    if key == "iyr":
        return validate_iyr(value)
    if key == "eyr":
        return validate_eyr(value)
    if key == "hgt":
        return validate_hgt(value)
    if key == "hcl":
        return validate_hcl(value)
    if key == "ecl":
        return validate_ecl(value)
    if key == "pid":
        return validate_pid(value)
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
        if is_passport_valid(passport, False):
            total += 1
    return total


def get_day2_answer(input_str: str) -> int:
    """
    Get the day 2 answer from an input string
    """
    parsed_input = parse_full_input(input_str.split("\n"))
    total = 0
    for passport in parsed_input:
        if is_passport_valid(passport, True):
            total += 1
    return total


def main():
    """
    Main method to run the day's input
    """
    full_input: str
    with open("day4_input.txt") as input_file:
        full_input = input_file.read()
    print(f"Day 1: {get_day1_answer(full_input)}")
    print(f"Day 2: {get_day2_answer(full_input)}")


if __name__ == "__main__":
    main()
