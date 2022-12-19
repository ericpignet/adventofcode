# https://adventofcode.com/2022/day/15

import re


def parse_nums(line, negatives=True):
    """
    Returns a list of numbers in `line`.
    Pass negatives=False to parse 1-2 as [1, 2].
    """
    num_re = r"-?\d+" if negatives else r"\d+"
    return [int(n) for n in re.findall(num_re, line)]


sensors = []
with open("2022/input_files/day15") as f:
    for line in f:
        line = line.rstrip()
        nums = parse_nums(line)
        sensors.append(nums)

# target_row = 0
# size = 20
size = 4000000
for target_row in range(size):
    intervals = []

    for sensor in sensors:
        # For each sensor, calculate where it intersects with y=10 or 2,000,000 (left/right). Then do a union between all the horizontal intervals
        # calculate manhattan distance
        dist = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
        y_offset = target_row - sensor[1]
        x_offset = dist - abs(y_offset)
        intervals.append((sensor[0] - x_offset, sensor[0] + x_offset))

    # calculate union
    union = []
    for begin, end in sorted(intervals):
        if union and union[-1][1] >= begin - 1:
            union[-1][1] = max(union[-1][1], end)
        else:
            union.append([begin, end])

    # remove possible intervals fully outside the problem's range
    to_delete = []
    for interval in union:
        if interval[1] < 0 or interval[0] > size:
            to_delete.append(interval)
    for todel in to_delete:
        union.remove(todel)

    if len(union) > 1:
        print(f"Found {target_row=} {union[1][0]=}")
        print(f"Part 2 res: {(union[1][0] * 4000000)+target_row}")
        break
    if target_row % 100000 == 0:
        print(f"{target_row=}")
