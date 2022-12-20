# https://adventofcode.com/2022/day/20


def move_backward_for_comparison(l, n, occurence):
    old_index = l.index((n, occurence))
    if old_index - 1 == 0:
        new_index = len(l) - 1
    elif old_index - 1 == -1:
        new_index = len(l) - 2
    else:
        new_index = old_index - 1
    l.insert(new_index, l.pop(old_index))
    pass


def move_forward_for_comparison(l, n, occurence):
    old_index = l.index((n, occurence))
    if old_index + 1 == len(l):
        new_index = 1
    else:
        new_index = old_index + 1
    l.insert(new_index, l.pop(old_index))


is_part_2 = True
original_sequence = []
with open("2022/input_files/day20") as f:
    for data in f:
        n = int(data.rstrip())
        if is_part_2:
            n *= 811589153
        c = [x[0] for x in original_sequence].count(n)
        original_sequence.append((n, c))

sequence = original_sequence.copy()
sequence_for_comparison = original_sequence.copy()
comparison_mode = False

for _ in range(10 if is_part_2 else 1):
    for n, occurence in original_sequence:
        # expected
        if comparison_mode:
            if n > 0:
                for j in range(n):
                    move_forward_for_comparison(sequence_for_comparison, n, occurence)
            elif n < 0:
                for j in range(-n):
                    move_backward_for_comparison(sequence_for_comparison, n, occurence)

        # fast
        old_index = sequence.index((n, occurence))
        new_index = old_index + n
        new_index %= len(sequence) - 1

        if new_index == 0:
            new_index = len(sequence) - 1

        sequence.insert(new_index, sequence.pop(old_index))

        if comparison_mode and sequence != sequence_for_comparison:
            print(f"Found isue at item {(n, occurence)=}")
            for k in range(len(sequence)):
                if sequence[k] != sequence_for_comparison[k]:
                    print(
                        f"At number {k=} {sequence[k]=} {sequence_for_comparison[k]=}"
                    )
            break

i0 = sequence.index((0, 0))
a = (i0 + 1000) % len(sequence)
b = (i0 + 2000) % len(sequence)
c = (i0 + 3000) % len(sequence)
print(f"{i0=} {a=} {b=} {c=}")
print(f"{sequence[a][0]=} {sequence[b][0]=} {sequence[c][0]=}")
print(f"{sequence[a][0]+sequence[b][0]+sequence[c][0]=}")
