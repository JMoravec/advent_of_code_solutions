"""
Test module for day 1
"""
from typing import List, Tuple
import pytest
from day1.day1 import check_2020, get_sums_from_list, get_day_1_answer, convert_input_str_to_int,get_day_2_answer


@pytest.mark.parametrize('value_tuple,expected',
    [((1721,299),True), ((1721,1456),False), ((299,675),False),
        ((979,366,675),True),((1,2,3),False)])
def test_check_2020(value_tuple: tuple, expected: bool):
    """
    Test the check_2020 method
    """
    assert check_2020(value_tuple) == expected

@pytest.mark.parametrize('values,combos,expected', [
    ([1721,979,366,299,675,1456],2,(1721,299)),
    ([1721,979,366,299,675,1456],3,(979,366,675))
    ])
def test_get_sums_from_list(values: List[int], combos: int, expected: tuple):
    """
    Test the sums method
    """
    answer_tuple = get_sums_from_list(values, combos)
    for answer_value in answer_tuple:
        assert answer_value in expected

@pytest.mark.parametrize('input_str,expected', [('1721\n979\n366\n299\n675\n1456',514579)])
def test_get_answer_1_from_input(input_str: str, expected: int):
    """
    Validate that the code can generate the day1 answer from an example input
    """
    values_input = convert_input_str_to_int(input_str)
    assert get_day_1_answer(values_input) == expected

@pytest.mark.parametrize('input_str,expected', [('1721\n979\n366\n299\n675\n1456',241861950)])
def test_get_answer_2_from_input(input_str: str, expected: int):
    """
    Validate that the code can generate the day1 answer from an example input
    """
    values_input = convert_input_str_to_int(input_str)
    assert get_day_2_answer(values_input) == expected
