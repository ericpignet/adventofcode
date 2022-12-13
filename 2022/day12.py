# https://adventofcode.com/2022/day/12

from typing import List
from collections import deque
import copy

grid = []


class Point:
    def __init__(self, x, y, elevation):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.visited = False
        self.start = False
        self.end = False

    def get_adjacent_tiles(self, grid):
        for dir in [
            (self.x - 1, self.y),
            (self.x + 1, self.y),
            (self.x, self.y - 1),
            (self.x, self.y + 1),
        ]:
            if p := find_point(grid, dir[0], dir[1]):
                yield p

    def __str__(self):
        return f"{self.x},{self.y}"


def find_point(grid, x, y):
    try:
        return next(p for p in grid if p.x == x and p.y == y)
    except StopIteration:
        return None


class GetOutOfLoop(Exception):
    pass


with open("2022/input_files/day12t") as f:
    for y, data in enumerate(f):
        data = data.rstrip()
        for x, c in enumerate(data):
            p = Point(x, y, c)
            if c == "S":
                p.elevation = "a"
                p.start = True
            elif c == "E":
                p.elevation = "z"
                p.end = True
            grid.append(p)

start = next(x for x in grid if x.start)
end = next(x for x in grid if x.end)

# BFS algorithm
try:
    queue = []
    queue.append([start])
    start.visited = True
    while queue:
        path = queue.pop(0)
        tile = path[-1]
        if tile == end:
            print(f"|".join(map(str, path)))
            raise GetOutOfLoop
        for adj_tile in tile.get_adjacent_tiles(grid):
            if (
                ord(adj_tile.elevation) <= ord(tile.elevation) + 1
                and not adj_tile.visited
            ):
                # new_path = copy.deepcopy(path)
                new_path = list(path)
                new_path.append(adj_tile)
                queue.append(new_path)
                adj_tile.visited = True

except GetOutOfLoop:
    print(f"{len(path)-1=}")
