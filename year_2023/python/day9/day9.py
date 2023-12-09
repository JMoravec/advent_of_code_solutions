"""Solution for day 9 of 2023"""

from collections import deque
from typing import List


class Nums:
    """Helper class to keep track of stacks and whatnot"""

    def __init__(self, nums: List[int]) -> None:
        self.all_stacks = {0: deque(nums)}
        self.last_nums = {0: nums[-1]}
        self.first_nums = {0: nums[0]}

    def pop(self, level: int, use_left: bool = False) -> int:
        """Get the next level's number in the stack"""
        if current_level := self.all_stacks.get(level):
            return current_level.popleft() if use_left else current_level.pop()
        return self.calculate_next(level - 1, use_left)

    def calculate_next(self, level: int, use_left: bool = False) -> int:
        """Calculate the next number in the stack"""
        last = self.pop(level, use_left)
        next_last = self.pop(level, use_left)
        self.add(level, next_last, use_left)
        if use_left:
            return next_last - last
        return last - next_last

    def add(self, level: int, num: int, use_left: bool = False):
        """Add a number to a stack"""
        if (current_level := self.all_stacks.get(level)) is not None:
            if use_left:
                current_level.appendleft(num)
            else:
                current_level.append(num)
            return
        self.all_stacks[level] = deque()
        self.all_stacks[level].append(num)
        if use_left:
            self.first_nums[level] = num
        else:
            self.last_nums[level] = num

    def get_next_num(self, level: int, use_left: bool = False) -> int:
        """Get the next unknown number of the stack"""
        last = self.pop(level, use_left)
        next_last = self.pop(level, use_left)
        if last == 0 and next_last == 0 and level != 0:
            return 0
        self.add(level, next_last, use_left)
        if use_left:
            self.add(level + 1, next_last - last, use_left)
        else:
            self.add(level + 1, last - next_last, use_left)

        if use_left:
            return self.first_nums[level] - self.get_next_num(level + 1, use_left)

        return self.get_next_num(level + 1) + self.last_nums[level]


def calculate_totals(input_lines: List[str], use_left: bool = False) -> int:
    """Get the total of the next numbers in the lines"""
    total = 0
    for line in input_lines:
        total += Nums([int(num) for num in line.strip().split()]).get_next_num(
            0, use_left
        )
    return total


if __name__ == "__main__":
    with open("year_2023/inputs/day9_input.txt", encoding="utf-8") as file:
        lines = file.readlines()
    print(f"Day 9 part 1: {calculate_totals(lines)}")
    print(f"Day 9 part 2: {calculate_totals(lines, True)}")
