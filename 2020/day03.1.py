with open("2020/input_files/day03") as f:
    grid = [line.rstrip() for line in f]

def pos(x: int, y: int):
    return grid[y][x % len(grid[0])]

# Display grid
def display():
    for y in range(10):
        for x in range(40):
            print(f"{pos(x, y)}", end="")
        print("")

me = [0, 0]
nb_trees = 0
while me[1] < len(grid):
    if pos(me[0], me[1]) == "#":
        nb_trees += 1
    me[0] += 3
    me[1] += 1
print(f"{nb_trees=}")
