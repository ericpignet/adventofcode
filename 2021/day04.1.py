with open("2021/input_files/day04") as f:
    lines = [line.rstrip() for line in f]
calls = lines[0].split(",")
boards = []
marks = []
i = 2
while i < len(lines):
    board = []
    mark = []
    board.append(lines[i].split())
    i += 1
    board.append(lines[i].split())
    i += 1
    board.append(lines[i].split())
    i += 1
    board.append(lines[i].split())
    i += 1
    board.append(lines[i].split())
    boards.append(board)
    mark.append([False, False, False, False, False])
    mark.append([False, False, False, False, False])
    mark.append([False, False, False, False, False])
    mark.append([False, False, False, False, False])
    mark.append([False, False, False, False, False])
    marks.append(mark)
    i += 2


class GetOutOfLoop(Exception):
    pass


try:
    for call in calls:
        for i_board, board in enumerate(boards):
            col_all_marked = [True, True, True, True, True]
            for i, row in enumerate(board):
                row_all_marked = True
                for j, nb in enumerate(row):
                    if nb == call:
                        marks[i_board][i][j] = True
                    if not marks[i_board][i][j]:
                        row_all_marked = False
                        col_all_marked[j] = False

                if row_all_marked:
                    print(f"Board {i_board} has won on {call=} for row {i=}")
                    raise GetOutOfLoop
            for i in range(5):
                if col_all_marked[i]:
                    print(f"Board {i_board} has won on {call=} for col {i=}")
                    raise GetOutOfLoop
except GetOutOfLoop:
    pass
sum_unmarked = 0
for i, row in enumerate(board):
    for j, nb in enumerate(row):
        if not marks[i_board][i][j]:
            sum_unmarked += int(nb)
print(f"{sum_unmarked=} {call=}")
print(f"Result={sum_unmarked*int(call)}")
