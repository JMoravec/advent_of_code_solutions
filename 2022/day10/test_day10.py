"""Tests for day 10"""

import pytest
from day10.day10 import run_all_instructions, CPU


TEST_INSTRUCTIONS = (
    "addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\n"
    "addx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1"
    "\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11"
    "\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\n"
    "addx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\n"
    "addx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1"
    "\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\n"
    "addx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\n"
    "addx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop"
    "\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\n"
    "addx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9"
    "\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2"
    "\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1"
    "\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\n"
    "addx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop"
)


@pytest.mark.parametrize(
    "instruction,expected_cycle,expected_regx",
    [("noop", 1, 1), ("addx 3", 2, 4), ("addx -5", 2, -4)],
)
def test_cpu(instruction: str, expected_cycle: int, expected_regx: int):
    """Test individual instructions on the cpu"""
    cpu = CPU()
    cpu.run_instruction(instruction)
    assert cpu.cycle == expected_cycle
    assert cpu.register_x == expected_regx


def test_register_x():
    """Test that basic instructions correctly run the cpu"""
    instructions = "noop\naddx 3\naddx -5"
    end_state = run_all_instructions(instructions)
    assert end_state.cycle == 5
    assert end_state.register_x == -1


def test_signal_strength():
    """Test the signal strength at various places"""
    end_state = run_all_instructions(TEST_INSTRUCTIONS)
    assert end_state._signal_strengths[20] == 420
    assert end_state._signal_strengths[60] == 1140
    assert end_state._signal_strengths[100] == 1800
    assert end_state._signal_strengths[140] == 2940
    assert end_state._signal_strengths[180] == 2880
    assert end_state._signal_strengths[220] == 3960


def test_full_signal_strength():
    """Test the sum of the signal strengths is correct"""
    end_state = run_all_instructions(TEST_INSTRUCTIONS)
    assert end_state.get_full_signal_strength() == 13140


def test_screen_output():
    """Test the screen output of the cpu"""
    end_state = run_all_instructions(TEST_INSTRUCTIONS)
    assert (
        end_state.render_screen() == "##..##..##..##..##..##..##..##..##..##..\n"
        "###...###...###...###...###...###...###.\n"
        "####....####....####....####....####....\n"
        "#####.....#####.....#####.....#####.....\n"
        "######......######......######......####\n"
        "#######.......#######.......#######.....\n"
    )
