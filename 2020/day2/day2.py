"""
Day 2 of advent of code 2020
"""
from dataclasses import dataclass

@dataclass
class PasswordRule:
    """
    Helper data class to hold the password rule information
    """
    min_value: int
    max_value: int
    character: str

def parse_password_rule(input_str: str) -> PasswordRule:
    """
    Parse the rule part of an input str to a helper data class
    format necessary:
        1-3 a

    :param input_str: string value to parse
    """
    range_str, letter = input_str.split(' ')
    min_value, max_value = range_str.split('-')
    return PasswordRule(int(min_value),int(max_value),letter)

def apply_rule_part_1(password: str, rule: PasswordRule) -> bool:
    """
    Apply a rule to a password to check if it is acceptable
    """
    current_letters = 0
    for char in password:
        if char == rule.character:
            current_letters += 1

        if current_letters > rule.max_value:
            return False

    return current_letters >= rule.min_value


def apply_rule_part_2(password: str, rule: PasswordRule) -> bool:
    """
    Apply a rule to a password to check if it is acceptable
    """
    first_pos = password[rule.min_value-1] == rule.character
    second_pos = password[rule.max_value-1] == rule.character

    if first_pos and second_pos:
        return False
    if not first_pos and not second_pos:
        return False

    return True


def main():
    """
    Main method for the problem set
    """
    with open('day2_input.txt') as f:
        all_inputs = f.readlines()

    total_valid_passwords_part1 = 0
    total_valid_passwords_part2 = 0
    for input_str in all_inputs:
        rule_str, password = input_str.split(': ')
        rule = parse_password_rule(rule_str)
        if apply_rule_part_1(password, rule):
            total_valid_passwords_part1 += 1
        if apply_rule_part_2(password, rule):
            total_valid_passwords_part2 += 1

    print(f'Part 1: {total_valid_passwords_part1}')
    print(f'Part 2: {total_valid_passwords_part2}')

if __name__ == '__main__':
    main()
