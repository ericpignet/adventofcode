# https://adventofcode.com/2022/day/13

from functools import cmp_to_key

with open("2022/input_files/day13") as f:
    data = "".join([line for line in f])
    pairs = [group.split("\n") for group in data.split("\n\n")]

# returns: (is finished, value if finished)
def evalLevel(exp1, exp2):
    if isinstance(exp1, int) and isinstance(exp2, int):
        if exp1 < exp2:
            return True, True
        elif exp1 > exp2:
            return True, False
        else:
            return False, False
    elif isinstance(exp1, int) and isinstance(exp2, list):
        return evalLevel([exp1], exp2)
    elif isinstance(exp1, list) and isinstance(exp2, int):
        return evalLevel(exp1, [exp2])
    elif isinstance(exp1, list) and isinstance(exp2, list):
        for i, elt in enumerate(exp1):
            if len(exp2) <= i:
                return True, False
            res = evalLevel(elt, exp2[i])
            if res[0]:
                return res
        if len(exp2) > len(exp1):
            return True, True
        # both lists have the same size with all elements equivalent
        return False, False


def compare(exp1, exp2):
    res = evalLevel(exp1, exp2)[1]
    # print(f"comparing {exp1} and {exp2}, found {res}")
    return -1 if res else 1


part1_sum_indices = 0
all_pairs = []

for iPair, pair in enumerate(pairs):
    exp1 = eval(pair[0])
    exp2 = eval(pair[1])
    all_pairs.append(exp1)
    all_pairs.append(exp2)

    res = evalLevel(exp1, exp2)
    if res[1]:
        part1_sum_indices += iPair + 1
    print(f"{iPair+1=} {res=}")

divider1 = [[2]]
divider2 = [[6]]
all_pairs.append(divider1)
all_pairs.append(divider2)

decoder1, decoder2 = 0, 0
all_pairs.sort(key=cmp_to_key(compare))

for i, packet in enumerate(all_pairs):
    if packet == divider1:
        decoder1 = i + 1
    elif packet == divider2:
        decoder2 = i + 1
        break

print(f"{part1_sum_indices=}")
print(f"part 2: {decoder1*decoder2}")
