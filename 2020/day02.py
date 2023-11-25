import re

# Part 1 with basic syntax
part1_nb_valid = 0
with open("2020/input_files/day02") as f:
    for data in f:
        match = re.match(r"(\d+)-(\d+) (\w): (\w+)", data.rstrip())
        min = int(match.group(1))
        max =  int(match.group(2))
        char = match.group(3)
        password = match.group(4)
        if min <= password.count(char) <= max:
            part1_nb_valid += 1
print(f"{part1_nb_valid=}")

# Part 1 with better Regex syntax:
part1_nb_valid = 0
with open("2020/input_files/day02") as f:
    for data in f:
        match = re.search(r"(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<password>\w+)", data.rstrip()).groupdict()
        if int(match['min']) <= match['password'].count(match['char']) <= int(match['max']):
            part1_nb_valid += 1
print(f"{part1_nb_valid=}")

# Part 2
part2_nb_valid = 0
with open("2020/input_files/day02") as f:
    for data in f:
        match = re.match(r"(\d+)-(\d+) (\w): (\w+)", data.rstrip())
        pos1 = int(match.group(1))
        pos2 =  int(match.group(2))
        char = match.group(3)
        password = match.group(4)
        if ((password[pos1-1] == char and password[pos2-1] != char) or
            (password[pos1-1] != char and password[pos2-1] == char)):
            part2_nb_valid += 1
print(f"{part2_nb_valid=}")
