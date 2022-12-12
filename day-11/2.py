from dataclasses import dataclass
from math import prod

with open('day-11/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

@dataclass(kw_only=True)
class Monkey:
    items: list[int]
    operation: str
    test_divisible: int
    if_true: int
    if_false: int
    all_monkeys: list["Monkey"]
    inspected_count: int = 0

    def __post_init__(self):
        self.operation_func = lambda old: eval(self.operation)

    def process_items(self, worry_level_divisor: int = 1, mod_factor: int = 0):
        for item in self.items:
            item = self.operation_func(item)
            item = int(item / worry_level_divisor)
            if mod_factor:
                item = item % mod_factor
            if item % self.test_divisible == 0:
                self.all_monkeys[self.if_true].items.append(item)
            else:
                self.all_monkeys[self.if_false].items.append(item)
            self.inspected_count += 1
        self.items = []


def load_monkeys() -> list[Monkey]:
    monkeys: list[Monkey] = []

    monkey_data: list[str] = [""]
    for line in data:
        if not line:
            monkey_data.append("")
        else:
            monkey_data[-1] += line + "\n"

    for monkey in monkey_data:
        rows = monkey.split("\n")
        items = eval("[" + rows[1].split(": ")[1] + "]")
        operation = rows[2].split(" = ")[1]
        test_divisible = int(rows[3].split(" by ")[1])
        if_true = int(rows[4].split(" monkey ")[1])
        if_false = int(rows[5].split(" monkey ")[1])
        monkeys.append(
            Monkey(
                items=items,
                operation=operation,
                test_divisible=test_divisible,
                if_true=if_true,
                if_false=if_false,
                all_monkeys=monkeys
            )
        )
    
    return monkeys



monkeys = load_monkeys()
mod_factor = prod([m.test_divisible for m in monkeys])
for _ in range(10000):
    for monkey in monkeys:
        monkey.process_items(mod_factor=mod_factor)

print(prod(sorted([m.inspected_count for m in monkeys], reverse=True)[0:2]))