"""
Day 3 of advent of code 2020
"""
from dataclasses import dataclass
from typing import List

@dataclass
class Point:
    """
    Helper class to keep track of current point
    """
    x: int
    y: int
    max_x: int
    x_vel: int
    y_vel: int

    def move_to_next_point(self):
        """
        Generate where the next point i
        """
        self.x += self.x_vel
        self.y += self.y_vel
        if self.x >= self.max_x:
            self.x -= self.max_x

def slide_down_slope(trees: List[str], toboggan: Point) -> int:
    """
    Get the amount of trees hit when sliding down the slope
    """
    total_trees = 0
    toboggan.move_to_next_point()
    while toboggan.y < len(trees):
        if trees[toboggan.y][toboggan.x] == '#':
            total_trees += 1

        toboggan.move_to_next_point()
    return total_trees


def main():
    trees: List[str] = []
    with open('day3_input.txt') as f:
        for row in f.readlines():
            trees.append(row.strip())
    day_1_toboggan = Point(0, 0, len(trees[0]), 3, 1)
    trees_1 = slide_down_slope(trees, day_1_toboggan)

    print(f'Part 1: {trees_1}')
    toboggan_2 = Point(0, 0, len(trees[0]), 1, 1)
    trees_2 = slide_down_slope(trees, toboggan_2)
    toboggan_3 = Point(0, 0, len(trees[0]), 5, 1)
    trees_3 = slide_down_slope(trees, toboggan_3)
    toboggan_4 = Point(0, 0, len(trees[0]), 7, 1)
    trees_4 = slide_down_slope(trees, toboggan_4)
    toboggan_5 = Point(0, 0, len(trees[0]), 1, 2)
    trees_5 = slide_down_slope(trees, toboggan_5)

    day2_answer = trees_1 * trees_2 * trees_3 * trees_4 * trees_5
    print(f'Part 2: {day2_answer}')


if __name__ == '__main__':
    main()
