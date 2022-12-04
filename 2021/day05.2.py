# https://adventofcode.com/2021/day/5

with open("2021/input_files/day05") as f:
    lines = [line.rstrip() for line in f]
grid = [[0] * 1000 for i in range(1000)]

for line in lines:
    data = line.split(" -> ")
    x1, y1 = map(int, data[0].split(","))
    x2, y2 = map(int, data[1].split(","))
    if x1 == x2:
        # vertical line
        # print(f"vertical line with {x1=} and from {y1=} to {y2=}")
        if y1 <= y2:
            for y in range(y1, y2 + 1):
                grid[y][x1] += 1
        else:
            for y in range(y2, y1 + 1):
                grid[y][x1] += 1
    elif y1 == y2:
        # horizontal line
        # print(f"horizontal line with {y1=} and from {x1=} to {x2=}")
        if x1 <= x2:
            for x in range(x1, x2 + 1):
                grid[y1][x] += 1
        else:
            for x in range(x2, x1 + 1):
                grid[y1][x] += 1
    else:
        # diagonal line
        # print(f"diagonal line from {y1=} to {y2=} and from {x1=} to {x2=}")
        y = y1
        x_step = 1 if x2 >= x1 else -1
        y_step = 1 if y2 >= y1 else -1
        for x in range(x1, x2 + x_step, x_step):
            grid[y][x] += 1
            y += y_step

overlapping_points = set()
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col > 1:
            overlapping_points.add((x, y))
        # print(col, end="")
    # print()
print(f"Nb overlapping={len(overlapping_points)}")
