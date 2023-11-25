with open("2020/input_files/day03") as f:
    grid = [line.rstrip() for line in f]

def pos(x: int, y: int):
    return grid[y][x % len(grid[0])]

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

slope_trees = []
for slope in slopes:
    me = [0, 0]
    nb_trees = 0
    while me[1] < len(grid):
        if pos(me[0], me[1]) == "#":
            nb_trees += 1
        me[0] += slope[0]
        me[1] += slope[1]
    slope_trees.append(nb_trees)
part2_total = 1
for nb_tree in slope_trees:
    part2_total *= nb_tree
print(f"{part2_total=}")
