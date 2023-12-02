"""Day 2 solution for 2023"""

from dataclasses import dataclass
from typing import List


@dataclass
class CubePull:
    """Helper class to represent a single pull of cubes"""

    red: int
    green: int
    blue: int

    @staticmethod
    def create_from_line(input_str: str) -> "CubePull":
        """create a cube pull from an input str"""
        cubes = input_str.split(",")
        red, green, blue = 0, 0, 0
        for cube in cubes:
            split_cube = cube.strip().split()
            num = int(split_cube[0])
            color = split_cube[1]
            if color == "red":
                red = num
            elif color == "green":
                green = num
            elif color == "blue":
                blue = num
        return CubePull(red, green, blue)


@dataclass
class Game:
    """Helper class to represent a game"""

    id: int
    cubes: List[CubePull]


def parse_all_lines(input_lines: List[str]) -> List[Game]:
    """Get all the games from a list of inputs"""
    return [parse_line(input_line) for input_line in input_lines]


def get_ids_of_valid_games(games: List[Game]) -> List[int]:
    """Get the id values of the valid games"""
    allowed_reds = 12
    allowed_greens = 13
    allowed_blues = 14
    valid_games = []

    for game in games:
        for pull in game.cubes:
            if (
                pull.red > allowed_reds
                or pull.green > allowed_greens
                or pull.blue > allowed_blues
            ):
                break
        else:
            valid_games.append(game.id)
    return valid_games


def solve_part_1(games: List[Game]) -> int:
    """Solve part1 of day 2"""
    return sum(get_ids_of_valid_games(games))


def parse_line(input_line: str) -> Game:
    """Parse a single line of input"""
    game_split = input_line.split(":")
    game_id = int(game_split[0].split()[1])
    games = game_split[1].split(";")
    cubes = [CubePull.create_from_line(game) for game in games]
    return Game(game_id, cubes)


def get_power_set_of_game(game: Game) -> int:
    """Returns min red*blue*green cubes"""
    red = max(cube.red for cube in game.cubes)
    green = max(cube.green for cube in game.cubes)
    blue = max(cube.blue for cube in game.cubes)
    return red * green * blue


def solve_part_2(games: List[Game]) -> int:
    """Solve part2 of day 2"""
    return sum(get_power_set_of_game(game) for game in games)


if __name__ == "__main__":
    with open("year_2023/inputs/day2_input.txt", encoding="utf-8") as file:
        input_lines = file.readlines()
    input_games = parse_all_lines(input_lines)
    print(f"Day 2 part 1: {solve_part_1(input_games)}")
    print(f"Day 2 part 2: {solve_part_2(input_games)}")
