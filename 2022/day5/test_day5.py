"""Tests for day 4"""

from typing import List, Tuple
import pytest
from day5.day5 import (
    parse_stacks,
    move_item_from_stack,
    move_n_from_stack,
    get_move_from_str,
    parse_input,
    get_final_state,
    get_final_string,
    move_n_from_stack_at_same_time,
)


def test_parse_stacks():
    """Test that parsing the stacks works as expected"""
    stacks = """    [D]     
[N] [C] 
[Z] [M] [P] 
 1   2   3
 """
    expected = [["Z", "N"], ["M", "C", "D"], ["P"]]
    all_stacks = parse_stacks(stacks)
    assert all_stacks == expected


@pytest.mark.parametrize(
    "move_from,move_to,first_expected_state,other_expected_state",
    [
        (["M", "C", "D"], ["Z", "N"], ["M", "C"], ["Z", "N", "D"]),
        (["Z", "N", "D"], ["P"], ["Z", "N"], ["P", "D"]),
    ],
)
def test_move_item(
    move_from: List[str],
    move_to: List[str],
    first_expected_state: List[str],
    other_expected_state: List[str],
):
    """Test moving items from stack to stack"""
    move_item_from_stack(move_from, move_to)
    assert move_from == first_expected_state
    assert move_to == other_expected_state


@pytest.mark.parametrize(
    "move_from,move_to,times,first_expected_state,other_expected_state",
    [
        (["M", "C", "D"], ["Z", "N"], 1, ["M", "C"], ["Z", "N", "D"]),
        (["Z", "N", "D"], ["P"], 3, [], ["P", "D", "N", "Z"]),
        (["M", "C"], [], 2, [], ["C", "M"]),
    ],
)
def test_move_n_item(
    move_from: List[str],
    move_to: List[str],
    times: int,
    first_expected_state: List[str],
    other_expected_state: List[str],
):
    """Test moving items from stack to stack"""
    move_n_from_stack(times, move_from, move_to)
    assert move_from == first_expected_state
    assert move_to == other_expected_state


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("move 1 from 2 to 1", (1, 2, 1)),
        ("move 3 from 1 to 3", (3, 1, 3)),
        ("move 2 from 2 to 1", (2, 2, 1)),
        ("move 1 from 1 to 2", (1, 1, 2)),
    ],
)
def test_get_move_string(input_str: str, expected: Tuple[int, int, int]):
    """Test parsing the input move command"""
    assert get_move_from_str(input_str) == expected


@pytest.mark.parametrize(
    "move_from,move_to,times,first_expected_state,other_expected_state",
    [
        (["M", "C", "D"], ["Z", "N"], 1, ["M", "C"], ["Z", "N", "D"]),
        (["Z", "N", "D"], ["P"], 3, [], ["P", "Z", "N", "D"]),
        (["M", "C"], [], 2, [], ["M", "C"]),
    ],
)
def test_move_n_at_a_time(
    move_from: List[str],
    move_to: List[str],
    times: int,
    first_expected_state: List[str],
    other_expected_state: List[str],
):
    """Test that the move function works for the group"""
    move_n_from_stack_at_same_time(times, move_from, move_to)
    assert move_from == first_expected_state
    assert move_to == other_expected_state


FULL_INPUT_STR = """    [D]     
[N] [C]     
[Z] [M] [P] 
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_parse_input():
    """test that parsing the input works as expected"""
    expected_stack = [["Z", "N"], ["M", "C", "D"], ["P"]]
    expected_moves = [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
    stack, moves = parse_input(FULL_INPUT_STR)
    assert stack == expected_stack
    assert moves == expected_moves


def test_full_state():
    """test that parsing the input works as expected"""
    expected_ending_state = [["C"], ["M"], ["P", "D", "N", "Z"]]
    stack = get_final_state(*parse_input(FULL_INPUT_STR), False)
    assert stack == expected_ending_state


def test_get_final_stack_string():
    """Test getting the final letter of the input"""
    expected_string = "CMZ"
    stack = get_final_state(*parse_input(FULL_INPUT_STR), False)
    assert get_final_string(stack) == expected_string


def test_full_state_part_2():
    """test that parsing the input works as expected"""
    expected_ending_state = [["M"], ["C"], ["P", "Z", "N", "D"]]
    stack = get_final_state(*parse_input(FULL_INPUT_STR), True)
    assert stack == expected_ending_state


def test_get_final_stack_string_part_2():
    """Test getting the final letter of the input"""
    expected_string = "MCD"
    stack = get_final_state(*parse_input(FULL_INPUT_STR), True)
    assert get_final_string(stack) == expected_string
