max_seat_id = 0
with open("2020/input_files/day05") as f:
    for data in f:
        boardingpass = data.rstrip()

        row = 0
        for power, i in enumerate(range(len(boardingpass)-4, -1, -1)):
            if boardingpass[i] == 'B':
                row = row + pow(2, power)

        col = 0
        for power, i in enumerate(range(len(boardingpass)-1, len(boardingpass)-4, -1)):
            if boardingpass[i] == 'R':
                col = col + pow(2, power)

        seat_id = row * 8 + col
        max_seat_id = max(max_seat_id, seat_id)
print(f"{max_seat_id=}")