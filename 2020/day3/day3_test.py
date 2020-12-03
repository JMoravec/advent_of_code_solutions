"""
Test module for day 3 2020
"""
import pytest
from day3.day3 import slide_down_slope, Point

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
    test_slide = Point(0,0,len(test_input), 3, 1)
    assert slide_down_slope(test_input, test_slide) == 7

def test_part_2():
    test_slide_1 = Point(0,0,len(test_input), 1, 1)
    trees_1 = slide_down_slope(test_input, test_slide_1)
    test_slide_2 = Point(0,0,len(test_input), 3, 1)
    trees_2 = slide_down_slope(test_input, test_slide_2)
    test_slide_3 = Point(0,0,len(test_input), 5, 1)
    trees_3 = slide_down_slope(test_input, test_slide_3)
    test_slide_4 = Point(0,0,len(test_input), 7, 1)
    trees_4 = slide_down_slope(test_input, test_slide_4)
    test_slide_5 = Point(0,0,len(test_input), 1, 2)
    trees_5 = slide_down_slope(test_input, test_slide_5)

    assert trees_1 * trees_2 * trees_3 * trees_4 * trees_5 == 336
