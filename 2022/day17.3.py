# https://adventofcode.com/2022/day/17

# TEST
# 28:       56      73   50 +22 68 +12
# 63:  +35 112 +56 129
# 98:  +35 165 +53 182  120 +22 174 +9    184 +2
# 133: +35 218 +53 235  155 +22 227 +9
# 168: +35 271 +53 288
# 203: +35 324

# 28 571 428 570.6 cycles of 35
# 28+28571428570*35 = 999,999,999,978
# +22

# REAL

# 187: 291               306
# 1927: +1740 3027 +2736 3042    2920: +993   4566 +1539 4574 +1532
# 3667: +1740 5751 +2724 5766    4660: +993   7290 +1539 7298 +1532
# 5407: +1740 8475 +2724 8490    6400: +993  10014 +1539
# 7147: 11199
# 8887: 13923

# 187 + 574,712,643*1740 + 993

# 291 + 574712643*2724 + 1539
# => 1,565,517,241,362  too low
# => 1,565,517,241,374  too low
#        1565517241375  not
#        1565517241378  not
#        1565517241380  not
#    1,565,517,241,384 too high
# 1927+574712642*1740+993
# 3027+1565517236808+1539

# 3667 + 574,712,641*1740 + 993


import functools

with open("input_files/day17") as f:
    jets = f.readline().rstrip()


def highest_rock(grid):
    for i, row in enumerate(grid):
        if row.count(1) == 2:
            break
    return i - 1


def highest_ground(grid):
    hg = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        hg[i] = max([x[1] for x in grid if x[0] == i])
    return hg


def add_rock(grid, shape, x, y):
    for pos in shape:
        grid.append((x + pos[0], y + pos[1]))


def can_add_rock(grid, shape, x, y):
    for pos in shape:
        if (x + pos[0], y + pos[1]) in grid or (x + pos[0] in (-1, 7)):
            return False
    return True


def del_rock(grid, shape, x, y):
    for pos in shape:
        grid.remove((x + pos[0], y + pos[1]))


@functools.lru_cache(maxsize=None)
def fall_rock(grid_tuple, cur_shape: int, cur_jet: int):

    high = max([x[1] for x in grid_tuple])
    grid_tuple = list(grid_tuple)

    x = 2
    y = high + 4
    while True:
        # Apply jet
        new_x = x + (1 if jets[cur_jet] == ">" else -1)
        cur_jet += 1
        cur_jet %= len(jets)

        if can_add_rock(grid_tuple, shapes[cur_shape], new_x, y):
            x = new_x
        # Fall
        new_y = y - 1
        if y < 0:
            pass
        if can_add_rock(grid_tuple, shapes[cur_shape], x, new_y):
            y = new_y
        else:
            break
    add_rock(grid_tuple, shapes[cur_shape], x, y)

    return tuple(grid_tuple), cur_jet


grid_tuple = ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0))

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]

cur_shape = -1
cur_jet = 0
offset = 0
searched_tuple_real = (
    (3, 0),
    (3, 1),
    (2, 0),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (3, 4),
    (2, 5),
    (3, 5),
    (0, 6),
    (1, 6),
    (2, 6),
    (3, 6),
    (3, 7),
    (2, 8),
    (3, 8),
    (4, 8),
    (3, 9),
    (2, 10),
    (3, 10),
    (4, 10),
    (4, 11),
    (4, 12),
    (0, 7),
    (0, 8),
    (0, 9),
    (0, 10),
    (2, 11),
    (3, 11),
    (2, 12),
    (3, 12),
    (1, 13),
    (2, 13),
    (3, 13),
    (4, 13),
    (5, 13),
    (4, 14),
    (5, 14),
    (6, 14),
    (5, 15),
    (0, 0),
    (1, 0),
    (4, 0),
    (5, 0),
    (6, 0),
)
searched_tuple_test = (
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (1, 0),
    (2, 0),
    (1, 5),
    (2, 5),
    (3, 5),
    (4, 5),
    (5, 5),
    (4, 6),
    (5, 6),
    (6, 6),
    (5, 7),
    (4, 8),
    (5, 8),
    (6, 8),
    (6, 9),
    (6, 10),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (1, 10),
    (2, 10),
    (1, 11),
    (2, 11),
    (2, 12),
    (3, 12),
    (4, 12),
    (5, 12),
    (3, 13),
    (2, 14),
    (3, 14),
    (4, 14),
    (3, 15),
    (0, 15),
    (1, 15),
    (2, 15),
    (2, 16),
    (2, 17),
    (0, 0),
    (3, 0),
    (5, 0),
    (6, 0),
)
# for nb_rock in range(2022):
for nb_rock in range(1000000000000):
    if nb_rock == 120:
        pass
    if grid_tuple == searched_tuple_real:
        pass
    print(f"{nb_rock=} {fall_rock.cache_info()} {grid_tuple=}")
    cur_shape += 1
    cur_shape %= 5

    grid_tuple, cur_jet = fall_rock(grid_tuple, cur_shape, cur_jet)

    # if nb_rock % 1000000 == 0:
    #     print(f"{nb_rock=}")
    #     print(fall_rock.cache_info())
    if nb_rock % 100000 == 0:
        print(f"{nb_rock=} {fall_rock.cache_info()}")

    hg = highest_ground(grid_tuple)
    lowest_hg = min(hg)
    if lowest_hg > 10:
        lowest_hg = lowest_hg - 10
        offset += lowest_hg
        new_grid_list = []
        for t in grid_tuple:
            if t[1] >= lowest_hg:
                new_grid_list.append((t[0], t[1] - lowest_hg))
        for i in range(7):
            if (i, 0) not in new_grid_list:
                new_grid_list.append((i, 0))

        grid_tuple = tuple(new_grid_list)
    res = offset + max(hg)

print(f"{max(hg)+offset=}")
print(fall_rock.cache_info())
