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

def slide_down_slope(trees: List[str]) -> int:
    """
    Get the amount of trees hit when sliding down the slope
    """
    total_trees = 0
    position = Point(0, 0, len(trees[0]), 3, 1)
    position.move_to_next_point()
    while position.y < len(trees):
        if trees[position.y][position.x] == '#':
            total_trees += 1

        position.move_to_next_point()
    return total_trees


def main():
    trees: List[str] = []
    with open('day3_input.txt') as f:
        for row in f.readlines():
            trees.append(row.strip())
    print(f'Part 1: {slide_down_slope(trees)}')

if __name__ == '__main__':
    main()
