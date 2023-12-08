"""Solution for day8 of 2023"""

from dataclasses import dataclass
import math
from typing import Dict, Tuple


@dataclass
class Node:
    """Class representing a node"""

    name: str
    left: str
    right: str

    @staticmethod
    def from_string(input_str: str) -> "Node":
        """Create a Node from a string input"""
        name, nodes = input_str.strip().split("=")
        left, right = nodes.strip().split(",")
        left = left.strip().removeprefix("(").strip()
        right = right.strip().removesuffix(")").strip()
        name = name.strip()
        return Node(name, left, right)


def read_lines(input_str: str) -> Tuple[str, Dict[str, Node]]:
    """Read the input file and create the nodes"""
    lines = input_str.splitlines()
    instructions = lines[0].strip()
    nodes = {}

    for line in lines[2:]:
        new_node = Node.from_string(line)
        nodes[new_node.name] = new_node
    return instructions, nodes


def follow_instructions(
    instructions: str, nodes: Dict[str, Node], starting_node: str = "AAA", all_zs=True
) -> int:
    """Get the amount of steps it takes to reach ZZZ"""

    current_node = starting_node
    i = 0
    steps = 0
    while (all_zs and current_node != "ZZZ") or (
        not all_zs and current_node[-1] != "Z"
    ):
        if i >= len(instructions):
            i = 0
        instruction = instructions[i]
        current_node = (
            nodes[current_node].left
            if instruction == "L"
            else nodes[current_node].right
        )
        steps += 1
        i += 1
    return steps


def follow_instructions_ghost(instructions: str, nodes: Dict[str, Node]) -> int:
    """Follow the instructions for ghost"""
    current_nodes = []
    for node in nodes.keys():
        if node[-1] == "A":
            current_nodes.append(node)

    steps_to_finish = [
        follow_instructions(instructions, nodes, node, False) for node in current_nodes
    ]
    answer = math.lcm(*steps_to_finish)
    return answer


if __name__ == "__main__":
    with open("year_2023/inputs/day8_input.txt", encoding="utf-8") as file:
        input_file = file.read()
    print(f"Day 8 part 1: {follow_instructions(*read_lines(input_file))}")
    print(f"Day 8 part 2: {follow_instructions_ghost(*read_lines(input_file))}")
