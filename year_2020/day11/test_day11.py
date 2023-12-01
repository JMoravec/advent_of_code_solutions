"""
Test module for day 11 2020
"""
from typing import Tuple
import pytest
from year_2020.day11.day11 import (
    run_simulation,
    get_list_from_input,
    get_output,
    run_n_rounds_of_simulation,
    solve_part_1,
    solve_part_2,
)


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (
            "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\n"
            "L.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL",
            "#.##.##.##\n#######.##\n#.#.#..#..\n####.##.##\n#.##.##.##\n"
            "#.#####.##\n..#.#.....\n##########\n#.######.#\n#.#####.##",
        )
    ],
)
def test_one_run_simulation(input_str: str, expected: str):
    input_lines = get_list_from_input(input_str.split("\n"))
    after_1_run = run_simulation(input_lines)
    assert get_output(after_1_run) == expected


@pytest.mark.parametrize(
    "input_str,rounds,expected",
    [
        (
            "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\n"
            "L.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL",
            1,
            "#.##.##.##\n#######.##\n#.#.#..#..\n####.##.##\n#.##.##.##\n"
            "#.#####.##\n..#.#.....\n##########\n#.######.#\n#.#####.##",
        ),
        (
            "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\n"
            "L.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL",
            2,
            "#.LL.L#.##\n#LLLLLL.L#\nL.L.L..L..\n#LLL.LL.L#\n#.LL.LL.LL\n"
            "#.LLLL#.##\n..L.L.....\n#LLLLLLLL#\n#.LLLLLL.L\n#.#LLLL.##",
        ),
        (
            "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\n"
            "L.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL",
            3,
            "#.##.L#.##\n#L###LL.L#\nL.#.#..#..\n#L##.##.L#\n#.##.LL.LL\n"
            "#.###L#.##\n..#.#.....\n#L######L#\n#.LL###L.L\n#.#L###.##",
        ),
        (
            "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\n"
            "L.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL",
            4,
            "#.#L.L#.##\n#LLL#LL.L#\nL.L.L..#..\n#LLL.##.L#\n#.LL.LL.LL\n"
            "#.LL#L#.##\n..L.L.....\n#L#LLLL#L#\n#.LLLLLL.L\n#.#L#L#.##",
        ),
        (
            "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\n"
            "L.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL",
            5,
            "#.#L.L#.##\n#LLL#LL.L#\nL.#.L..#..\n#L##.##.L#\n#.#L.LL.LL\n"
            "#.#L#L#.##\n..L.L.....\n#L#L##L#L#\n#.LLLLLL.L\n#.#L#L#.##",
        ),
    ],
)
def test_n_run_simulation(input_str: str, rounds: int, expected: str):
    input_lines = get_list_from_input(input_str.split("\n"))
    after_n_run = run_n_rounds_of_simulation(input_lines, rounds)
    output = get_output(after_n_run)
    print(output)
    print()
    print(expected)
    assert output == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (
            "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\n"
            "L.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL",
            37,
        )
    ],
)
def test_part_1(input_str: str, expected: int):
    assert solve_part_1(input_str.split("\n")) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (
            "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\n"
            "L.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL",
            26,
        )
    ],
)
def test_part_2(input_str: str, expected: int):
    assert solve_part_2(input_str.split("\n")) == expected


@pytest.mark.parametrize(
    "input_str,test_chair,expected_seen",
    [
        (
            ".......#.\n...#.....\n.#.......\n.........\n..#L....#\n....#....\n.........\n#........\n...#.....",
            (4, 3),
            8,
        ),
        (".............\n.L.L.#.#.#.#.\n.............", (1, 1), 1),
        (".##.##.\n#.#.#.#\n##...##\n...L...\n##...##\n#.#.#.#\n.##.##.", (3, 3), 0),
    ],
)
def test_chairs_seen(input_str: str, test_chair: Tuple[int, int], expected_seen: int):
    input_lines = get_list_from_input(input_str.split("\n"))
    test_chair_actual = input_lines[test_chair[0]][test_chair[1]]
    assert len(test_chair_actual.chairs_seen(input_lines)) == expected_seen


@pytest.mark.parametrize(
    "rounds,expected",
    [
        (
            1,
            "#.##.##.##\n#######.##\n#.#.#..#..\n####.##.##\n#.##.##.##\n#.#####.##\n..#.#.....\n##########\n#.######.#\n#.#####.##",
        ),
        (
            2,
            "#.LL.LL.L#\n#LLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLL#\n#.LLLLLL.L\n#.LLLLL.L#",
        ),
        (
            3,
            "#.L#.##.L#\n#L#####.LL\nL.#.#..#..\n##L#.##.##\n#.##.#L.##\n#.#####.#L\n..#.#.....\nLLL####LL#\n#.L#####.L\n#.L####.L#",
        ),
        (
            4,
            "#.L#.L#.L#\n#LLLLLL.LL\nL.L.L..#..\n##LL.LL.L#\nL.LL.LL.L#\n#.LLLLL.LL\n..L.L.....\nLLLLLLLLL#\n#.LLLLL#.L\n#.L#LL#.L#",
        ),
        (
            5,
            "#.L#.L#.L#\n#LLLLLL.LL\nL.L.L..#..\n##L#.#L.L#\nL.L#.#L.L#\n#.L####.LL\n..#.#.....\nLLL###LLL#\n#.LLLLL#.L\n#.L#LL#.L#",
        ),
        (
            6,
            "#.L#.L#.L#\n#LLLLLL.LL\nL.L.L..#..\n##L#.#L.L#\nL.L#.LL.L#\n#.LLLL#.LL\n..#.L.....\nLLL###LLL#\n#.LLLLL#.L\n#.L#LL#.L#",
        ),
    ],
)
def test_n_run_simulation2(rounds: int, expected: str):
    input_str = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL"
    input_lines = get_list_from_input(input_str.split("\n"))
    after_n_run = run_n_rounds_of_simulation(input_lines, rounds, True)
    output = get_output(after_n_run)
    assert output == expected
