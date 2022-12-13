# https://adventofcode.com/2022/day/11

from typing import List
from collections import deque
import math

part = 2


class Monkey:
    def __init__(
        self,
        nb: int,
        items,
        operation,
        operationValue,
        test: int,
        monkeyIfTrue,
        monkeyIfFalse,
    ):
        self.nb = nb
        self.items = items
        self.operation = operation
        self.operationValue = operationValue
        self.test = test
        self.monkeyIfTrue = monkeyIfTrue
        self.monkeyIfFalse = monkeyIfFalse
        self.nbInspections = 0


groups = []
with open("2022/input_files/day11") as f:
    data = "".join([line for line in f])
    groups = [group.split("\n") for group in data.split("\n\n")]

monkeys: List[Monkey] = []

for group in groups:
    starting_items = deque(map(int, group[1].split(":")[1].split(",")))
    monkey = Monkey(
        int(group[0][7:-1]),
        starting_items,
        group[2][23],
        group[2][25:],
        int(group[3][21:]),
        int(group[4].split()[-1]),
        int(group[5].split()[-1]),
    )
    monkeys.append(monkey)

productTestIntegers = math.prod([monkey.test for monkey in monkeys])

for cycle in range(20 if part == 1 else 10000):
    for monkey in monkeys:
        while monkey.items:
            worryLevel = monkey.items.popleft()
            monkey.nbInspections += 1
            operationValue = (
                worryLevel
                if monkey.operationValue == "old"
                else int(monkey.operationValue)
            )
            if monkey.operation == "*":
                worryLevel *= operationValue
            elif monkey.operation == "+":
                worryLevel += operationValue
            if part == 1:
                worryLevel = int(worryLevel / 3)
            else:
                worryLevel = worryLevel % productTestIntegers
            if worryLevel % monkey.test == 0:
                monkeys[monkey.monkeyIfTrue].items.append(worryLevel)
            else:
                monkeys[monkey.monkeyIfFalse].items.append(worryLevel)
            # print(f"{worryLevel=}")
    if cycle % 10 == 0:
        print(f"{cycle=}")

monkeys.sort(key=lambda x: x.nbInspections, reverse=True)
monkey_business = monkeys[0].nbInspections * monkeys[1].nbInspections
print(f"{monkey_business=}")
