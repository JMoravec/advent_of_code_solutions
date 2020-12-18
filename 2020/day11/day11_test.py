"""
Test module for day 11 2020
"""
import pytest
from day11.day11 import (
    run_simulation,
    get_list_from_input,
    get_output,
    run_n_rounds_of_simulation,
    solve_part_1,
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
