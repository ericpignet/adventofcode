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
        adjacent_tiles = []
        if find_point(grid, self.x - 1, self.y):
            adjacent_tiles.append(find_point(grid, self.x - 1, self.y))
        if find_point(grid, self.x + 1, self.y):
            adjacent_tiles.append(find_point(grid, self.x + 1, self.y))
        if find_point(grid, self.x, self.y - 1):
            adjacent_tiles.append(find_point(grid, self.x, self.y - 1))
        if find_point(grid, self.x, self.y + 1):
            adjacent_tiles.append(find_point(grid, self.x, self.y + 1))
        return adjacent_tiles

    def __str__(self):
        return f"{self.x},{self.y}"


def find_point(grid, x, y):
    try:
        point = next(p for p in grid if p.x == x and p.y == y)
        return point
    except StopIteration:
        return None


class GetOutOfLoop(Exception):
    pass


with open("2022/input_files/day12") as f:
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

cache = {}
shortest_path = 9999999

for p in grid:
    if p.elevation == "a":
        if (p.x, p.y) in cache:
            shortest_path = min(shortest_path, cache[(p.x, p.y)])
            print(f"starting pos: {str(p)}")
            print(f"{cache[(p.x, p.y)]=}")
        else:
            # BFS algorithm
            start = p
            path_length = 999999999
            best_path = []
            try:
                queue = []
                queue.append([p])
                for p_to_visit in grid:
                    p_to_visit.visited = False
                start.visited = True
                while queue:
                    path = queue.pop(0)
                    tile = path[-1]

                    # We found the end
                    if tile == end:
                        print(f"|".join(map(str, path)))
                        for pp_i, pp in enumerate(path):
                            cache[(pp.x, pp.y)] = len(path[pp_i:]) - 1
                        path_length = len(path) - 1
                        raise GetOutOfLoop

                    # Is it in the cache?
                    if (tile.x, tile.y) in cache:
                        length = len(path) - 1 + cache[(tile.x, tile.y)]
                        if length < path_length:
                            path_length = length
                            best_path = path

                    else:
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
                pass
            if best_path:
                for pp_i, pp in enumerate(best_path):
                    cache[(pp.x, pp.y)] = (
                        len(best_path[pp_i:])
                        - 1
                        + cache[(best_path[-1].x, best_path[-1].y)]
                    )
            if path_length < 999999:  # these paths don't even terminate
                print(f"starting pos: {str(start)}")
                print(f"{path_length=}")
                shortest_path = min(shortest_path, path_length)
print(f"{shortest_path=}")
