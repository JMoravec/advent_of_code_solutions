"""Tests for day 11"""
from typing import List
import pytest
from day11.day11 import (
    Monkey,
    parse_monkeys_from_string,
    run_round,
    run_rounds,
    get_most_active_inspected,
)


TEST_MONKEY_INPUT = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


@pytest.mark.parametrize(
    "input_str,expected_items,expected_op_result,expected_divisible,expected_true,"
    "expected_false",
    [
        (
            "Starting items: 79, 98\nOperation: new = old * 19\nTest: divisible by 23"
            "\nIf true: throw to monkey 2\nIf false: throw to monkey 3",
            [79, 98],
            38,
            23,
            2,
            3,
        ),
        (
            "  Starting items: 54, 65, 75, 74\nOperation: new = old + 6\nTest: "
            "divisible by 19\nIf true: throw to monkey 2\nIf false: throw to monkey 0",
            [54, 65, 75, 74],
            8,
            19,
            2,
            0,
        ),
        (
            "  Starting items: 79, 60, 97\nOperation: new = old * old\nTest: "
            "divisible by 13\nIf true: throw to monkey 1\nIf false: throw to monkey 3",
            [79, 60, 97],
            4,
            13,
            1,
            3,
        ),
        (
            "  Starting items: 74\nOperation: new = old + 3\nTest: divisible by 17"
            "\nIf true: throw to monkey 0\nIf false: throw to monkey 1",
            [74],
            5,
            17,
            0,
            1,
        ),
    ],
)
def test_create_monkey(
    input_str: str,
    expected_items: List[int],
    expected_op_result: int,
    expected_divisible: int,
    expected_true: int,
    expected_false: int,
):
    """Test the creation of monkey objects"""
    test_monkey = Monkey.create_from_string(input_str)
    assert test_monkey.items == expected_items
    assert test_monkey.operation(2) == expected_op_result
    assert test_monkey.test_divisible == expected_divisible
    assert test_monkey.true_monkey == expected_true
    assert test_monkey.false_monkey == expected_false


def test_single_round():
    """Test a single round with the test monkeys"""
    monkeys = parse_monkeys_from_string(TEST_MONKEY_INPUT)
    run_round(monkeys)
    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].items == []
    assert monkeys[3].items == []


@pytest.mark.parametrize(
    "rounds,monkey_0,monkey_1,monkey_2,monkey_3",
    [
        (1, [20, 23, 27, 26], [2080, 25, 167, 207, 401, 1046], [], []),
        (2, [695, 10, 71, 135, 350], [43, 49, 58, 55, 362], [], []),
        (3, [16, 18, 21, 20, 122], [1468, 22, 150, 286, 739], [], []),
        (4, [491, 9, 52, 97, 248, 34], [39, 45, 43, 258], [], []),
        (5, [15, 17, 16, 88, 1037], [20, 110, 205, 524, 72], [], []),
        (6, [8, 70, 176, 26, 34], [481, 32, 36, 186, 2190], [], []),
        (7, [162, 12, 14, 64, 732, 17], [148, 372, 55, 72], [], []),
        (8, [51, 126, 20, 26, 136], [343, 26, 30, 1546, 36], [], []),
        (9, [116, 10, 12, 517, 14], [108, 267, 43, 55, 288], [], []),
        (10, [91, 16, 20, 98], [481, 245, 22, 26, 1092, 30], [], []),
        (15, [83, 44, 8, 184, 9, 20, 26, 102], [110, 36], [], []),
        (20, [10, 12, 14, 26, 34], [245, 93, 53, 199, 115], [], []),
    ],
)
def test_multiple_rounds(
    rounds: int,
    monkey_0: List[int],
    monkey_1: List[int],
    monkey_2: List[int],
    monkey_3: List[int],
):
    """Test running multiple rounds of the input"""
    monkeys = parse_monkeys_from_string(TEST_MONKEY_INPUT)
    run_rounds(rounds, monkeys)
    assert monkeys[0].items == monkey_0
    assert monkeys[1].items == monkey_1
    assert monkeys[2].items == monkey_2
    assert monkeys[3].items == monkey_3


def test_inspected_total_counts():
    """Validate that the total inspected itmes is correct"""
    monkeys = parse_monkeys_from_string(TEST_MONKEY_INPUT)
    run_rounds(20, monkeys)
    assert monkeys[0].times_inspected == 101
    assert monkeys[1].times_inspected == 95
    assert monkeys[2].times_inspected == 7
    assert monkeys[3].times_inspected == 105


def test_inspected_total():
    """Validate that the total inspected itmes is correct"""
    monkeys = parse_monkeys_from_string(TEST_MONKEY_INPUT)
    run_rounds(20, monkeys)
    assert get_most_active_inspected(monkeys) == 10605


@pytest.mark.parametrize(
    "rounds,monkey_0,monkey_1,monkey_2,monkey_3",
    [
        (1, 2, 4, 3, 6),
        (20, 99, 97, 8, 103),
        (1000, 5204, 4792, 199, 5192),
        (2000, 10419, 9577, 392, 10391),
        (3000, 15638, 14358, 587, 15593),
        (4000, 20858, 19138, 780, 20797),
        (5000, 26075, 23921, 974, 26000),
        (6000, 31294, 28702, 1165, 31204),
        (7000, 36508, 33488, 1360, 36400),
        (8000, 41728, 38268, 1553, 41606),
        (9000, 46945, 43051, 1746, 46807),
        (10000, 52166, 47830, 1938, 52013),
    ],
)
def test_inspected_total_counts_no_worry(
    rounds: int, monkey_0: int, monkey_1: int, monkey_2: int, monkey_3: int
):
    """Validate that the total inspected itmes is correct"""
    monkeys = parse_monkeys_from_string(TEST_MONKEY_INPUT, True, 23 * 19 * 13 * 17)
    run_rounds(rounds, monkeys)
    assert monkeys[0].times_inspected == monkey_0
    assert monkeys[1].times_inspected == monkey_1
    assert monkeys[2].times_inspected == monkey_2
    assert monkeys[3].times_inspected == monkey_3


def test_total_counts_no_worry():
    """Test the active inspected for all the monkeys no worry divide"""
    monkeys = parse_monkeys_from_string(TEST_MONKEY_INPUT, True, 23 * 19 * 13 * 17)
    run_rounds(10000, monkeys)
    assert get_most_active_inspected(monkeys) == 2713310158
