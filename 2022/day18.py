# https://adventofcode.com/2022/day/18


def included(cube):
    for i in range(3):
        global max_coordinate
        if cube[i] < -1 or cube[i] > max_coordinate + 1:
            return False
    return True


def get_adjacents(cube):
    x, y, z = cube
    for adj in [
        (x, y, z + 1),  # up
        (x, y, z - 1),  # down
        (x - 1, y, z),  # left
        (x + 1, y, z),  # right
        (x, y - 1, z),  # back
        (x, y + 1, z),  # front
    ]:
        if included(adj):
            yield adj


droplet = []
max_coordinate = 0
with open("2022/input_files/day18") as f:
    for data in f:
        cube = tuple(map(int, data.rstrip().split(",")))
        max_coordinate = max(max_coordinate, max(cube))
        droplet.append(cube)

# Start BFS on top left corner to find exterior area
exterior = [(0, 0, 0)]
queue = []
queue.append((0, 0, 0))
while queue:
    cube = queue.pop(0)
    for adj in get_adjacents(cube):
        if adj not in exterior and adj not in droplet:
            exterior.append(adj)
            queue.append(adj)
print(f"{len(exterior)=}")
print(f"{len(droplet)=}")

part1_surface = 0
part2_surface = 0
for cube in droplet:
    for adj in get_adjacents(cube):
        if adj not in droplet:
            part1_surface += 1
            if adj in exterior:
                part2_surface += 1
print(f"{part1_surface=}")
print(f"{part2_surface=}")
