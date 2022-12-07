"""Day 7 of Advent of code 2022"""

from enum import Enum, auto
from typing import List, Optional


class FileType(Enum):
    """File type of a given file object"""

    FILE = auto()
    DIRECTORY = auto()


class TreeNode:
    """A node of the filesystem tree"""

    name: str
    size: int
    type: FileType
    children: List["TreeNode"]
    parent: Optional["TreeNode"]

    def __init__(self, name: str, filetype: FileType, size: int = 0) -> None:
        self.name = name
        self.type = filetype
        self.size = size
        self.children = []

    def add_child(self, child_node: "TreeNode") -> None:
        """Add a child to the chilrden of this node"""
        self.children.append(child_node)


def part_1() -> int:
    """Solve part 1 of day 7"""
    return 0


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    # print(f"Part 2: {part_2()}")
