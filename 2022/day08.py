def isVisible(grid, x, y):
    # above
    vis_from_above = True
    for yy in range(0, y):
        if int(grid[yy][x]) >= int(grid[y][x]):
            vis_from_above = False
            break
    # left
    vis_from_left = True
    for xx in range(0, x):
        if int(grid[y][xx]) >= int(grid[y][x]):
            vis_from_left = False
            break
    # right
    vis_from_right = True
    for xx in range(x + 1, len(grid[0])):
        if int(grid[y][xx]) >= int(grid[y][x]):
            vis_from_right = False
            break
    # down
    vis_from_down = True
    for yy in range(y + 1, len(grid)):
        if int(grid[yy][x]) >= int(grid[y][x]):
            vis_from_down = False
            break
    return vis_from_above or vis_from_left or vis_from_right or vis_from_down


def calcScenicScore(grid, x, y):
    # Up
    score_up = 0
    for yy in range(y - 1, -1, -1):
        score_up += 1
        if int(grid[yy][x]) >= int(grid[y][x]):
            break
    # left
    score_left = 0
    for xx in range(x - 1, -1, -1):
        score_left += 1
        if int(grid[y][xx]) >= int(grid[y][x]):
            break
    # right
    score_right = 0
    for xx in range(x + 1, len(grid[0])):
        score_right += 1
        if int(grid[y][xx]) >= int(grid[y][x]):
            break
    # down
    score_down = 0
    for yy in range(y + 1, len(grid)):
        score_down += 1
        if int(grid[yy][x]) >= int(grid[y][x]):
            break
    return score_up * score_left * score_right * score_down


grid = []

with open("2022/input_files/day08") as f:
    grid = [line.rstrip() for line in f]

part1_nb_visible = 0
for y, row in enumerate(grid):
    for x, tree in enumerate(row):
        if isVisible(grid, x, y):
            part1_nb_visible += 1
print(f"{part1_nb_visible=}")

part2_highest_score = 0
winner_x, winner_y = 0, 0
for y, row in enumerate(grid):
    for x, tree in enumerate(row):
        score = calcScenicScore(grid, x, y)
        if score > part2_highest_score:
            winner_x, winner_y = x, y
            part2_highest_score = score
print(f"{(winner_x,winner_y)=}")
print(f"{part2_highest_score=}")
