from collections import Counter

# https://adventofcode.com/2021/day/6

with open("2021/input_files/day06") as f:
    ages = list(map(int, f.readline().rstrip().split(",")))
print(ages)
c = Counter(ages)
for day in range(256):
    print(f"{day=} {c=}")
    nb_new = c[0]
    for i in range(0, 8):
        c[i] = c[i + 1]
    c[8] = nb_new
    c[6] += nb_new

print(f"Nb fish: {c.total()}")
