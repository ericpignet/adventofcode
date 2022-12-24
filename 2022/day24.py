# https://adventofcode.com/2022/day/24
# part 1: 249
# part 2: trip1=249 trip2=246 trip3=240 (trip1+trip2+trip3)=735

import copy
from collections import deque

grid = []
with open("2022/input_files/day24") as f:
    for line in f:
        row = []
        for c in line.rstrip():
            tile = {"#": 0, ">": 0, "<": 0, "v": 0, "^": 0, "f": 1}
            if c != ".":
                tile[c] += 1
                tile["f"] = 0  # means it is not free
            row.append(tile)
        row = list(map(lambda x: {x: 1} if x != "." else {}, line.rstrip()))
        grid.append(row)

width = len(grid[0])
height = len(grid)


def apply_move(grid, char, x, y, new_x, new_y):
    grid[y][x][char] -= 1
    # we know f was 0, because there was a blizzard on it
    grid[y][x]["f"] = 1 if sum(grid[y][x].values()) == 0 else 0
    grid[new_y][new_x][char] += 1
    old_free_value = grid[new_y][new_x]["f"]
    grid[new_y][new_x]["f"] = 1 if sum(grid[new_y][new_x].values()) - old_free_value == 0 else 0


def display_grid(grid, me_x, me_y):
    print()
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if (x, y) == (me_x, me_y):
                print("E", end="")
            elif tile["#"] > 0:
                print("#", end="")
            elif tile["f"] == 1:
                print(".", end="")
            elif sum(tile.values()) > 1:
                print(sum(tile.values()), end="")
            elif sum(tile.values()) == 1:
                print(next(x for x in tile if tile[x] == 1), end="")
            else:
                print(".", end="")
        print()


def update_grid(grid) -> list:
    new_grid = copy.deepcopy(grid)
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            for type in ">", "<", "v", "^":
                for _ in range(tile[type]):
                    if type == ">":
                        new_x = 1 if grid[y][x + 1]["#"] > 0 else x + 1
                        apply_move(new_grid, ">", x, y, new_x, y)
                    elif type == "<":
                        new_x = width - 2 if grid[y][x - 1]["#"] > 0 else x - 1
                        apply_move(new_grid, "<", x, y, new_x, y)
                    elif type == "^":
                        new_y = height - 2 if grid[y - 1][x]["#"] > 0 else y - 1
                        apply_move(new_grid, "^", x, y, x, new_y)
                    elif type == "v":
                        new_y = 1 if grid[y + 1][x]["#"] > 0 else y + 1
                        apply_move(new_grid, "v", x, y, x, new_y)
    return new_grid


def free_neighbours(grid, x, y):
    if y != height - 1 and grid[y + 1][x]["f"]:
        yield (x, y + 1)
    if grid[y][x + 1]["f"]:
        yield (x + 1, y)
    if y != 0 and grid[y - 1][x]["f"]:
        yield (x, y - 1)
    if grid[y][x - 1]["f"]:
        yield (x - 1, y)
    # or stay still
    if grid[y][x]["f"]:
        yield (x, y)


def bfs(grid, start, end):
    queue = deque([(start[0], start[1], 0)])
    old_steps = -1
    while queue:
        me_x, me_y, steps = queue.popleft()

        if steps > old_steps:
            # print(f"{steps=} {len(queue)=}")

            # check dupes
            queue_as_set = set(queue)
            if len(queue) != len(queue_as_set):
                queue = deque(queue_as_set)

            grid = update_grid(grid)
            # display_grid(grid, me_x, me_y)
            old_steps = steps

        for tile in free_neighbours(grid, me_x, me_y):
            if (tile[0], tile[1]) == end:
                print(f"Nice! We found it in {steps+1} steps")
                return grid, steps + 1
            queue.append((tile[0], tile[1], steps + 1))


display_grid(grid, 1, 0)
grid, trip1 = bfs(grid, (1, 0), (width - 2, height - 1))

display_grid(grid, width - 2, height - 1)
grid, trip2 = bfs(grid, (width - 2, height - 1), (1, 0))

display_grid(grid, 1, 0)
grid, trip3 = bfs(grid, (1, 0), (width - 2, height - 1))

print(f"{trip1=} {trip2=} {trip3=} {(trip1+trip2+trip3)=}")
