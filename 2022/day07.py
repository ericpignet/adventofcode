with open("2022/input_files/day07t") as f:
    data = "".join([line for line in f])
    commands = [group.split("\n") for group in data.split("\n$ ")]

part1_size_small_dirs = 0

all_dir_sizes = []


class Node:
    def __init__(self, name, is_dir, parent=None, size=0):
        self.children = []
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.parent = parent

    def calculate_size(self):
        size = 0
        for child in self.children:
            child_size = 0
            if child.is_dir:
                child_size = child.calculate_size()
            else:
                child_size = child.size
            size += child_size
        self.size = size
        if size <= 100000:
            global part1_size_small_dirs
            part1_size_small_dirs += size
        return size

    def populate_all_sizes(self):
        global all_dir_sizes
        all_dir_sizes.append(self.size)
        for child in self.children:
            if child.is_dir:
                child.populate_all_sizes()


tree = Node("", True)

# Process commands and populate tree
for command in commands:
    if command[0][0:2] == "$ ":
        command[0] = command[0][2:]
    if command[0][0:2] == "cd":
        target_dir = command[0][3:]
        if target_dir == "..":
            cur_dir = cur_dir.parent
        elif target_dir == "/":
            cur_dir = tree
        else:
            cur_dir = next(x for x in cur_dir.children if x.name == target_dir)
    elif command[0] == "ls":
        for item in command[1:]:
            item = item.split()
            new = Node(
                item[1],
                (item[0] == "dir"),
                cur_dir,
                int(item[0] if item[0] != "dir" else 0),
            )
            cur_dir.children.append(new)

    print(f"{cur_dir.name=}")

# Calculate directory sizes
treesize = tree.calculate_size()
print(f"{treesize=}")
print(f"{part1_size_small_dirs=}")

# Part 2
unused_space = 70000000 - treesize
disk_space_to_free = 30000000 - unused_space
print(f"{disk_space_to_free=}")

tree.populate_all_sizes()
all_dir_sizes.sort(reverse=True)
print(f"{all_dir_sizes=}")
part2_best_dir_to_delete = all_dir_sizes[0]
for size in all_dir_sizes:
    if size < disk_space_to_free:
        break
    else:
        part2_best_dir_to_delete = size

print(f"{part2_best_dir_to_delete=}")
