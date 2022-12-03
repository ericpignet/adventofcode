points = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}

total_score = 0
with open("2022/input_files/day02") as f:
    for data in f:
        opponent = data[0]
        me = data[2]
        score = 0
        if me == "X":
            score += 1
        elif me == "Y":
            score += 2
        elif me == "Z":
            score += 3
        score += points[(opponent, me)]
        total_score += score
print(f"Total score: {total_score}")
