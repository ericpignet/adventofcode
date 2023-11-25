# https://adventofcode.com/2020/day/01

with open("2020/input_files/day01") as f:
    entries = [int(line.rstrip()) for line in f]

for i, entry in enumerate(entries):
    for other_entry in entries[i:]:
        if entry + other_entry == 2020:
            print(f"Part 1: {entry * other_entry}")
            break

for i, entry in enumerate(entries):
    for j, other_entry in enumerate(entries[i:]):
        for third_entry in entries[j:]:
            if entry + other_entry + third_entry == 2020:
                print(f"Part 2: {entry * other_entry * third_entry}")
                exit()
