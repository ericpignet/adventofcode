# https://adventofcode.com/2021/day/8

with open("2021/input_files/day09") as f:
    lines = [line.rstrip() for line in f]

part1_lowpoints = 0

basins = []


def adjacents(x, y):
    res = []
    if y > 0:
        res.append(int(lines[y - 1][x]))
    if x > 0:
        res.append(int(lines[y][x - 1]))
    if x < len(lines[0]) - 1:
        res.append(int(lines[y][x + 1]))
    if y < len(lines) - 1:
        res.append(int(lines[y + 1][x]))
    return res


for y in range(len(lines)):
    for x in range(len(lines[y])):
        if int(lines[y][x]) < min(adjacents(int(x), int(y))):
            part1_lowpoints += int(lines[y][x]) + 1

        if y > 0 and lines[y - 1][x] != 9:
            pass
        # TODO

print(f"{part1_lowpoints=}")
