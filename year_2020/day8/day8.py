"""
Day 8 of advent of code 2020
"""
from typing import List, Set


class Computer:
    """
    Store the computer info
    """

    def __init__(self, program: List[str], initial_value: int = 0):
        self.program = program
        self.accumulator = initial_value
        self.pc = 0

    def _process_instruction(self, instruction: str):
        operation, argument_str = instruction.split(" ")
        argument = int(argument_str)

        if operation == "nop":
            self.pc += 1
        elif operation == "acc":
            self.accumulator += argument
            self.pc += 1
        elif operation == "jmp":
            self.pc += argument

    def run_program(self, debug=False) -> bool:
        """
        Run the program of the computer and returns True if the program
        terminated correctly
        """
        ran_lines: Set[int] = set()
        in_loop = False
        while self.pc < len(self.program):
            if debug:
                print(f"ran_pc: {ran_lines}")
                print(f"pc: {self.pc}")
                print(f"acc: {self.accumulator}")
                print(f"program: {self.program[self.pc]}")
                print()
            ran_lines.add(self.pc)
            self._process_instruction(self.program[self.pc])
            if self.pc in ran_lines:
                in_loop = True
                break

        return not in_loop


def solve_part_1(program: List[str]) -> int:
    """
    Solve part 1 of the day
    """
    new_computer = Computer(program)
    new_computer.run_program()
    return new_computer.accumulator


def solve_part_2(program: List[str]) -> int:
    for i, instruction in enumerate(program):
        new_program = program.copy()
        if "nop" in instruction:
            new_program[i] = instruction.replace("nop", "jmp")
        elif "jmp" in instruction:
            new_program[i] = instruction.replace("jmp", "nop")
        else:
            continue
        computer = Computer(new_program)
        if computer.run_program():
            return computer.accumulator
    return -1


def main():
    """
    Main method to run the day's input
    """
    with open("day8_input.txt") as problem_file:
        all_inputs = problem_file.readlines()
    print(f"Part 1: {solve_part_1(all_inputs)}")
    print(f"Part 2: {solve_part_2(all_inputs)}")


if __name__ == "__main__":
    main()
