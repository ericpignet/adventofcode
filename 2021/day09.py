# https://adventofcode.com/2021/day/9

# Part 2 would have been cleaner with BFS algorithm from low points

with open("2021/input_files/day09t") as f:
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

        if int(lines[y][x]) != 9:
            if y > 0 and int(lines[y - 1][x]) != 9:
                basin = next(bas for bas in basins if (x, y - 1) in bas)
                basin.add((x, y))
                if x > 0 and int(lines[y][x - 1]) != 9 and (x - 1, y) not in basin:
                    other_basin = next(bas for bas in basins if (x - 1, y) in bas)
                    basin.update(other_basin)
                    for i, bas in enumerate(basins):
                        if other_basin == bas:
                            del basins[i]
                            break

            elif x > 0 and int(lines[y][x - 1]) != 9:
                basin = next(bas for bas in basins if (x - 1, y) in bas)
                basin.add((x, y))
            else:
                basin = set([(x, y)])
                basins.append(basin)
for y in range(len(lines)):
    print("")
    for x in range(len(lines[0])):
        for i, bas in enumerate(basins):
            if (x, y) in bas:
                print(f"{i}", end="")
                break
        else:
            print(" ", end="")
print("")
sizes = []
for bas in basins:
    sizes.append(len(bas))
sizes.sort(reverse=True)
part2_product = sizes[0] * sizes[1] * sizes[2]
print(f"{part1_lowpoints=}")
print(f"{part2_product=}")
