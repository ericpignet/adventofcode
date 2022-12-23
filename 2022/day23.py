# https://adventofcode.com/2022/day/23
# To profile the program, run python -m cProfile 2022\day23.2.py

elves = {}
directions = ["N", "S", "W", "E"]
display = False

with open("2022/input_files/day23t") as f:
    for y, line in enumerate(f):
        line = line.rstrip()
        for x, char in enumerate(line):
            if char == "#":
                elves[(x, y)] = {}

cycle = 0
while True:
    cycle += 1
    # Consider adjacent directions
    for pos in elves:
        if not (
            (pos[0] - 1, pos[1] - 1) not in elves
            and (pos[0], pos[1] - 1) not in elves
            and (pos[0] + 1, pos[1] - 1) not in elves
            and (pos[0] - 1, pos[1]) not in elves
            and (pos[0] + 1, pos[1]) not in elves
            and (pos[0] - 1, pos[1] + 1) not in elves
            and (pos[0], pos[1] + 1) not in elves
            and (pos[0] + 1, pos[1] + 1) not in elves
        ):
            for direction in directions:
                if direction == "N":
                    if (
                        (pos[0] - 1, pos[1] - 1) not in elves
                        and (pos[0], pos[1] - 1) not in elves
                        and (pos[0] + 1, pos[1] - 1) not in elves
                    ):
                        elves[pos] = (pos[0], pos[1] - 1)
                        break
                elif direction == "S":
                    if (
                        (pos[0] - 1, pos[1] + 1) not in elves
                        and (pos[0], pos[1] + 1) not in elves
                        and (pos[0] + 1, pos[1] + 1) not in elves
                    ):
                        elves[pos] = (pos[0], pos[1] + 1)
                        break
                elif direction == "W":
                    if (
                        (pos[0] - 1, pos[1] - 1) not in elves
                        and (pos[0] - 1, pos[1]) not in elves
                        and (pos[0] - 1, pos[1] + 1) not in elves
                    ):
                        elves[pos] = (pos[0] - 1, pos[1])
                        break
                elif direction == "E":
                    if (
                        (pos[0] + 1, pos[1] - 1) not in elves
                        and (pos[0] + 1, pos[1]) not in elves
                        and (pos[0] + 1, pos[1] + 1) not in elves
                    ):
                        elves[pos] = (pos[0] + 1, pos[1])
                        break

    # Do the moves
    new_elves = {}
    at_least_one_move = False
    for pos in elves:
        if elves[pos]:
            try:
                val = elves[pos]
                next(k for k, v in elves.items() if k != pos and v == val)
                new_elves[pos] = {}
            except StopIteration:
                # No other elf going to the same place, we can move
                new_elves[elves[pos]] = {}
                at_least_one_move = True
        else:
            new_elves[pos] = {}
    if not at_least_one_move:
        break
    elves = new_elves

    # Rotate directions
    directions.append(directions.pop(0))

    if display:
        min_x = min(x[0] for x in elves)
        max_x = max(x[0] for x in elves)
        min_y = min(x[1] for x in elves)
        max_y = max(x[1] for x in elves)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                print("#" if (x, y) in elves else ".", end="")
            print()
        print()
    if cycle % 100 == 0:
        print(f"{cycle=}")

    if cycle == 10:
        min_x = min(x[0] for x in elves)
        max_x = max(x[0] for x in elves)
        min_y = min(x[1] for x in elves)
        max_y = max(x[1] for x in elves)
        empty_tiles = 0
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) not in elves:
                    empty_tiles += 1
        print(f"Part 1: {empty_tiles=}")

print(f"Part 2: {cycle=}")
