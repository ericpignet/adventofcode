import copy

with open("2022/input_files/day05") as f:
    data = "".join([line for line in f])
    groups = [group.split("\n") for group in data.split("\n\n")]

indexes = groups[0][-1].split()
nb_stacks = int(indexes[-1])
stacks = [list() for i in range(nb_stacks)]

for row in groups[0][: len(groups[0]) - 1]:
    print(row)
    idx = 0
    for i in range(nb_stacks):
        stack_letter = row[idx + 1 : idx + 2]
        if stack_letter != " ":
            stacks[i].insert(0, stack_letter)
        idx += 4

part2_stacks = copy.deepcopy(stacks)

for action in groups[1]:
    action = action.split()
    amount = int(action[1])
    origin = int(action[3])
    destination = int(action[5])

    # Part 1
    for i in range(amount):
        val = stacks[origin - 1].pop()
        stacks[destination - 1].append(val)

    # Part 2
    boxes_to_be_moved = part2_stacks[origin - 1][-amount:]
    del part2_stacks[origin - 1][-amount:]
    part2_stacks[destination - 1].extend(boxes_to_be_moved)

print("Part 1")
for stack in stacks:
    print(stack[-1], end="")

print("\nPart 2")
for stack in part2_stacks:
    print(stack[-1], end="")
