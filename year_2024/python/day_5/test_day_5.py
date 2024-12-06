"""tests for day 5"""

from typing import Dict, List
import pytest
from day_5.day_5 import PageRule, process_bad_line, process_line, process_rule_line


test_rules = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
]

line_test_data = [
    ([75, 47, 61, 53, 29], 61),
    ([97, 61, 53, 29, 13], 53),
    ([75, 29, 13], 29),
    ([75, 97, 47, 61, 53], 0),
    ([61, 13, 29], 0),
    ([97, 13, 75, 29, 47], 0),
]


@pytest.mark.parametrize("line,expected", line_test_data)
def test_process_line(line: List[int], expected: int):
    """test processing a single line"""
    rules: Dict[int, PageRule] = {}
    for rule in test_rules:
        process_rule_line(rule, rules)

    assert process_line(rules, line) == expected


bad_line_test_data = [
    ([75, 97, 47, 61, 53], 47),
    ([61, 13, 29], 29),
    ([97, 13, 75, 29, 47], 47),
]


@pytest.mark.parametrize("line,expected", bad_line_test_data)
def test_process_bad_line(line: List[int], expected: int):
    """test processing a single line"""
    rules: Dict[int, PageRule] = {}
    for rule in test_rules:
        process_rule_line(rule, rules)

    assert process_bad_line(rules, line) == expected
