"""
Test module for day 4 2020
"""
from typing import List
import pytest
from year_2020.day4.day4 import (
    is_passport_valid,
    parse_full_input,
    get_day1_answer,
    validate_byr,
    validate_hgt,
    validate_hcl,
    validate_ecl,
    validate_pid,
)


@pytest.mark.parametrize("test,expected", [("2002", True), ("2003", False)])
def test_validate_byr(test: str, expected: bool):
    assert validate_byr(test) == expected


@pytest.mark.parametrize(
    "test,expected", [("60in", True), ("190cm", True), ("190in", False), ("190", False)]
)
def test_validate_hgt(test: str, expected: bool):
    assert validate_hgt(test) == expected


@pytest.mark.parametrize(
    "test,expected",
    [
        ("#123abc", True),
        ("#123abz", False),
        ("123abc", False),
    ],
)
def test_validate_hcl(test: str, expected: bool):
    assert validate_hcl(test) == expected


@pytest.mark.parametrize(
    "test,expected",
    [
        ("brn", True),
        ("wat", False),
    ],
)
def test_validate_ecl(test: str, expected: bool):
    assert validate_ecl(test) == expected


@pytest.mark.parametrize(
    "test,expected",
    [
        ("000000001", True),
        ("0123456789", False),
    ],
)
def test_validate_pid(test: str, expected: bool):
    assert validate_pid(test) == expected


@pytest.mark.parametrize(
    "test_input,validate_fields,expected",
    [
        (
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm",
            False,
            True,
        ),
        (
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929",
            False,
            False,
        ),
        (
            "hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm",
            False,
            True,
        ),
        ("hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in", False, False),
        (
            "eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
            True,
            False,
        ),
        (
            "iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946",
            True,
            False,
        ),
        (
            "hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
            True,
            False,
        ),
        (
            "hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007",
            True,
            False,
        ),
        (
            "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\n hcl:#623a2f",
            True,
            True,
        ),
        (
            "eyr:2029 ecl:blu cid:129 byr:1989\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
            True,
            True,
        ),
        (
            "hcl:#888785\nhgt:164cm byr:2001 iyr:2015 cid:88\npid:545766238 ecl:hzl\neyr:2022",
            True,
            True,
        ),
        (
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
            True,
            True,
        ),
    ],
)
def test_validate_passport(test_input: str, validate_fields: bool, expected: bool):
    """
    Validate that the code can determine if a passport is valid
    """
    assert is_passport_valid(test_input, validate_fields) == expected


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
