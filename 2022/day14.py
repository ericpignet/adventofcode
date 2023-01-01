# https://adventofcode.com/2022/day/14

# Parsing input
paths = []
grid = set()
with open("2022/input_files/day14") as f:
    for data in f:
        points = data.rstrip().split(" -> ")
        points2 = []
        for ps in points:
            pss = ps.split(",")
            point = (int(pss[0]), int(pss[1]))
            points2.append(point)
        paths.append(points2)

# Generating full list of rocks
part1_nb_still_sand = 0
part2_nb_still_sand = 0
still_sands = set()
lowest_y = 0
for path in paths:
    last_point = ()
    for point in path:
        if point[1] > lowest_y:
            lowest_y = point[1]
        if last_point:
            for i in range(min(last_point[0], point[0]), max(last_point[0], point[0]) + 1):
                for j in range(min(last_point[1], point[1]), max(last_point[1], point[1]) + 1):
                    grid.add((i, j))
        last_point = point


def is_blocked(grid, still_sands, pos):
    return pos in grid or pos in still_sands or pos[1] >= lowest_y + 2


# Dropping sand elements
while True:
    # one unit of sand starts falling
    sand = (500, 0)
    while True:
        if part1_nb_still_sand == 0 and sand[1] > lowest_y:
            part1_nb_still_sand = len(still_sands)
        if not is_blocked(grid, still_sands, (sand[0], sand[1] + 1)):
            sand = (sand[0], sand[1] + 1)
        elif not is_blocked(grid, still_sands, (sand[0] - 1, sand[1] + 1)):
            sand = (sand[0] - 1, sand[1] + 1)
        elif not is_blocked(grid, still_sands, (sand[0] + 1, sand[1] + 1)):
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            still_sands.add(sand)
            break
    if sand == (500, 0):
        break
part2_nb_still_sand = len(still_sands)

print(f"{part1_nb_still_sand=}")
print(f"{part2_nb_still_sand=}")
