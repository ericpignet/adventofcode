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

for action in groups[1]:
    action = action.split()
    amount = int(action[1])
    origin = int(action[3])
    destination = int(action[5])
    boxes_to_be_moved = stacks[origin - 1][-amount:]
    del stacks[origin - 1][-amount:]
    stacks[destination - 1].extend(boxes_to_be_moved)

for stack in stacks:
    print(stack[-1], end="")
