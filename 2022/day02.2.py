what_to_play = {
    ("A", "X"): "C",
    ("A", "Y"): "A",
    ("A", "Z"): "B",
    ("B", "X"): "A",
    ("B", "Y"): "B",
    ("B", "Z"): "C",
    ("C", "X"): "B",
    ("C", "Y"): "C",
    ("C", "Z"): "A",
}

total_score = 0
with open("2022/input_files/day02") as f:
    for data in f:
        opponent = data[0]
        target = data[2]
        me = what_to_play[(opponent, target)]
        score = 0
        if target == "Y":
            score += 3
        elif target == "Z":
            score += 6
        if me == "A":
            score += 1
        elif me == "B":
            score += 2
        elif me == "C":
            score += 3
        total_score += score
print(f"Total score: {total_score}")
