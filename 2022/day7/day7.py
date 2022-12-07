"""Day 7 of Advent of code 2022"""

from enum import Enum, auto
from typing import Dict, List, Optional


class FileType(Enum):
    """File type of a given file object"""

    FILE = auto()
    DIRECTORY = auto()


UNKNOWN_SIZE = -1
DISK_SIZE_AVAILABLE = 70000000
DISK_SIZE_NEEDED = 30000000


class TreeNode:
    """A node of the filesystem tree"""

    name: str
    _size: int
    type: FileType
    children: Dict[str, "TreeNode"]
    parent: Optional["TreeNode"]

    def __init__(self, name: str, filetype: FileType, size: int = UNKNOWN_SIZE) -> None:
        self.name = name
        self.type = filetype
        self._size = size
        self.children = {}
        self.parent = None

    def add_child(self, child_node: "TreeNode") -> None:
        """Add a child to the chilrden of this node and make its parent this"""
        child_node.add_parent(self)
        self.children[child_node.name] = child_node

    def add_parent(self, parent_node: "TreeNode") -> None:
        """Add a parent to this node"""
        self.parent = parent_node

    def get_size(self) -> int:
        """
        Get the size of the current node, returns UNKNOWN_SIZE if it can't
        determine
        """
        if self._size != UNKNOWN_SIZE:
            return self._size
        if self.type == FileType.DIRECTORY:
            total_size = 0
            for child in self.children.values():
                total_size += child.get_size()
            return total_size
        return UNKNOWN_SIZE

    def get_top_level_node(self) -> "TreeNode":
        """Get the / directory"""
        current_node = self
        while current_node.parent is not None:
            current_node = current_node.parent

        if current_node.name == "/":
            return current_node
        raise Exception("Couldn't find / dir")

    @staticmethod
    def create_from_str(input_line: str) -> "TreeNode":
        """Parse a single line of input that contains file info"""
        info = input_line.split(" ")
        filename = info[1]
        filetype = FileType.DIRECTORY if info[0] == "dir" else FileType.FILE
        size = UNKNOWN_SIZE if filetype == FileType.DIRECTORY else int(info[0])
        return TreeNode(filename, filetype, size)


def parse_cd_command(directory_to_switch_to: str, current_node: TreeNode) -> TreeNode:
    """Parse a cd command"""
    if directory_to_switch_to == "..":
        if current_node.parent is not None:
            return current_node.parent
        raise Exception("No parent to switch to for .. command")
    if directory_to_switch_to == "/":
        return current_node.get_top_level_node()
    return current_node.children[directory_to_switch_to]


def parse_commands(all_commands: List[str], current_node: TreeNode) -> TreeNode:
    """Parse all the given commmands, Returns the / node"""
    for current_command in all_commands:
        split_command = current_command.strip().split(" ")
        if split_command[0] == "$" and split_command[1] == "cd":
            current_node = parse_cd_command(split_command[2], current_node)
        elif split_command[0] == "$" and split_command[1] == "ls":
            pass
        else:
            current_node.add_child(TreeNode.create_from_str(current_command.strip()))

    return current_node.get_top_level_node()


def get_total_size_dir_under_amount(node_to_check: TreeNode, size_to_check: int) -> int:
    """Get the total size of directories under the given size amount"""
    if node_to_check.type == FileType.FILE:
        return 0
    current_total = (
        node_to_check.get_size() if node_to_check.get_size() <= size_to_check else 0
    )
    for child in node_to_check.children.values():
        current_total += get_total_size_dir_under_amount(child, size_to_check)
    return current_total


def flatten_sizes(node_to_check: TreeNode) -> List[int]:
    """Get a list of all the directory sizes"""
    if node_to_check.type == FileType.FILE:
        return []
    sizes: List[int] = [node_to_check.get_size()]
    for child in node_to_check.children.values():
        sizes.extend(flatten_sizes(child))
    sizes.sort()
    return sizes


def get_smallest_deletable_dir(top_level_node: TreeNode) -> int:
    """Get the size of the smallest deletable directory"""
    total_size = top_level_node.get_size()
    current_unused_space = DISK_SIZE_AVAILABLE - total_size
    needed_space_to_delete = DISK_SIZE_NEEDED - current_unused_space
    for size in flatten_sizes(top_level_node):
        if size >= needed_space_to_delete:
            return size
    raise Exception("No dir available to delete")


def part_1() -> int:
    """Solve part 1 of day 7"""
    with open("input.txt", "r", encoding="utf-8") as file:
        commands = file.readlines()
    top_level = TreeNode("/", FileType.DIRECTORY)
    top_level = parse_commands(commands, top_level)
    return get_total_size_dir_under_amount(top_level, 100000)


def part_2() -> int:
    """Solve part 2 of day 7"""
    with open("input.txt", "r", encoding="utf-8") as file:
        commands = file.readlines()
    top_level = TreeNode("/", FileType.DIRECTORY)
    top_level = parse_commands(commands, top_level)
    return get_smallest_deletable_dir(top_level)


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
