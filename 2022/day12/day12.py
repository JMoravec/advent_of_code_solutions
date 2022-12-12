"""Day 12 of Advent of code 2022"""

from dataclasses import dataclass
from queue import Queue
from typing import List, Tuple


@dataclass
class Point:
    """Represents a point on the heightmap"""

    x_coor: int
    y_coor: int
    height: int
    distance: int


def convert_height(input_char: str) -> int:
    """Convert a letter string to a height value"""
    return "abcdefghijklmnopqrstuvwxyz".index(input_char)


def parse_graph(
    input_str: str, skip_starting: bool = False
) -> Tuple[Point, Point, List[List[Point]]]:
    """Parse the graph into starting point, ending point, parsed list"""
    all_points = []
    starting_point = None
    ending_point = None
    for y_index, row in enumerate(input_str.splitlines()):
        current_row = []
        for x_index, char in enumerate(row):
            if char == "S":
                height = 999999 if skip_starting else 0
                current_point = Point(x_index, y_index, convert_height("a"), height)
                starting_point = current_point
            elif char == "E":
                current_point = Point(x_index, y_index, convert_height("z"), 999999)
                ending_point = current_point
            else:
                current_point = Point(x_index, y_index, convert_height(char), 999999)
            current_row.append(current_point)
        all_points.append(current_row)

    if not starting_point or not ending_point:
        raise Exception("Starting or ending point not found")
    return (starting_point, ending_point, all_points)


def _test_current_point(test_point: Point, current_height: int, current_distance: int):
    return (
        test_point.height <= current_height + 1
        and current_distance < test_point.distance
    )


def add_points_to_queue(
    queue: Queue[Point], current_point: Point, all_points: List[List[Point]]
):
    """Add the next points of the queue to the queue"""
    current_height = current_point.height
    current_y = current_point.y_coor
    current_x = current_point.x_coor
    current_distance = current_point.distance + 1

    if current_x != 0:
        test_point = all_points[current_y][current_x - 1]

        if _test_current_point(test_point, current_height, current_distance):
            test_point.distance = current_distance
            queue.put(test_point)

    if current_x != len(all_points[0]) - 1:
        test_point = all_points[current_y][current_x + 1]
        if _test_current_point(test_point, current_height, current_distance):
            test_point.distance = current_distance
            queue.put(test_point)

    if current_y != 0:
        test_point = all_points[current_y - 1][current_x]
        if _test_current_point(test_point, current_height, current_distance):
            test_point.distance = current_distance
            queue.put(test_point)

    if current_y != len(all_points) - 1:
        test_point = all_points[current_y + 1][current_x]
        if _test_current_point(test_point, current_height, current_distance):
            test_point.distance = current_distance
            queue.put(test_point)


def find_shortest_path(
    starting_point: Point, ending_point: Point, all_points: List[List[Point]]
) -> int:
    """Find the length of the shortest path"""
    queue: Queue[Point] = Queue()
    queue.put(starting_point)
    while queue.qsize() != 0:
        current_point = queue.get()
        add_points_to_queue(queue, current_point, all_points)
    return all_points[ending_point.y_coor][ending_point.x_coor].distance


def get_list_of_starting_points(graph: List[List[Point]]) -> List[Point]:
    """Get the list of starting points"""
    starting_points = []
    for row in graph:
        for point in row:
            if point.height == 0:
                starting_points.append(point)
    return starting_points


def find_shortest_starting_path(input_str: str) -> int:
    """Find the shortest path at any starting point"""
    _, _, all_points_starting = parse_graph(input_str, True)
    shortest_path = 999999
    for starting_point in get_list_of_starting_points(all_points_starting):
        starting_point.distance = 0
        _, ending_point, all_points = parse_graph(input_str, True)
        path_length = find_shortest_path(starting_point, ending_point, all_points)
        if path_length < shortest_path:
            shortest_path = path_length
    return shortest_path


def part_1() -> int:
    """Solve part 1 of day 2022"""
    with open("input.txt", "r", encoding="utf-8") as file:
        lines = file.read()
    return find_shortest_path(*parse_graph(lines))


def part_2() -> int:
    """Solve part 2 of day 2022"""
    with open("input.txt", "r", encoding="utf-8") as file:
        lines = file.read()
    return find_shortest_starting_path(lines)


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
