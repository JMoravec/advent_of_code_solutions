"""Day 11 of Advent of code 2022"""


import enum
from typing import Callable, List, Tuple


class OperationsAllowed(enum.Enum):
    """Allowed operations for the monkey"""

    PLUS = "+"
    TIMES = "*"


class Monkey:
    """Represents a monkey for the solution"""

    items: List[int]
    operation: Callable[[int], int]
    test_divisible: int
    true_monkey: int
    false_monkey: int
    times_inspected: int
    worry_constant: int
    use_worry_constant: bool

    def __init__(
        self,
        starting_items: List[int],
        operation: Callable[[int], int],
        test_divisible: int,
        true_monkey: int,
        false_monkey: int,
        use_worry_constant: bool = False,
        worry_constant: int = 0,
    ) -> None:
        self.items = starting_items
        self.operation = operation
        self.test_divisible = test_divisible
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.times_inspected = 0
        self.use_worry_constant = use_worry_constant
        self.worry_constant = worry_constant

    def inspect_item(self) -> Tuple[int, int]:
        """Have the monkey inspect the next item"""
        self.times_inspected += 1
        item = self.items.pop(0)
        new_worry_level = (
            self.operation(item) % self.worry_constant
            if self.use_worry_constant
            else self.operation(item) // 3
        )

        if new_worry_level % self.test_divisible == 0:
            return (new_worry_level, self.true_monkey)
        return (new_worry_level, self.false_monkey)

    def add_item(self, item: int):
        """Add an item to the list of items held"""
        self.items.append(item)

    @classmethod
    def _get_operation(cls, operation: OperationsAllowed) -> Callable[[int, int], int]:
        if operation == OperationsAllowed.PLUS:
            return lambda val1, val2: val1 + val2
        elif operation == OperationsAllowed.TIMES:
            return lambda val1, val2: val1 * val2
        raise Exception("not allowed operation")

    @classmethod
    def create_from_string(
        cls, input_str: str, use_worry_constant: bool = False, worry_constant: int = 0
    ) -> "Monkey":
        """Create a new monkey isntance from input string"""
        lines = input_str.splitlines()
        if len(lines) != 5:
            raise Exception("Input not formatted correctl")

        # starting items
        input_values = lines[0].strip().split(":")[1]
        input_values_split = input_values.strip().split(",")
        starting_items = [int(value.strip()) for value in input_values_split]

        # operation
        operation_values = lines[1].strip().split(" = old ")[1]
        if operation_values[0] == OperationsAllowed.PLUS.value:
            operation = OperationsAllowed.PLUS
        elif operation_values[0] == OperationsAllowed.TIMES.value:
            operation = OperationsAllowed.TIMES
        else:
            raise Exception("Operation not allowed")

        second_argument = operation_values[2:].strip()

        def _both_old(old_value: int):
            return cls._get_operation(operation)(old_value, old_value)

        def _one_old(old_value: int):
            return cls._get_operation(operation)(old_value, int(second_argument))

        operation_function: Callable[[int], int] = (
            _both_old if second_argument == "old" else _one_old
        )

        # test
        test_value = int(lines[2].strip().split(" by ")[1].strip())

        # true/false value
        true_value = int(lines[3].strip().split(" throw to monkey ")[1].strip())
        false_value = int(lines[4].strip().split(" throw to monkey ")[1].strip())

        return Monkey(
            starting_items,
            operation_function,
            test_value,
            true_value,
            false_value,
            use_worry_constant,
            worry_constant,
        )


def parse_monkeys_from_string(
    input_str: str, use_worry_constant: bool = False, worry_constant: int = 0
) -> List[Monkey]:
    """Get the full list of monkeys"""
    monkeys = []
    lines = input_str.splitlines()
    while lines:
        # monkey number
        lines.pop(0)
        new_monkey_str = []
        for _ in range(5):
            new_monkey_str.append(f"{lines.pop(0)}\n")
        monkeys.append(
            Monkey.create_from_string(
                "".join(new_monkey_str), use_worry_constant, worry_constant
            )
        )
        # blank line
        if lines:
            lines.pop(0)
    return monkeys


def run_round(monkeys: List[Monkey]):
    """Run a single round of inspecting items"""
    for monkey in monkeys:
        while monkey.items:
            item, monkey_index = monkey.inspect_item()
            monkeys[monkey_index].add_item(item)


def run_rounds(rounds: int, monkeys: List[Monkey]):
    """Run multiple rounds"""
    for i in range(rounds):
        run_round(monkeys)


def get_most_active_inspected(monkeys: List[Monkey]) -> int:
    """Get the multiplication of active inspected items"""
    inspected_items = [monkey.times_inspected for monkey in monkeys]
    inspected_items.sort()
    return inspected_items[-1] * inspected_items[-2]


def part_1() -> int:
    """Solve part 1 of day 11"""
    with open("input.txt", "r", encoding="utf-8") as file:
        monkey_input = file.read()
    monkeys = parse_monkeys_from_string(monkey_input)
    run_rounds(20, monkeys)
    return get_most_active_inspected(monkeys)


def part_2() -> int:
    """Solve part 2 of day 11"""
    worry_constant = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    with open("input.txt", "r", encoding="utf-8") as file:
        monkey_input = file.read()
    monkeys = parse_monkeys_from_string(monkey_input, True, worry_constant)
    run_rounds(10000, monkeys)
    return get_most_active_inspected(monkeys)


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2:\n{part_2()}")
