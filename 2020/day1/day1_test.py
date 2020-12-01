"""
Test module for day 1
"""
from typing import List, Tuple
import pytest
from day1.day1 import check_2020, get_sums_from_list, get_day_1_answer


@pytest.mark.parametrize('value_1,value_2,expected',
    [(1721,299,True), (1721,1456,False), (299,675,False)])
def test_check_2020(value_1: int, value_2: int, expected: bool):
    """
    Test the check_2020 method
    """
    assert check_2020(value_1, value_2) == expected

@pytest.mark.parametrize('values,expected', [([1721,979,366,299,675,1456],(1721,299))])
def test_get_sums_from_list(values: List[int], expected: Tuple[int, int]):
    """
    Test the sums method
    """
    answer_1, answer_2 = get_sums_from_list(values)
    assert answer_1 in expected
    assert answer_2 in expected

@pytest.mark.parametrize('input_str,expected', [('1721\n979\n366\n299\n675\n1456',514579)])
def test_get_answer_from_input(input_str: str, expected: int):
    """
    Validate that the code can generate the day1 answer from an example input
    """
    assert get_day_1_answer(input_str) == expected
