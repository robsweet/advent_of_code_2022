#!python
from functools import reduce
from pathlib import Path
import ipdb
import json
import re
from copy import deepcopy

raw_monkeys = Path("input_11.txt").read_text().strip()


class Monkey:
    @staticmethod
    def make_monkey(block):
        items = (
            re.sub(r".*Starting items: ([\d ,]+)\n.*", r"\1", block, flags=re.M | re.S)
            .strip()
            .replace(" ", "")
            .split(",")
        )

        op_str = re.sub(r".*Operation: new = (.+?)\n.*", r"\1", block, flags=re.S)

        div_test_str = int(
            re.sub(r".*Test: divisible by (\d+)\n.*", r"\1", block, flags=re.M | re.S)
        )

        true_monkey = int(
            re.sub(
                r".*If true: throw to monkey (\d+)\n.*", r"\1", block, flags=re.M | re.S
            )
        )

        false_monkey = int(
            re.sub(
                r".*If false: throw to monkey (\d+).*", r"\1", block, flags=re.M | re.S
            )
        )

        return Monkey(items, op_str, div_test_str, true_monkey, false_monkey)

    def __init__(self, items, operation, div_test, true_monkey, false_monkey):
        self.items = [int(item) for item in items]
        self.operation = operation
        self.div_test = div_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.items_inspected = 0

    def take_turn(self, divisor, monkeys):
        m = 1
        for div in [m.div_test for m in monkeys]:
            m = m * div

        for _ in range(len(self.items)):
            self.items_inspected += 1
            old = self.items.pop(0)
            to_throw = int(eval(self.operation) // divisor) % m

            throw_to_monkey = (
                self.true_monkey if (to_throw % self.div_test) == 0 else self.false_monkey
            )

            monkeys[throw_to_monkey].items.append(to_throw)


def print_items(monkeys):
    print(
        "\n".join(
            [
                str(idx) + ": [ " + ", ".join([str(i) for i in m.items]) + " ]"
                for idx, m in enumerate(monkeys)
            ]
        )
    )
    print("----------")


def print_inspections(monkeys):
    print(f"\tInspections: {json.dumps([m.items_inspected for m in monkeys])}")


monkeys = []
for monkey_block in re.split(r"Monkey \d:", raw_monkeys):
    if len(monkey_block.replace(" ", "")) > 0:
        monkeys.append(Monkey.make_monkey(monkey_block))

monkeys2 = deepcopy(monkeys)

for _ in range(20):
    for idx, monkey in enumerate(monkeys):
        monkey.take_turn(3, monkeys)


print_inspections(monkeys)
monkey_business = reduce(
    lambda x, y: x * y, sorted([m.items_inspected for m in monkeys])[-2:]
)
print(f"\tMonkey Business Level:  {monkey_business}")


# Part 2
print("\nPart 2:")
for i in range(10000):
    for idx, monkey in enumerate(monkeys2):
        monkey.take_turn(1, monkeys2)

monkey_business = reduce(
    lambda x, y: x * y, sorted([m.items_inspected for m in monkeys2])[-2:]
)
print(f"\tMonkey Business Level:  {monkey_business}")
