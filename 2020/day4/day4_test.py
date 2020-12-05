"""
Test module for day 4 2020
"""
from typing import List
import pytest
from day4.day4 import is_passport_valid, parse_full_input, get_day1_answer


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm",
            True,
        ),
        (
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929",
            False,
        ),
        (
            "hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm",
            True,
        ),
        ("hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in", False),
    ],
)
def test_validate_passport(test_input: str, expected: bool):
    """
    Validate that the code can determine if a passport is valid
    """
    assert is_passport_valid(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            [
                "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
                "byr:1937 iyr:2017 cid:147 hgt:183cm",
                "",
                "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
                "hcl:#cfa07d byr:1929",
                "",
                "hcl:#ae17e1 iyr:2013",
                "eyr:2024",
                "ecl:brn pid:760753108 byr:1931",
                "hgt:179cm",
                "",
                "hcl:#cfa07d eyr:2025 pid:166559648",
                "iyr:2011 ecl:brn hgt:59in",
            ],
            [
                "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm",
                "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929",
                "hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm",
                "hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in",
            ],
        )
    ],
)
def test_parse_input(test_input: List[str], expected: List[str]):
    """
    Validate that the parse input method works as expected
    """
    full_output = parse_full_input(test_input)
    for actual in full_output:
        assert actual in expected
    assert len(full_output) == len(expected)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""",
            2,
        )
    ],
)
def test_day1(test_input: str, expected: int):
    """
    Validate that the day1 solution code works as expected
    """
    assert get_day1_answer(test_input) == expected
