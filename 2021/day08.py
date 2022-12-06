# https://adventofcode.com/2021/day/8

with open("2021/input_files/day08") as f:
    lines = [line.rstrip() for line in f]

part1_nb_1478 = 0
part2_total = 0
for line in lines:
    signals, outputs = line.split(" | ")
    signals = signals.split()
    outputs = outputs.split()
    digits = {}

    for output in outputs:
        if len(output) in (2, 4, 3, 7):
            part1_nb_1478 += 1

    def reverse_range(a_list):
        return range(len(a_list) - 1, -1, -1)

    for i in reverse_range(signals):
        if len(signals[i]) == 2:
            digits[1] = set(signals[i])
            del signals[i]
        elif len(signals[i]) == 4:
            digits[4] = set(signals[i])
            del signals[i]
        elif len(signals[i]) == 3:
            digits[7] = set(signals[i])
            del signals[i]
        elif len(signals[i]) == 7:
            digits[8] = set(signals[i])
            del signals[i]
    # remaining 0, 2, 3, 5, 6, 9
    # the ones including 4 are 8 and 9 => gives us 9
    for i in reverse_range(signals):
        if digits[4].issubset(signals[i]):
            digits[9] = set(signals[i])
            del signals[i]
            break
    # remaining 0, 2, 3, 5, 6,
    # between the ones with 6 segments (0, 6) the one including 1 is 0, so the other one is 6
    for i in reverse_range(signals):
        if len(signals[i]) == 6:
            if digits[1].issubset(signals[i]):
                digits[0] = set(signals[i])
                del signals[i]
            else:
                digits[6] = set(signals[i])
                del signals[i]
    # remaining 2, 3, 5,
    # the one including 1 is 3
    for i in reverse_range(signals):
        if digits[1].issubset(signals[i]):
            digits[3] = set(signals[i])
            del signals[i]
            break
    # remaining 2, 5
    # the one included in 6 is 5
    for i in reverse_range(signals):
        if set(signals[i]).issubset(digits[6]):
            digits[5] = set(signals[i])
            del signals[i]
            break
    digits[2] = set(signals[0])
    print(f"{digits=}")

    number = ""
    for output in outputs:
        for digit, segments in digits.items():
            if segments == set(output):
                number += str(digit)
                break
    part2_total += int(number)

print(f"{part1_nb_1478=}")
print(f"{part2_total=}")
