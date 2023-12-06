"""Tests for day 5 of 2023"""

import pytest
from year_2023.python.day5.day5 import Map, solve_part_1, solve_part_2


TEST_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


@pytest.mark.parametrize(
    "input_str,exp_source,exp_dest",
    [
        ("seed-to-soil map:", "seed", "soil"),
        ("soil-to-fertilizer map:", "soil", "fertilizer"),
        ("fertilizer-to-water map:", "fertilizer", "water"),
        ("water-to-light map:", "water", "light"),
        ("light-to-temperature map:", "light", "temperature"),
        ("temperature-to-humidity map:", "temperature", "humidity"),
        ("humidity-to-location map:", "humidity", "location"),
    ],
)
def test_map_creation(input_str: str, exp_source: str, exp_dest: str):
    """Validate that creating the mapping object works as expected"""
    mapping = Map.create_from_string(input_str)
    assert mapping.source == exp_source
    assert mapping.destination == exp_dest


def test_seed_to_soil():
    """Validate that getting the seed number for the inputs works correctly"""
    mapping = Map.create_from_string("seed-to-soil map:")
    input_lines = "50 98 2\n52 50 48"
    for input_line in input_lines.splitlines():
        mapping.add_map_line(input_line)

    assert mapping.get_value(79) == 81
    assert mapping.get_value(14) == 14
    assert mapping.get_value(55) == 57
    assert mapping.get_value(13) == 13


def test_part_1():
    """Validate part1 solution works with test input"""
    assert solve_part_1(TEST_INPUT) == 35


def test_part_2():
    """Validate part 2 solution works with test input"""
    assert solve_part_2(TEST_INPUT) == 46
