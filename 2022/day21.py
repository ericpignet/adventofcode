# https://adventofcode.com/2022/day/21
from __future__ import annotations
from dataclasses import dataclass

NOVAL = "99999999"


@dataclass
class Monkey:
    name: str
    val: int
    dep1: Monkey
    dep1Str: str  # only needed temporarily until dep1 object is created
    dep2: Monkey
    dep2Str: str  # only needed temporarily until dep2 object is created
    operation: str
    isHuman: bool

    def calculate(self, humanAsNOVAL=False) -> int:
        if humanAsNOVAL and self.isHuman:
            return NOVAL
        if self.val != NOVAL:
            return self.val
        dep1val = self.dep1.calculate(humanAsNOVAL)
        dep2val = self.dep2.calculate(humanAsNOVAL)
        if NOVAL in (dep1val, dep2val):
            return NOVAL
        match self.operation:
            case "+":
                return dep1val + dep2val
            case "-":
                return dep1val - dep2val
            case "*":
                return dep1val * dep2val
            case "/":
                return int(dep1val / dep2val)

    def findUnknown(self, result) -> int:
        if self.isHuman:
            return result
        dep1val = self.dep1.calculate(True)
        dep2val = self.dep2.calculate(True)
        if dep1val == NOVAL:
            new_result = 0
            match self.operation:
                case "+":
                    new_result = result - dep2val
                case "-":
                    new_result = result + dep2val
                case "*":
                    new_result = int(result / dep2val)
                case "/":
                    new_result = result * dep2val
            return self.dep1.findUnknown(new_result)
        elif dep2val == NOVAL:
            new_result = 0
            match self.operation:
                case "+":
                    new_result = result - dep1val
                case "-":
                    new_result = dep1val - result
                case "*":
                    new_result = int(result / dep1val)
                case "/":
                    new_result = int(dep1val / result)
            return self.dep2.findUnknown(new_result)


monkeys: list[Monkey] = []
with open("2022/input_files/day21") as f:
    for data in f:
        data = data.rstrip().split()
        monkeys.append(
            Monkey(
                data[0][:4],
                int(data[1]) if len(data) == 2 else NOVAL,
                None,
                data[1] if len(data) > 2 else "",
                None,
                data[3] if len(data) > 2 else "",
                data[2] if len(data) > 2 else "",
                (data[0][:4] == "humn"),
            )
        )
for monkey in monkeys:
    if monkey.val == NOVAL:
        monkey.dep1 = next(mon for mon in monkeys if mon.name == monkey.dep1Str)
        monkey.dep2 = next(mon for mon in monkeys if mon.name == monkey.dep2Str)

root = next(mon for mon in monkeys if mon.name == "root")

print(f"Part 1: {root.calculate()=}")

pathToAnalyze = None
expectedResult = NOVAL
dep1val = root.dep1.calculate(True)
if dep1val == NOVAL:
    pathToAnalyze = root.dep1
    expectedResult = root.dep2.calculate()
else:
    pathToAnalyze = root.dep2
    expectedResult = dep1val
print(f"Part 2: {pathToAnalyze.findUnknown(expectedResult)=}")
