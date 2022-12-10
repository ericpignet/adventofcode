# https://adventofcode.com/2021/day/10

from collections import deque

with open("2021/input_files/day10") as f:
    lines = [line.rstrip() for line in f]

MATCHES = {"(": ")", "[": "]", "{": "}", "<": ">"}
REVERSE_MATCHES = {v: k for k, v in MATCHES.items()}
PART_1_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
PART_2_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
part1_total = 0
scores = []

for line in lines:
    q = deque()
    incorrect = False
    for c in line:
        if c in MATCHES:
            q.append(c)
        else:
            expected = q.pop()
            if c != MATCHES[expected]:
                # Invalid line
                part1_total += PART_1_POINTS[c]
                incorrect = True
                break
    else:
        # Incomplete line
        q1 = deque(line)
        q2 = deque()
        chars_to_add = ""
        i = 0
        points = 0
        while q1:
            c = q1.pop()
            if c in REVERSE_MATCHES:
                q2.append(c)
            elif q2:
                q2.pop()
            else:
                # Need to start adding
                points = points * 5 + PART_2_POINTS[MATCHES[c]]
                chars_to_add += MATCHES[c]
        print(f"{chars_to_add=}")
        scores.append(points)
scores.sort()
part2_middle = scores[len(scores) // 2]

print(f"{part1_total=}")
print(f"{part2_middle=}")
