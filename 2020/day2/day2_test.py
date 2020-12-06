"""
Test module for day 2 2020
"""
import pytest
from day2.day2 import (
    PasswordRule,
    parse_password_rule,
    apply_rule_part_1,
    apply_rule_part_2,
)


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("1-3 a", PasswordRule(1, 3, "a")),
        ("1-3 b", PasswordRule(1, 3, "b")),
        ("2-9 c", PasswordRule(2, 9, "c")),
    ],
)
def test_parse_password_rule(input_str: str, expected: PasswordRule):
    """
    Validate that the code can parse the rule correctly
    """
    actual = parse_password_rule(input_str)
    assert actual == expected


@pytest.mark.parametrize(
    "password,rule,expected",
    [
        ("abcde", PasswordRule(1, 3, "a"), True),
        ("cdefg", PasswordRule(1, 3, "b"), False),
        ("ccccccccc", PasswordRule(2, 9, "c"), True),
    ],
)
def test_apply_rule_part1(password: str, rule: PasswordRule, expected: bool):
    """
    Validate that the given rule will correctly check a given string
    """
    assert apply_rule_part_1(password, rule) == expected


@pytest.mark.parametrize(
    "password,rule,expected",
    [
        ("abcde", PasswordRule(1, 3, "a"), True),
        ("cdefg", PasswordRule(1, 3, "b"), False),
        ("ccccccccc", PasswordRule(2, 9, "c"), False),
    ],
)
def test_apply_rule_part2(password: str, rule: PasswordRule, expected: bool):
    """
    Validate that the given rule will correctly check a given string
    """
    assert apply_rule_part_2(password, rule) == expected
