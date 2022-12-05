# https://adventofcode.com/2021/day/7

# I used a cache because I didn't know that 1+2+3+..+n = n(n+1)/2

with open("2021/input_files/day07") as f:
    positions = list(map(int, f.readline().rstrip().split(",")))
cache = {}
min_fuel = 999999999
min_pos = min(positions)
max_pos = max(positions)
for pos in range(min_pos, max_pos + 1):
    print(pos)
    fuel = 0
    for crab in positions:
        dist = abs(pos - crab)
        if dist in cache:
            fuel += cache[dist]
        else:
            crab_fuel = 0
            for i in range(1, dist + 1):
                crab_fuel += i
            cache[dist] = crab_fuel
            fuel += crab_fuel
    if fuel < min_fuel:
        min_fuel = fuel

print(f"{min_fuel=}")
