"""Day 10 of Advent of code 2022"""


from enum import Enum
from typing import Dict, List


class Command(Enum):
    """Command/instructions available"""

    NOOP = "noop"
    ADDX = "addx"


class CPU:
    """Represents the CPU for the device"""

    register_x: int
    cycle: int
    _signal_strengths: Dict[int, int]
    _screen: List[str]

    def __init__(self) -> None:
        self.register_x = 1
        self.cycle = 0
        self._signal_strengths = {}
        self._screen = ["."] * (40 * 6)

    def _set_signal_strength(self):
        self._signal_strengths[self.cycle] = self.cycle * self.register_x

    def get_full_signal_strength(self):
        """Return the sum of all the signal strengths"""
        return sum(self._signal_strengths.values())

    def _run_cycle(self):
        """Run a single cycle"""
        self._draw_screen()
        self.cycle += 1
        if (self.cycle - 20) % 40 == 0 and self.cycle <= 220:
            self._set_signal_strength()

    def _draw_screen(self):
        # if self.cycle in [self.register_x - 1, self.register_x, self.register_x + 1]:
        pixel = self.cycle % 40
        if self.register_x - 1 <= pixel <= self.register_x + 1:
            # self._screen[self.cycle - 1] = "#"
            self._screen[self.cycle] = "#"

    def render_screen(self) -> str:
        """Print out the results of the screen to a string"""
        screen = ""
        previous_index = 0
        for end_row_index in range(40, len(self._screen) + 1, 40):
            # print(screen)
            screen += "".join(self._screen[previous_index:end_row_index])
            screen += "\n"
            previous_index = end_row_index
        return screen

    def _run_instruction(self, instruction: Command, *params):
        if instruction == Command.NOOP:
            self.noop()
        elif instruction == Command.ADDX:
            self.addx(int(params[0]))

    def run_instruction(self, instruction: str):
        """Run a single instruction"""
        split_instruction = instruction.strip().split(" ")
        if len(split_instruction) == 1:
            self._run_instruction(Command(split_instruction[0]))
        else:
            self._run_instruction(Command(split_instruction[0]), *split_instruction[1:])

    def noop(self):
        """A NOOP command"""
        self._run_cycle()

    def addx(self, v_input: int):
        """Add V to X Register"""
        # 2 cycles for addx
        self._run_cycle()
        self._run_cycle()
        self.register_x += v_input


def run_all_instructions(input_str: str) -> CPU:
    """Run all the instructions in a given string"""
    running_cpu = CPU()
    for instruction in input_str.splitlines():
        if instruction == "addx 1":
            pass
        running_cpu.run_instruction(instruction)
    return running_cpu


def part_1() -> int:
    """Solve part 1 of day 10"""
    with open("input.txt", "r", encoding="utf-8") as file:
        instructions = file.read()
    end_state = run_all_instructions(instructions)
    return end_state.get_full_signal_strength()


def part_2() -> str:
    with open("input.txt", "r", encoding="utf-8") as file:
        instructions = file.read()
    end_state = run_all_instructions(instructions)
    return end_state.render_screen()


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2:\n{part_2()}")
