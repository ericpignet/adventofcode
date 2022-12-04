# https://adventofcode.com/2021/day/6

with open("2021/input_files/day06t") as f:
    ages = list(map(int, f.readline().rstrip().split(",")))
print(ages)
for day in range(80):
    for i in range(len(ages)):
        if ages[i] == 0:
            ages[i] = 6
            ages.append(8)
        else:
            ages[i] -= 1
print(f"Nb fish: {len(ages)}")
