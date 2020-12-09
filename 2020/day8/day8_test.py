"""
Test module for day 8 2020
"""
from typing import List
import pytest
from day8.day8 import solve_part_1


@pytest.mark.parametrize(
    "program,expected",
    [
        (
            [
                "nop +0",
                "acc +1",
                "jmp +4",
                "acc +3",
                "jmp -3",
                "acc -99",
                "acc +1",
                "jmp -4",
                "acc +6",
            ],
            5,
        )
    ],
)
def test_part_1(program: List[str], expected: int):
    assert solve_part_1(program) == expected
