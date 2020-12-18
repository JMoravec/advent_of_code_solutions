"""
Day 11 of advent of code 2020
"""
from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple
from enum import auto, Enum


class ChairStatus(Enum):
    """
    Enum for the vairious states a chair can be in
    """

    EMPTY = auto()
    OCCUPIED = auto()
    FLOOR = auto()


@dataclass
class Chair:
    """
    Class to hold information about a single chair
    """

    x_point: int
    y_point: int
    status: ChairStatus

    def get_new_chair_status(self, all_chairs: List[List["Chair"]]) -> "Chair":
        """
        Return the new chair status
        """
        max_y = len(all_chairs) - 1
        max_x = len(all_chairs[0]) - 1

        if self.status == ChairStatus.FLOOR:
            return Chair(self.x_point, self.y_point, ChairStatus.FLOOR)

        list_of_points = self.get_points_to_check(max_x, max_y)
        # print()
        # print(f'{self.x_point=}, {self.y_point=}')
        # print(f'{list_of_points=}')

        if self.status == ChairStatus.EMPTY:
            no_occupied_seats = True
            for y, x in list_of_points:
                # print(f'{max_y=} {max_x=} {y=} {x=}')
                if all_chairs[y][x].status == ChairStatus.OCCUPIED:
                    no_occupied_seats = False
                    break
            new_status = (
                ChairStatus.OCCUPIED if no_occupied_seats else ChairStatus.EMPTY
            )
        else:
            ocupied_seats = 0
            for y, x in list_of_points:
                if all_chairs[y][x].status == ChairStatus.OCCUPIED:
                    ocupied_seats += 1
            new_status = (
                ChairStatus.EMPTY if ocupied_seats >= 4 else ChairStatus.OCCUPIED
            )

        return Chair(self.x_point, self.y_point, new_status)

    def get_points_to_check(self, max_x: int, max_y: int) -> List[Tuple[int, int]]:
        """
        Get the list of points to check for a chair
        """
        list_of_points: List[Tuple[int, int]] = []
        # middle cases
        if (
            self.x_point > 0
            and self.x_point < max_x
            and self.y_point > 0
            and self.y_point < max_y
        ):
            list_of_points.append((self.y_point, self.x_point + 1))
            list_of_points.append((self.y_point, self.x_point - 1))
            list_of_points.append((self.y_point + 1, self.x_point))
            list_of_points.append((self.y_point + 1, self.x_point + 1))
            list_of_points.append((self.y_point + 1, self.x_point - 1))
            list_of_points.append((self.y_point - 1, self.x_point))
            list_of_points.append((self.y_point - 1, self.x_point + 1))
            list_of_points.append((self.y_point - 1, self.x_point - 1))
        # corner cases
        # top left
        elif self.x_point == 0 and self.y_point == 0:
            list_of_points.append((self.y_point, self.x_point + 1))
            list_of_points.append((self.y_point + 1, self.x_point + 1))
            list_of_points.append((self.y_point + 1, self.x_point))
        # bottom left
        elif self.x_point == 0 and self.y_point == max_y:
            list_of_points.append((self.y_point, self.x_point + 1))
            list_of_points.append((self.y_point - 1, self.x_point + 1))
            list_of_points.append((self.y_point - 1, self.x_point))
        # top right
        elif self.x_point == max_x and self.y_point == 0:
            list_of_points.append((self.y_point, self.x_point - 1))
            list_of_points.append((self.y_point + 1, self.x_point - 1))
            list_of_points.append((self.y_point + 1, self.x_point))
        # bottom right
        elif self.x_point == max_x and self.y_point == max_y:
            list_of_points.append((self.y_point, self.x_point - 1))
            list_of_points.append((self.y_point - 1, self.x_point - 1))
            list_of_points.append((self.y_point - 1, self.x_point))
        # edge cases
        # top edge
        elif self.x_point not in [0, max_x] and self.y_point == 0:
            list_of_points.append((self.y_point, self.x_point - 1))
            list_of_points.append((self.y_point, self.x_point + 1))
            list_of_points.append((self.y_point + 1, self.x_point - 1))
            list_of_points.append((self.y_point + 1, self.x_point))
            list_of_points.append((self.y_point + 1, self.x_point + 1))
        # bottom edge
        elif self.x_point not in [0, max_x] and self.y_point == max_y:
            list_of_points.append((self.y_point, self.x_point - 1))
            list_of_points.append((self.y_point, self.x_point + 1))
            list_of_points.append((self.y_point - 1, self.x_point - 1))
            list_of_points.append((self.y_point - 1, self.x_point))
            list_of_points.append((self.y_point - 1, self.x_point + 1))
        # left edge
        elif self.y_point not in [0, max_y] and self.x_point == 0:
            list_of_points.append((self.y_point - 1, self.x_point))
            list_of_points.append((self.y_point - 1, self.x_point + 1))
            list_of_points.append((self.y_point, self.x_point + 1))
            list_of_points.append((self.y_point + 1, self.x_point))
            list_of_points.append((self.y_point + 1, self.x_point + 1))
        # right edge
        elif self.y_point not in [0, max_y] and self.x_point == max_x:
            list_of_points.append((self.y_point - 1, self.x_point))
            list_of_points.append((self.y_point - 1, self.x_point - 1))
            list_of_points.append((self.y_point, self.x_point - 1))
            list_of_points.append((self.y_point + 1, self.x_point))
            list_of_points.append((self.y_point + 1, self.x_point - 1))

        return list_of_points

    @staticmethod
    def generate_chair_from_char(x_point: int, y_point: int, char: str) -> "Chair":
        if char == "L":
            status = ChairStatus.EMPTY
        elif char == "#":
            status = ChairStatus.OCCUPIED
        else:
            status = ChairStatus.FLOOR
        return Chair(x_point, y_point, status)


def run_simulation(all_chairs: List[List[Chair]]) -> List[List[Chair]]:
    """
    Run 1 instance of the simulation
    """
    new_set: List[List[Chair]] = []
    for row in all_chairs:
        new_row: List[Chair] = []
        for test_chair in row:
            new_row.append(test_chair.get_new_chair_status(all_chairs))
        new_set.append(new_row)
    return new_set


def run_n_rounds_of_simulation(
    all_chairs: List[List[Chair]], rounds: int
) -> List[List[Chair]]:
    """
    Run multiple rounds of the simulation
    """
    for _ in range(rounds):
        all_chairs = run_simulation(all_chairs)
    return all_chairs


def get_list_from_input(input_lines: List[str]) -> List[List[Chair]]:
    all_chairs: List[List[Chair]] = []
    for y, row in enumerate(input_lines):
        new_row: List[Chair] = []
        for x, char in enumerate(row):
            new_row.append(Chair.generate_chair_from_char(x, y, char))
        all_chairs.append(new_row)
    return all_chairs


def get_output(all_chairs: List[List[Chair]]) -> str:
    output_str = ""
    for row in all_chairs:
        for chair in row:
            if chair.status == ChairStatus.EMPTY:
                output_char = "L"
            elif chair.status == ChairStatus.OCCUPIED:
                output_char = "#"
            else:
                output_char = "."
            output_str += output_char
        output_str += "\n"
    return output_str[:-1]


def solve_part_1(input_str: List[str]) -> int:
    all_chairs = get_list_from_input(input_str)
    while True:
        new_chairs = run_n_rounds_of_simulation(all_chairs, 10)
        if new_chairs == all_chairs:
            break
        all_chairs = new_chairs
    count = Counter(get_output(all_chairs))
    return count["#"]


def main():
    """
    Main method to run the day's input
    """
    with open("day11_input.txt") as problem_file:
        all_inputs = problem_file.readlines()

    print(f"Part 1: {solve_part_1(all_inputs)}")
    # print(f"Part 2: {solve_part_2(all_inputs_int)}")


if __name__ == "__main__":
    main()
