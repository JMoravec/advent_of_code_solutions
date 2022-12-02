"""
Day 2 solution of 2022 Advent of Code
"""

from enum import Enum
from typing import List, Tuple


class RPSResult(Enum):
    """
    Point values for result state
    """

    LOSS = 0
    DRAW = 3
    WIN = 6

    @classmethod
    def get_result_from_str(cls, input_str: str) -> "RPSResult":
        """
        Get the result value for a leter string
        """
        if input_str == "X":
            return RPSResult.LOSS
        if input_str == "Y":
            return RPSResult.DRAW
        if input_str == "Z":
            return RPSResult.WIN
        raise Exception("Not a valid result str")


class RPS(Enum):
    """
    The Rock Paper Scissors point values
    """

    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def get_rps_from_str(cls, input_str: str) -> "RPS":
        """
        Get the RPS value for a letter string
        """
        if input_str in ["A", "X"]:
            return RPS.ROCK
        if input_str in ["B", "Y"]:
            return RPS.PAPER
        if input_str in ["C", "Z"]:
            return RPS.SCISSORS

        raise Exception(f"Not valid input for RPS: {input_str}")


def calculate_points(myself: RPS, result: RPSResult) -> int:
    """
    Get the point value of the play
    """
    return myself.value + result.value


def calculate_points_for_opponent(opponent: RPS, result: RPSResult) -> int:
    """
    Calculate the score given the opponents move and the result
    """
    return calculate_points(get_needed_move(opponent, result), result)


def play_rps(opponent: RPS, myself: RPS) -> RPSResult:
    """
    Play a game of Rock paper scissors
    """
    if opponent == myself:
        return RPSResult.DRAW
    if opponent == RPS.ROCK:
        if myself == RPS.PAPER:
            return RPSResult.WIN
        return RPSResult.LOSS
    if opponent == RPS.PAPER:
        if myself == RPS.SCISSORS:
            return RPSResult.WIN
        return RPSResult.LOSS
    if opponent == RPS.SCISSORS:
        if myself == RPS.ROCK:
            return RPSResult.WIN
        return RPSResult.LOSS
    raise Exception("No result possible?")


def get_needed_move(opponent: RPS, result: RPSResult) -> RPS:
    """
    Get the required move against opponent given the result
    """
    if result == RPSResult.DRAW:
        return opponent
    if result == RPSResult.WIN:
        if opponent == RPS.PAPER:
            return RPS.SCISSORS
        if opponent == RPS.ROCK:
            return RPS.PAPER
        return RPS.ROCK
    if result == RPSResult.LOSS:
        if opponent == RPS.PAPER:
            return RPS.ROCK
        if opponent == RPS.ROCK:
            return RPS.SCISSORS
        return RPS.PAPER
    raise Exception("Something went wrong")


def parse_input_part_1() -> List[Tuple[RPS, RPS]]:
    """
    Parse the text input for the day for part 1
    """
    output = []
    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            game = line.split(" ")
            output.append(
                (
                    RPS.get_rps_from_str(game[0].strip()),
                    RPS.get_rps_from_str(game[1].strip()),
                )
            )
    return output


def parse_input_part_2() -> List[Tuple[RPS, RPSResult]]:
    """
    Parse the text input for the day for part 1
    """
    output = []
    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            game = line.split(" ")
            output.append(
                (
                    RPS.get_rps_from_str(game[0].strip()),
                    RPSResult.get_result_from_str(game[1].strip()),
                )
            )
    return output


def part_1() -> int:
    """
    Compute the solution to part 1
    """
    total_score = 0
    for game in parse_input_part_1():
        result = play_rps(game[0], game[1])
        total_score += calculate_points(game[1], result)
    return total_score


def part_2() -> int:
    """
    Compute the solution to part 2
    """
    total_score = 0
    for game in parse_input_part_2():
        total_score += calculate_points_for_opponent(game[0], game[1])
    return total_score


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
