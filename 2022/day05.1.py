from collections import deque

with open("2022/input_files/day05") as f:
    data = "".join([line for line in f])
    groups = [group.split("\n") for group in data.split("\n\n")]

indexes = groups[0][-1].split()
nb_stacks = int(indexes[-1])
stacks = [deque() for i in range(nb_stacks)]

for row in groups[0][: len(groups[0]) - 1]:
    print(row)
    idx = 0
    for i in range(nb_stacks):
        stack_letter = row[idx + 1 : idx + 2]
        if stack_letter != " ":
            stacks[i].appendleft(stack_letter)
        idx += 4
for action in groups[1]:
    action = action.split()
    amount = int(action[1])
    origin = int(action[3])
    destination = int(action[5])
    for i in range(amount):
        val = stacks[origin - 1].pop()
        stacks[destination - 1].append(val)
for stack in stacks:
    print(stack[-1], end="")
