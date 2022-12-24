# https://adventofcode.com/2022/day/24
# 249

import copy
from collections import deque

prune = False
prune_value = 100000
grid = []
with open("2022/input_files/day24tt") as f:
    for line in f:
        # row =
        # for c in line.rstrip()
        row = []
        for c in line.rstrip():
            tile = {"#": 0, ">": 0, "<": 0, "v": 0, "^": 0, "f": 1}
            if c != ".":
                tile[c] += 1
                tile["f"] = 0  # means it is not free
            row.append(tile)
        grid.append(row)
        # data = list(map(lambda x: {x: 1} if x != "." else {}, line.rstrip()))
        # grid.append(data)

# def moveBy1(grid, new_grid, x, y):
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


visited = set()
number_calls = 0


def bfs(grid, start, end):
    queue = deque([(start[0], start[1], 0)])
    old_steps = -1
    while queue:
        global number_calls
        number_calls += 1

        me_x, me_y, steps = queue.popleft()
        if steps > old_steps:
            print(f"{steps=} {len(queue)=}")

            # check dupes
            queue_as_set = set(queue)
            if len(queue) != len(queue_as_set):
                queue = deque(queue_as_set)

            if prune:
                # Trim the queue
                l = list(queue)
                l.sort(key=lambda x: x[0] + x[1], reverse=True)
                queue = deque(l[:prune_value])

            grid = update_grid(grid)
            old_steps = steps

        if (me_x, me_y) == end:
            print(f"Nice! We found it in {steps} steps")
            return steps
        # display_grid(new_grid, me_x, me_y)

        for tile in free_neighbours(grid, me_x, me_y):
            if True:  # tile not in visited:
                # visited.add(tile)
                queue.append((tile[0], tile[1], steps + 1))


trip1 = bfs(grid, (1, 0), (width - 2, height - 1))

trip2 = bfs(grid, (width - 2, height - 1), (1, 0))

trip3 = bfs(grid, (1, 0), (width - 2, height - 1))

print(f"{trip1=} {trip2=} {trip3=} {(trip1+trip2+trip3)=}")
