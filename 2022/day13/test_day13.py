"""Tests for day 13"""


from typing import List, Union
import pytest
from day13.day13 import (
    compare_two_values,
    parse_list_from_str,
    get_indexes_of_correct_order,
    get_sum_of_indexes,
    get_decoder_value,
    sort_inputs,
    parse_list_from_str_flat,
    CompareValues,
)

TEST_INPUT = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


@pytest.mark.parametrize(
    "left_list,right_list,expected",
    [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], CompareValues.TRUE),
        ([[1], [2, 3, 4]], [[1], 4], CompareValues.TRUE),
        ([9], [[8, 7, 6]], CompareValues.FALSE),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4], CompareValues.TRUE),
        ([7, 7, 7, 7], [7, 7, 7], CompareValues.FALSE),
        ([], [3], CompareValues.TRUE),
        ([[[]]], [[]], CompareValues.FALSE),
        (
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            CompareValues.FALSE,
        ),
    ],
)
def test_compare_to_lines(
    left_list: List[Union[int, List[int]]],
    right_list: List[Union[int, List[int]]],
    expected: CompareValues,
):
    """Test that the compare function works as expected"""
    assert compare_two_values(left_list, right_list) == expected


def test_parse_input():
    """Test that parsing the string works"""
    all_inputs = parse_list_from_str(TEST_INPUT)
    assert all_inputs[0] == ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1])
    assert all_inputs[1] == ([[1], [2, 3, 4]], [[1], 4])
    assert all_inputs[2] == ([9], [[8, 7, 6]])
    assert all_inputs[3] == ([[4, 4], 4, 4], [[4, 4], 4, 4, 4])
    assert all_inputs[4] == ([7, 7, 7, 7], [7, 7, 7])
    assert all_inputs[5] == ([], [3])
    assert all_inputs[6] == ([[[]]], [[]])
    assert all_inputs[7] == (
        [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
        [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
    )


def test_sum_of_input_indexes():
    """Test that the sum of the correct indexes is the expected value"""
    all_inputs = parse_list_from_str(TEST_INPUT)
    assert get_sum_of_indexes(get_indexes_of_correct_order(all_inputs)) == 13


def test_sorted_decoder():
    """Test that the sum of the correct indexes is the expected value"""
    all_inputs = parse_list_from_str_flat(TEST_INPUT)
    assert get_decoder_value(sort_inputs(all_inputs)) == 140
