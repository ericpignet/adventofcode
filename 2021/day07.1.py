# https://adventofcode.com/2021/day/7

with open("2021/input_files/day07") as f:
    positions = list(map(int, f.readline().rstrip().split(",")))

min_fuel = 999999
min_pos = min(positions)
max_pos = max(positions)
for pos in range(min_pos, max_pos + 1):
    fuel = 0
    for crab in positions:
        fuel += abs(pos - crab)
    if fuel < min_fuel:
        min_fuel = fuel
1
print(f"{min_fuel=}")
