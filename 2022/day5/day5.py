"""Day 5 of Advent of code 2022"""

import re
from typing import List, Tuple


def parse_stacks(input_str: str) -> List[List[str]]:
    """Parse the input stacks"""
    all_stacks: List[List[str]] = []
    lines = input_str.splitlines()

    for _ in range((len(lines[0]) + 1) // 4):
        all_stacks.append([])

    for line in lines:
        for i in range(1, len(line), 4):
            if line[i] and line[i].strip():
                try:
                    int(line[i])
                    break
                except ValueError:
                    all_stacks[i // 4] = [line[i]] + all_stacks[i // 4]

    return all_stacks


def move_item_from_stack(from_stack: List[str], to_stack: List[str]):
    """Get the top item from the stack and move it to another stack"""
    to_stack.append(from_stack.pop())


def move_n_from_stack(n_times: int, from_stack: List[str], to_stack: List[str]):
    """Move n items from stack to another stack"""
    for _ in range(n_times):
        move_item_from_stack(from_stack, to_stack)


def move_n_from_stack_at_same_time(
    n_times: int, from_stack: List[str], to_stack: List[str]
):
    """Move a group of containers from one stack to another"""
    for item in from_stack[-n_times:]:
        to_stack.append(item)
    del from_stack[-n_times:]


def get_move_from_str(input_str: str) -> Tuple[int, int, int]:
    """Get the stack move instructions from a string"""
    all_nums = map(int, re.findall(r"\d+", input_str))
    return next(all_nums), next(all_nums), next(all_nums)


def get_all_moves_from_input(all_moves_str: str) -> List[Tuple[int, int, int]]:
    """Parse all the moves from an input string"""
    all_moves: List[Tuple[int, int, int]] = []
    for line in all_moves_str.splitlines():
        all_moves.append(get_move_from_str(line))
    return all_moves


def parse_input(full_input: str) -> Tuple[List[List[str]], List[Tuple[int, int, int]]]:
    """Parse the input string into an initial stack and list of moves"""
    stack_string = ""
    move_string = ""
    parse_move = False
    for line in full_input.splitlines():
        if not line:
            parse_move = True
            continue
        if parse_move:
            move_string += f"{line}\n"
        else:
            stack_string += f"{line}\n"

    return (parse_stacks(stack_string), get_all_moves_from_input(move_string))


def get_final_state(
    stack: List[List[str]], moves: List[Tuple[int, int, int]], move_all_at_a_time: bool
) -> List[List[str]]:
    """Run all the moves on the stack"""
    for move in moves:
        # index is 1 based on the moves
        times, from_stack, to_stack = move
        if move_all_at_a_time:
            move_n_from_stack_at_same_time(
                times, stack[from_stack - 1], stack[to_stack - 1]
            )
        else:
            move_n_from_stack(times, stack[from_stack - 1], stack[to_stack - 1])
    return stack


def get_final_string(stacks: List[List[str]]) -> str:
    """Get the final string of the top of all the stacks"""
    return "".join([stack[-1] for stack in stacks])


def part_1() -> str:
    """Solve part 1 of day 5"""
    with open("input.txt", "r", encoding="utf-8") as file:
        input_str = file.read()

    return get_final_string(get_final_state(*parse_input(input_str), False))


def part_2() -> str:
    """Solve part 2 of day 5"""
    with open("input.txt", "r", encoding="utf-8") as file:
        input_str = file.read()

    return get_final_string(get_final_state(*parse_input(input_str), True))


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
