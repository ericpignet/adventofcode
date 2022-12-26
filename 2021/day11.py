# https://adventofcode.com/2021/day/11

from itertools import count

grid = []
with open("2021/input_files/day11") as f:
    for data in f:
        grid.append([int(x) for x in "".join(data.rstrip())])


def neighbours(grid, x, y):
    if y > 0:
        if x > 0:
            yield (x - 1, y - 1)
        yield (x, y - 1)
        if x < len(grid[0]) - 1:
            yield (x + 1, y - 1)
    if x > 0:
        yield (x - 1, y)
    yield (x, y)
    if x < len(grid[0]) - 1:
        yield (x + 1, y)
    if y < len(grid) - 1:
        if x > 0:
            yield (x - 1, y + 1)
        yield (x, y + 1)
        if x < len(grid[0]) - 1:
            yield (x + 1, y + 1)


def try_flash(grid, x, y, step):
    if grid[y][x] > 9:
        if step < 100:
            global flashes_in_100_steps
            flashes_in_100_steps += 1
        global total_flashes_by_step
        total_flashes_by_step += 1
        grid[y][x] = 0
        for neigh in neighbours(grid, x, y):
            if grid[neigh[1]][neigh[0]] != 0:
                grid[neigh[1]][neigh[0]] += 1
                try_flash(grid, neigh[0], neigh[1], step)


flashes_in_100_steps = 0
for step in count(0):
    total_flashes_by_step = 0
    for y, row in enumerate(grid):
        for x, octopus in enumerate(row):
            grid[y][x] += 1
    for y, row in enumerate(grid):
        for x, octopus in enumerate(row):
            try_flash(grid, x, y, step)
    if total_flashes_by_step == len(grid) ** 2:
        break

print(f"Part 1: {flashes_in_100_steps=}")
print(f"Part 2: {step+1=}")
