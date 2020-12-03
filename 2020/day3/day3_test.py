"""
Test module for day 3 2020
"""
import pytest
from day3.day3 import slide_down_slope

test_input = ['..##.......',
'#...#...#..',
'.#....#..#.',
'..#.#...#.#',
'.#...##..#.',
'..#.##.....',
'.#.#.#....#',
'.#........#',
'#.##...#...',
'#...##....#',
'.#..#...#.#',
]

def test_part_1():
    assert slide_down_slope(test_input) == 7
