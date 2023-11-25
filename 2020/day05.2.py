max_seat_id = 0
paxlist = []
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
        paxlist.append(seat_id)
print(f"{max_seat_id=}")

previous_empty = True
for seat_id in range(max_seat_id):
    if previous_empty and seat_id in paxlist:
        previous_empty = False
    if not previous_empty and seat_id not in paxlist:
        print(f"{seat_id=}")
