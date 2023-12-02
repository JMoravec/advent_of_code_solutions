"""Tests for day 2 of 2023"""


from typing import List
from year_2023.python.day2.day2 import (
    CubePull,
    Game,
    get_ids_of_valid_games,
    get_power_set_of_game,
    parse_all_lines,
    parse_line,
    solve_part_1,
    solve_part_2,
)
import pytest


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (" 3 blue, 4 red", CubePull(4, 0, 3)),
        (" 2 green, 6 blue", CubePull(0, 2, 6)),
        (" 2 green", CubePull(0, 2, 0)),
        (" 1 blue, 2 green", CubePull(0, 2, 1)),
        (" 3 green, 4 blue, 1 red", CubePull(1, 3, 4)),
        (" 1 green, 1 blue", CubePull(0, 1, 1)),
        (" 8 green, 6 blue, 20 red", CubePull(20, 8, 6)),
        (" 5 blue, 4 red, 13 green", CubePull(4, 13, 5)),
        (" 5 green, 1 red", CubePull(1, 5, 0)),
        (" 1 green, 3 red, 6 blue", CubePull(3, 1, 6)),
        (" 3 green, 6 red", CubePull(6, 3, 0)),
        (" 3 green, 15 blue, 14 red", CubePull(14, 3, 15)),
        (" 6 red, 1 blue, 3 green", CubePull(6, 3, 1)),
        (" 2 blue, 1 red, 2 green", CubePull(1, 2, 2)),
    ],
)
def test_create_cube_pull(input_str: str, expected: CubePull):
    """test the creation of cube pulls from an input str"""
    test_pull = CubePull.create_from_line(input_str)
    assert test_pull.red == expected.red
    assert test_pull.blue == expected.blue
    assert test_pull.green == expected.green


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            Game(1, [CubePull(4, 0, 3), CubePull(1, 2, 6), CubePull(0, 2, 0)]),
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            Game(2, [CubePull(0, 2, 1), CubePull(1, 3, 4), CubePull(0, 1, 1)]),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            Game(3, [CubePull(20, 8, 6), CubePull(4, 13, 5), CubePull(1, 5, 0)]),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            Game(4, [CubePull(3, 1, 6), CubePull(6, 3, 0), CubePull(14, 3, 15)]),
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            Game(5, [CubePull(6, 3, 1), CubePull(1, 2, 2)]),
        ),
    ],
)
def test_create_game(input_str: str, expected: Game):
    """Test that creating a game object from an input line works as expected"""
    game = parse_line(input_str)
    assert game.id == expected.id
    assert len(game.cubes) == len(expected.cubes)
    for i, test_cube in enumerate(game.cubes):
        assert test_cube == expected.cubes[i]


def test_get_valid_ids():
    """Test that getting the valid ids works correctly"""
    input_str = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    games = parse_all_lines(input_str)
    assert get_ids_of_valid_games(games) == [1, 2, 5]
    assert solve_part_1(games) == 8


@pytest.mark.parametrize(
    "input_game,expected",
    [
        (Game(1, [CubePull(4, 0, 3), CubePull(1, 2, 6), CubePull(0, 2, 0)]), 48),
        (Game(2, [CubePull(0, 2, 1), CubePull(1, 3, 4), CubePull(0, 1, 1)]), 12),
        (Game(3, [CubePull(20, 8, 6), CubePull(4, 13, 5), CubePull(1, 5, 0)]), 1560),
        (Game(4, [CubePull(3, 1, 6), CubePull(6, 3, 0), CubePull(14, 3, 15)]), 630),
        (Game(5, [CubePull(6, 3, 1), CubePull(1, 2, 2)]), 36),
    ],
)
def test_get_power_cubes(input_game: Game, expected: int):
    """Validate getting the power set of a single game"""
    assert get_power_set_of_game(input_game) == expected


def test_solve_part_2():
    """validate solving part 2"""
    input_games = [
        Game(1, [CubePull(4, 0, 3), CubePull(1, 2, 6), CubePull(0, 2, 0)]),
        Game(2, [CubePull(0, 2, 1), CubePull(1, 3, 4), CubePull(0, 1, 1)]),
        Game(3, [CubePull(20, 8, 6), CubePull(4, 13, 5), CubePull(1, 5, 0)]),
        Game(4, [CubePull(3, 1, 6), CubePull(6, 3, 0), CubePull(14, 3, 15)]),
        Game(5, [CubePull(6, 3, 1), CubePull(1, 2, 2)]),
    ]
    assert solve_part_2(input_games) == 2286
