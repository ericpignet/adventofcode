# https://adventofcode.com/2022/day/10

inputs = []
with open("2022/input_files/day10") as f:
    lines = [line.rstrip() for line in f]

clock = 0
x = 1
part1_strengths = 0


def check_clock(clock, x):
    # Part 1
    if clock in (20, 60, 100, 140, 180, 220):
        global part1_strengths
        part1_strengths += clock * x
        # print(f"{clock=} {x=} {clock*x}")

    # Part 2
    pixel = "#" if (clock - 1) % 40 in (x - 1, x, x + 1) else "."
    print(pixel, end="")
    if clock % 40 == 0:
        print()


for input in lines:
    if input[0:4] == "noop":
        clock += 1
        check_clock(clock, x)
    else:
        value = int(input[5:])
        clock += 1
        check_clock(clock, x)
        clock += 1
        check_clock(clock, x)
        x += value

print(f"{part1_strengths=}")
