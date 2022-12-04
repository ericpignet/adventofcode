nb_fully_contained = 0
with open("2022/input_files/day04") as f:
    for line in f:
        elf1, elf2 = line.rstrip().split(",")
        # print(line)
        elf1_lower, elf1_upper = elf1.split("-")
        elf1_lower = int(elf1_lower)
        elf1_upper = int(elf1_upper)
        elf2_lower, elf2_upper = elf2.split("-")
        elf2_lower = int(elf2_lower)
        elf2_upper = int(elf2_upper)

        if (elf1_lower >= elf2_lower and elf1_upper <= elf2_upper) or (
            elf2_lower >= elf1_lower and elf2_upper <= elf1_upper
        ):
            nb_fully_contained += 1

print(f"nb_fully_contained: {nb_fully_contained}")
