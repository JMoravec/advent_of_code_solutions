"""
Test module for day 7 2020
"""
from typing import List
import pytest
from day7.day7 import solve_part_1


@pytest.mark.parametrize(
    "input_text,expected",
    [
        (
            [
                "light red bags contain 1 bright white bag, 2 muted yellow bags.",
                "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                "bright white bags contain 1 shiny gold bag.",
                "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                "faded blue bags contain no other bags.",
                "dotted black bags contain no other bags.",
            ],
            4,
        )
    ],
)
def test_solve_part_1(input_text: List[str], expected: int):
    assert solve_part_1(input_text) == expected
